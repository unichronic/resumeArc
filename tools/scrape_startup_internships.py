#!/usr/bin/env python3
"""Scrape startup-heavy internship sources into CSV and Markdown reports.

The scraper intentionally uses public pages/APIs and skips boards that block
automated access or require login. It favors startup-heavy sources and official
ATS APIs over broad job aggregators.
"""

from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now().strftime("%Y_%m_%d")
OUT_CSV = ROOT / f"startup_internship_scrape_{TODAY}.csv"
OUT_MD = ROOT / f"startup_internship_scrape_{TODAY}.md"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
    "application/json;q=0.8,*/*;q=0.7",
    "Accept-Language": "en-US,en;q=0.8",
}
TIMEOUT = 20

INTERNSHIP_RE = re.compile(
    r"\b(internship|intern(?!al)\b|co[- ]?op\b|coop\b|working student|"
    r"student intern|apprentice)\b",
    re.I,
)
BAD_TITLE_RE = re.compile(r"\b(internal|international)\b", re.I)

STARTUP_HEAVY_HOST_FRAGMENTS = (
    "ycombinator.com",
    "workatastartup.com",
    "wellfound.com",
    "angel.co",
    "jobs.ashbyhq.com",
    "job-boards.greenhouse.io",
    "boards.greenhouse.io",
    "job-boards.eu.greenhouse.io",
    "jobs.lever.co",
    "apply.workable.com",
    "breezy.hr",
    "rippling-ats.com",
    "jobs.polymer.co",
)

GITHUB_LISTING_SOURCES = [
    (
        "SimplifyJobs Summer2026",
        "https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/dev/.github/scripts/listings.json",
        "https://github.com/SimplifyJobs/Summer2026-Internships",
    ),
    (
        "PittCSC Summer2026",
        "https://raw.githubusercontent.com/pittcsc/Summer2026-Internships/dev/.github/scripts/listings.json",
        "https://github.com/pittcsc/Summer2026-Internships",
    ),
]

LOCAL_SEED_FILES = [
    ROOT / "internship_opportunities_2026-05-13.md",
    ROOT / "internship_opportunities_last_30_days_2026-05-13.md",
    ROOT / "internship_tracker_2026_05_27_opportunities.csv",
    ROOT / "unapplied_jobs_draft_2026_05_26.md",
]


@dataclass(frozen=True)
class BoardSeed:
    kind: str
    token: str
    source: str


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_url(url: str) -> str:
    url = clean_text(url)
    if not url:
        return ""
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), "", ""))


def is_internship_title(title: str) -> bool:
    title = clean_text(title)
    if not title:
        return False
    return bool(INTERNSHIP_RE.search(title)) and not bool(BAD_TITLE_RE.search(title))


def is_startup_heavy_url(url: str) -> bool:
    host = urlsplit(url).netloc.lower()
    return any(fragment in host for fragment in STARTUP_HEAVY_HOST_FRAGMENTS)


def get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(HEADERS)
    return session


def get_json(session: requests.Session, url: str) -> Any:
    resp = session.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def get_text(session: requests.Session, url: str) -> str:
    resp = session.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.text


def make_row(
    *,
    source: str,
    company: str,
    role: str,
    apply_url: str,
    source_url: str,
    location: str = "",
    job_type: str = "",
    category: str = "",
    term: str = "",
    salary: str = "",
    sponsorship: str = "",
    last_seen_signal: str = "",
    board: str = "",
    board_token: str = "",
    startup_signal: str = "",
    notes: str = "",
) -> dict[str, str]:
    return {
        "source": clean_text(source),
        "company": clean_text(company),
        "role": clean_text(role),
        "location": clean_text(location),
        "job_type": clean_text(job_type),
        "category": clean_text(category),
        "term": clean_text(term),
        "salary": clean_text(salary),
        "sponsorship": clean_text(sponsorship),
        "last_seen_signal": clean_text(last_seen_signal),
        "apply_url": clean_text(apply_url),
        "source_url": clean_text(source_url),
        "board": clean_text(board),
        "board_token": clean_text(board_token),
        "startup_signal": clean_text(startup_signal),
        "notes": clean_text(notes),
    }


def extract_board_seed(url: str, source: str) -> BoardSeed | None:
    parts = urlsplit(url)
    host = parts.netloc.lower()
    path = [part for part in parts.path.split("/") if part]
    if not path:
        return None
    if "greenhouse.io" in host:
        token = path[0]
        if token and token not in {"jobs", "embed"}:
            return BoardSeed("greenhouse", token, source)
    if host == "jobs.ashbyhq.com":
        return BoardSeed("ashby", path[0], source)
    if host == "jobs.lever.co":
        return BoardSeed("lever", path[0], source)
    return None


def parse_yc_internships(session: requests.Session) -> tuple[list[dict[str, str]], set[BoardSeed]]:
    source_url = "https://www.workatastartup.com/internships"
    rows: list[dict[str, str]] = []
    html_text = get_text(session, source_url)
    soup = BeautifulSoup(html_text, "html.parser")
    holder = soup.find(attrs={"data-page": True})
    if not holder:
        return rows, set()
    data = json.loads(html.unescape(holder["data-page"]))
    jobs = data.get("props", {}).get("jobPostings", [])
    for job in jobs:
        title = clean_text(job.get("title"))
        if job.get("type") != "Internship" and not is_internship_title(title):
            continue
        public_url = urljoin("https://www.ycombinator.com", job.get("url", ""))
        rows.append(
            make_row(
                source="YC Work at a Startup",
                company=job.get("companyName", ""),
                role=title,
                location=job.get("location", ""),
                job_type=job.get("type", ""),
                category=job.get("roleSpecificType", "") or job.get("prettyRole", ""),
                salary=job.get("salaryRange", ""),
                sponsorship=job.get("visa", ""),
                last_seen_signal=job.get("lastActive", "") or job.get("createdAt", ""),
                apply_url=public_url,
                source_url=source_url,
                board="YC",
                board_token=str(job.get("id", "")),
                startup_signal="YC startup",
                notes=job.get("companyOneLiner", ""),
            )
        )
    return rows, set()


def parse_github_listing_source(
    session: requests.Session, name: str, json_url: str, source_url: str
) -> tuple[list[dict[str, str]], set[BoardSeed]]:
    rows: list[dict[str, str]] = []
    board_seeds: set[BoardSeed] = set()
    data = get_json(session, json_url)
    for item in data:
        title = clean_text(item.get("title"))
        apply_url = clean_text(item.get("url"))
        if not item.get("active") or item.get("is_visible") is False:
            continue
        if not is_internship_title(title):
            continue
        if not is_startup_heavy_url(apply_url):
            continue
        seed = extract_board_seed(apply_url, name)
        if seed:
            board_seeds.add(seed)
        rows.append(
            make_row(
                source=name,
                company=item.get("company_name", ""),
                role=title,
                location="; ".join(item.get("locations", []) or []),
                category=item.get("category", ""),
                term="; ".join(item.get("terms", []) or []),
                sponsorship=item.get("sponsorship", ""),
                last_seen_signal=format_epoch(item.get("date_updated") or item.get("date_posted")),
                apply_url=apply_url,
                source_url=source_url,
                board=seed.kind if seed else urlsplit(apply_url).netloc,
                board_token=seed.token if seed else "",
                startup_signal="startup-heavy ATS/apply host",
                notes="Active listing in broad internship index; kept because apply host is startup-heavy.",
            )
        )
    return rows, board_seeds


def format_epoch(value: Any) -> str:
    if not value:
        return ""
    try:
        return datetime.fromtimestamp(int(value), tz=timezone.utc).date().isoformat()
    except Exception:
        return clean_text(value)


def parse_remoteok(session: requests.Session) -> tuple[list[dict[str, str]], set[BoardSeed]]:
    source_url = "https://remoteok.com/remote-internship-jobs"
    api_url = "https://remoteok.com/remote-internship-jobs.json"
    rows: list[dict[str, str]] = []
    data = get_json(session, api_url)
    for item in data:
        if "position" not in item:
            continue
        title = clean_text(item.get("position"))
        if not is_internship_title(title):
            continue
        rows.append(
            make_row(
                source="Remote OK",
                company=item.get("company", ""),
                role=title,
                location=item.get("location", "") or "Remote",
                category="; ".join(item.get("tags", []) or []),
                salary=format_salary(item.get("salary_min"), item.get("salary_max")),
                last_seen_signal=item.get("date", ""),
                apply_url=item.get("url", "") or item.get("apply_url", ""),
                source_url=source_url,
                board="Remote OK",
                startup_signal="remote job board",
                notes="Remote OK API requests attribution/link-back to source URL.",
            )
        )
    return rows, set()


def format_salary(min_salary: Any, max_salary: Any) -> str:
    try:
        lo = int(min_salary or 0)
        hi = int(max_salary or 0)
    except Exception:
        return ""
    if lo and hi:
        return f"{lo}-{hi}"
    if lo:
        return str(lo)
    if hi:
        return str(hi)
    return ""


def parse_nodesk(session: requests.Session) -> tuple[list[dict[str, str]], set[BoardSeed]]:
    source_url = "https://nodesk.co/remote-jobs/internship/"
    rows: list[dict[str, str]] = []
    html_text = get_text(session, source_url)
    soup = BeautifulSoup(html_text, "html.parser")
    seen: set[str] = set()
    for li in soup.find_all("li"):
        link = li.find("a", href=re.compile(r"^/remote-jobs/[^/]+/$"))
        if not link:
            continue
        title = clean_text(link.get_text(" ", strip=True))
        if not is_internship_title(title):
            continue
        apply_url = urljoin("https://nodesk.co", link.get("href", ""))
        if apply_url in seen:
            continue
        seen.add(apply_url)
        company_link = li.find("a", href=re.compile(r"^/remote-companies/"))
        company = clean_text(company_link.get_text(" ", strip=True)) if company_link else ""
        time_tag = li.find("time")
        rows.append(
            make_row(
                source="NoDesk",
                company=company,
                role=title,
                location="Remote",
                last_seen_signal=time_tag.get("datetime", "") if time_tag else "",
                apply_url=apply_url,
                source_url=source_url,
                board="NoDesk",
                startup_signal="remote job board",
            )
        )
    return rows, set()


def parse_remotive(session: requests.Session) -> tuple[list[dict[str, str]], set[BoardSeed]]:
    source_url = "https://remotive.com/remote-jobs"
    api_url = "https://remotive.com/api/remote-jobs?search=intern"
    rows: list[dict[str, str]] = []
    data = get_json(session, api_url)
    for item in data.get("jobs", []):
        title = clean_text(item.get("title"))
        if not is_internship_title(title):
            continue
        rows.append(
            make_row(
                source="Remotive",
                company=item.get("company_name", ""),
                role=title,
                location=item.get("candidate_required_location", "") or "Remote",
                category=item.get("category", ""),
                salary=item.get("salary", ""),
                last_seen_signal=item.get("publication_date", ""),
                apply_url=item.get("url", ""),
                source_url=source_url,
                board="Remotive",
                startup_signal="remote/startup job board",
            )
        )
    return rows, set()


def local_board_seeds() -> set[BoardSeed]:
    seeds: set[BoardSeed] = set()
    url_re = re.compile(r"https?://[^\s)>,|]+")
    for path in LOCAL_SEED_FILES:
        if not path.exists():
            continue
        for url in url_re.findall(path.read_text(errors="ignore")):
            seed = extract_board_seed(url, f"local:{path.name}")
            if seed:
                seeds.add(seed)
    return seeds


def fetch_board_jobs(session: requests.Session, seed: BoardSeed) -> list[dict[str, str]]:
    if seed.kind == "greenhouse":
        return fetch_greenhouse_jobs(session, seed)
    if seed.kind == "ashby":
        return fetch_ashby_jobs(session, seed)
    if seed.kind == "lever":
        return fetch_lever_jobs(session, seed)
    return []


def fetch_greenhouse_jobs(session: requests.Session, seed: BoardSeed) -> list[dict[str, str]]:
    api = f"https://boards-api.greenhouse.io/v1/boards/{seed.token}/jobs?content=true"
    source_url = f"https://job-boards.greenhouse.io/{seed.token}"
    rows: list[dict[str, str]] = []
    data = get_json(session, api)
    for job in data.get("jobs", []):
        title = clean_text(job.get("title"))
        if not is_internship_title(title):
            continue
        location = ""
        if isinstance(job.get("location"), dict):
            location = job["location"].get("name", "")
        dept = ""
        if isinstance(job.get("departments"), list):
            dept = "; ".join(clean_text(d.get("name")) for d in job["departments"] if d.get("name"))
        rows.append(
            make_row(
                source="Official Greenhouse board",
                company=seed.token,
                role=title,
                location=location,
                category=dept,
                last_seen_signal=job.get("updated_at", "") or job.get("published_at", ""),
                apply_url=job.get("absolute_url", ""),
                source_url=source_url,
                board=seed.kind,
                board_token=seed.token,
                startup_signal=f"seeded by {seed.source}",
                notes="Live official ATS scrape.",
            )
        )
    return rows


def fetch_ashby_jobs(session: requests.Session, seed: BoardSeed) -> list[dict[str, str]]:
    api = f"https://api.ashbyhq.com/posting-api/job-board/{seed.token}"
    source_url = f"https://jobs.ashbyhq.com/{seed.token}"
    rows: list[dict[str, str]] = []
    data = get_json(session, api)
    for job in data.get("jobs", []):
        title = clean_text(job.get("title"))
        if not is_internship_title(title):
            continue
        rows.append(
            make_row(
                source="Official Ashby board",
                company=seed.token,
                role=title,
                location=job.get("locationName", ""),
                job_type=job.get("employmentType", ""),
                category=job.get("departmentName", ""),
                last_seen_signal=job.get("publishedAt", ""),
                apply_url=job.get("jobUrl", "") or job.get("externalLink", ""),
                source_url=source_url,
                board=seed.kind,
                board_token=seed.token,
                startup_signal=f"seeded by {seed.source}",
                notes="Live official ATS scrape.",
            )
        )
    return rows


def fetch_lever_jobs(session: requests.Session, seed: BoardSeed) -> list[dict[str, str]]:
    api = f"https://api.lever.co/v0/postings/{seed.token}?mode=json"
    source_url = f"https://jobs.lever.co/{seed.token}"
    rows: list[dict[str, str]] = []
    data = get_json(session, api)
    for job in data:
        title = clean_text(job.get("text"))
        if not is_internship_title(title):
            continue
        categories = job.get("categories") or {}
        rows.append(
            make_row(
                source="Official Lever board",
                company=seed.token,
                role=title,
                location=categories.get("location", ""),
                job_type=categories.get("commitment", ""),
                category=categories.get("team", ""),
                last_seen_signal=format_epoch(job.get("createdAt")),
                apply_url=job.get("hostedUrl", "") or job.get("applyUrl", ""),
                source_url=source_url,
                board=seed.kind,
                board_token=seed.token,
                startup_signal=f"seeded by {seed.source}",
                notes="Live official ATS scrape.",
            )
        )
    return rows


def merge_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    fieldnames = output_fieldnames()
    for row in rows:
        key = normalize_url(row.get("apply_url", ""))
        if not key:
            key = "|".join(
                clean_text(row.get(field, "")).lower()
                for field in ("company", "role", "location")
            )
        if key not in merged:
            merged[key] = row.copy()
            continue
        existing = merged[key]
        for field in fieldnames:
            value = row.get(field, "")
            if not value:
                continue
            if not existing.get(field):
                existing[field] = value
            elif field in {"source", "source_url", "startup_signal", "notes"}:
                parts = [p.strip() for p in existing[field].split(";") if p.strip()]
                if value not in parts:
                    parts.append(value)
                existing[field] = "; ".join(parts)
    return sorted(
        merged.values(),
        key=lambda r: (
            source_rank(r.get("source", "")),
            r.get("company", "").lower(),
            r.get("role", "").lower(),
        ),
    )


def source_rank(source: str) -> int:
    if "YC Work" in source:
        return 0
    if "Official" in source:
        return 1
    if "Simplify" in source or "PittCSC" in source:
        return 2
    if "NoDesk" in source or "Remote OK" in source or "Remotive" in source:
        return 3
    return 9


def output_fieldnames() -> list[str]:
    return [
        "source",
        "company",
        "role",
        "location",
        "job_type",
        "category",
        "term",
        "salary",
        "sponsorship",
        "last_seen_signal",
        "apply_url",
        "source_url",
        "board",
        "board_token",
        "startup_signal",
        "notes",
    ]


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fieldnames())
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(
    rows: list[dict[str, str]],
    source_counts: Counter[str],
    board_counts: Counter[str],
    skipped: list[str],
) -> None:
    top_rows = rows[:80]
    lines = [
        "# Startup Internship Scrape",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Rows after dedupe: {len(rows)}",
        "",
        "## Source counts",
        "",
    ]
    for source, count in source_counts.most_common():
        lines.append(f"- {source}: {count}")
    lines.extend(["", "## Board counts", ""])
    for board, count in board_counts.most_common():
        lines.append(f"- {board or 'unknown'}: {count}")
    lines.extend(["", "## Top rows", ""])
    lines.append("| Source | Company | Role | Location | Apply |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in top_rows:
        apply = row.get("apply_url", "")
        apply_cell = f"[link]({apply})" if apply else ""
        lines.append(
            "| "
            + " | ".join(
                [
                    md_cell(row.get("source", "")),
                    md_cell(row.get("company", "")),
                    md_cell(row.get("role", "")),
                    md_cell(row.get("location", "")),
                    apply_cell,
                ]
            )
            + " |"
        )
    lines.extend(["", "## Skipped or limited", ""])
    for item in skipped:
        lines.append(f"- {item}")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def md_cell(value: str) -> str:
    return clean_text(value).replace("|", "\\|")


def main() -> int:
    session = get_session()
    rows: list[dict[str, str]] = []
    board_seeds: set[BoardSeed] = set()
    skipped: list[str] = []

    source_fetchers = [
        ("YC Work at a Startup", lambda: parse_yc_internships(session)),
        ("Remote OK", lambda: parse_remoteok(session)),
        ("NoDesk", lambda: parse_nodesk(session)),
        ("Remotive", lambda: parse_remotive(session)),
    ]
    for name, fetcher in source_fetchers:
        try:
            source_rows, source_seeds = fetcher()
            rows.extend(source_rows)
            board_seeds.update(source_seeds)
            print(f"{name}: {len(source_rows)} rows")
        except Exception as exc:
            skipped.append(f"{name}: {type(exc).__name__}: {exc}")
            print(f"{name}: skipped ({type(exc).__name__})")

    for name, json_url, source_url in GITHUB_LISTING_SOURCES:
        try:
            source_rows, source_seeds = parse_github_listing_source(
                session, name, json_url, source_url
            )
            rows.extend(source_rows)
            board_seeds.update(source_seeds)
            print(f"{name}: {len(source_rows)} rows; {len(source_seeds)} board seeds")
        except Exception as exc:
            skipped.append(f"{name}: {type(exc).__name__}: {exc}")
            print(f"{name}: skipped ({type(exc).__name__})")

    local_seeds = local_board_seeds()
    board_seeds.update(local_seeds)
    print(f"Local files: {len(local_seeds)} board seeds")

    board_rows: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_map = {
            executor.submit(fetch_board_jobs, session, seed): seed for seed in sorted(board_seeds, key=lambda s: (s.kind, s.token))
        }
        for i, future in enumerate(as_completed(future_map), 1):
            seed = future_map[future]
            try:
                found = future.result()
                board_rows.extend(found)
            except Exception as exc:
                skipped.append(
                    f"{seed.kind}:{seed.token}: {type(exc).__name__}: {exc}"
                )
            if i % 50 == 0:
                print(f"ATS boards checked: {i}/{len(future_map)}")
    print(f"Official ATS boards: {len(board_rows)} internship rows")
    rows.extend(board_rows)

    skipped.extend(
        [
            "Wellfound: blocked by DataDome/JS challenge in this environment.",
            "startup.jobs: blocked by Cloudflare challenge in this environment.",
            "LinkedIn: not scraped because it requires login and blocks automated access.",
            "Himalayas: dynamic Next.js page; left out to avoid noisy non-startup remote listings.",
        ]
    )

    merged = merge_rows(rows)
    source_counts = Counter(row["source"].split(";")[0] for row in merged)
    board_counts = Counter(row["board"] for row in merged)
    write_csv(merged)
    write_markdown(merged, source_counts, board_counts, skipped)
    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_MD}")
    print(f"Rows after dedupe: {len(merged)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
