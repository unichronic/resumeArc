#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KEY_FILE = Path.home() / ".config" / "intern-outreach" / "keys.env"


def load_env_files() -> None:
    candidates = [
        Path(os.environ.get("OUTREACH_KEYS_FILE", DEFAULT_KEY_FILE)),
        REPO_ROOT / ".env",
    ]
    seen: set[Path] = set()
    for path in candidates:
        path = path.expanduser()
        if path in seen or not path.exists():
            continue
        seen.add(path)
        for raw_line in path.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


load_env_files()

mcp = FastMCP(
    "intern-outreach",
    instructions=(
        "Credit-aware internship outreach tools. Use public/provided names and domains, "
        "verify before sending, avoid scraping logged-in sites, and do not bulk-send mail."
    ),
)


def secret(name: str) -> str | None:
    value = os.environ.get(name)
    return value if value else None


def api_result(response: httpx.Response) -> dict[str, Any]:
    try:
        data: Any = response.json()
    except Exception:
        data = response.text[:2000]
    return {
        "ok": response.is_success,
        "status_code": response.status_code,
        "data": data,
    }


def request_json(method: str, url: str, **kwargs: Any) -> dict[str, Any]:
    try:
        with httpx.Client(timeout=45.0, follow_redirects=True) as client:
            response = client.request(method, url, **kwargs)
        return api_result(response)
    except httpx.HTTPError as exc:
        return {"ok": False, "error": str(exc)}


def normalize_domain(domain: str) -> str:
    domain = domain.strip().lower()
    domain = re.sub(r"^https?://", "", domain)
    domain = domain.split("/", 1)[0]
    return domain.removeprefix("www.")


def name_token(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", value.lower())


def split_name(full_name: str) -> tuple[str, str]:
    parts = [name_token(part) for part in full_name.split() if name_token(part)]
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[-1]


def email_guesses(first_name: str, last_name: str, domain: str) -> list[dict[str, Any]]:
    first = name_token(first_name)
    last = name_token(last_name)
    domain = normalize_domain(domain)
    if not first or not last or not domain:
        return []
    first_initial = first[0]
    last_initial = last[0]
    patterns = [
        ("first.last", f"{first}.{last}@{domain}", 1),
        ("first", f"{first}@{domain}", 2),
        ("firstlast", f"{first}{last}@{domain}", 3),
        ("flast", f"{first_initial}{last}@{domain}", 4),
        ("firstl", f"{first}{last_initial}@{domain}", 5),
        ("first_last", f"{first}_{last}@{domain}", 6),
        ("last.first", f"{last}.{first}@{domain}", 7),
        ("last", f"{last}@{domain}", 8),
    ]
    seen: set[str] = set()
    guesses: list[dict[str, Any]] = []
    for pattern, email, priority in patterns:
        if email in seen:
            continue
        seen.add(email)
        guesses.append({"email": email, "pattern": pattern, "priority": priority})
    return guesses


def role_score(role: str) -> dict[str, Any]:
    value = role.lower()
    score = 0
    reasons: list[str] = []
    groups = [
        (35, ("founder", "co-founder", "cto", "chief technology"), "founder/technical executive"),
        (28, ("engineering manager", "head of engineering", "director of engineering", "vp engineering"), "engineering leadership"),
        (24, ("recruiter", "talent", "people", "hr"), "recruiting route"),
        (18, ("staff engineer", "principal engineer", "tech lead", "lead engineer"), "senior engineering IC"),
        (10, ("software engineer", "backend", "platform", "infrastructure", "ml engineer"), "technical staff"),
    ]
    for points, needles, reason in groups:
        if any(needle in value for needle in needles):
            score += points
            reasons.append(reason)
    if not reasons:
        reasons.append("no strong internship-routing signal")
    return {"score": score, "reasons": reasons}


@mcp.tool()
def available_connections() -> dict[str, Any]:
    """Show which outreach API keys are configured without revealing them."""
    return {
        "key_file": str(Path(os.environ.get("OUTREACH_KEYS_FILE", DEFAULT_KEY_FILE)).expanduser()),
        "hunter": bool(secret("HUNTER_API_KEY")),
        "prospeo": bool(secret("PROSPEO_API_KEY")),
        "reoon": bool(secret("REOON_API_KEY")),
        "recommended_order": [
            "Generate likely email patterns without credits.",
            "Use Reoon power verification for guessed emails.",
            "Use Hunter or Prospeo credits only for high-value staff.",
            "Send manually or create drafts; avoid bulk sending.",
        ],
    }


@mcp.tool()
def generate_email_guesses(first_name: str, last_name: str, domain: str) -> dict[str, Any]:
    """Generate likely work-email patterns for a person and company domain."""
    guesses = email_guesses(first_name, last_name, domain)
    return {
        "input": {"first_name": first_name, "last_name": last_name, "domain": normalize_domain(domain)},
        "guesses": guesses,
        "credit_cost": 0,
    }


@mcp.tool()
def score_outreach_role(role: str) -> dict[str, Any]:
    """Score a staff role for internship cold outreach routing priority."""
    result = role_score(role)
    result["role"] = role
    return result


@mcp.tool()
def reoon_check_balance() -> dict[str, Any]:
    """Check Reoon remaining credits."""
    key = secret("REOON_API_KEY")
    if not key:
        return {"ok": False, "error": "REOON_API_KEY is not configured"}
    return request_json(
        "GET",
        "https://emailverifier.reoon.com/api/v1/check-account-balance/",
        params={"key": key},
    )


@mcp.tool()
def reoon_verify_email(email: str, mode: str = "power") -> dict[str, Any]:
    """Verify one email with Reoon. Use power for cold outreach accuracy."""
    key = secret("REOON_API_KEY")
    if not key:
        return {"ok": False, "error": "REOON_API_KEY is not configured"}
    if mode not in {"quick", "power"}:
        return {"ok": False, "error": "mode must be quick or power"}
    return request_json(
        "GET",
        "https://emailverifier.reoon.com/api/v1/verify",
        params={"email": email, "key": key, "mode": mode},
    )


@mcp.tool()
def hunter_account() -> dict[str, Any]:
    """Check Hunter account and usage."""
    key = secret("HUNTER_API_KEY")
    if not key:
        return {"ok": False, "error": "HUNTER_API_KEY is not configured"}
    return request_json("GET", "https://api.hunter.io/v2/account", params={"api_key": key})


@mcp.tool()
def hunter_find_email(first_name: str, last_name: str, domain: str) -> dict[str, Any]:
    """Use Hunter credits to find a likely professional email."""
    key = secret("HUNTER_API_KEY")
    if not key:
        return {"ok": False, "error": "HUNTER_API_KEY is not configured"}
    return request_json(
        "GET",
        "https://api.hunter.io/v2/email-finder",
        params={
            "first_name": first_name,
            "last_name": last_name,
            "domain": normalize_domain(domain),
            "api_key": key,
        },
    )


@mcp.tool()
def hunter_verify_email(email: str) -> dict[str, Any]:
    """Verify one email with Hunter."""
    key = secret("HUNTER_API_KEY")
    if not key:
        return {"ok": False, "error": "HUNTER_API_KEY is not configured"}
    return request_json(
        "GET",
        "https://api.hunter.io/v2/email-verifier",
        params={"email": email, "api_key": key},
    )


@mcp.tool()
def hunter_domain_search(domain: str, limit: int = 10) -> dict[str, Any]:
    """Find public emails known for a domain with Hunter. Keep limit low to conserve credits."""
    key = secret("HUNTER_API_KEY")
    if not key:
        return {"ok": False, "error": "HUNTER_API_KEY is not configured"}
    bounded_limit = max(1, min(int(limit), 25))
    return request_json(
        "GET",
        "https://api.hunter.io/v2/domain-search",
        params={"domain": normalize_domain(domain), "limit": bounded_limit, "api_key": key},
    )


@mcp.tool()
def prospeo_account_information() -> dict[str, Any]:
    """Check Prospeo current plan and remaining credits."""
    key = secret("PROSPEO_API_KEY")
    if not key:
        return {"ok": False, "error": "PROSPEO_API_KEY is not configured"}
    return request_json(
        "GET",
        "https://api.prospeo.io/account-information",
        headers={"X-KEY": key},
    )


@mcp.tool()
def prospeo_enrich_person(
    first_name: str = "",
    last_name: str = "",
    full_name: str = "",
    company_website: str = "",
    company_name: str = "",
    linkedin_url: str = "",
    only_verified_email: bool = True,
) -> dict[str, Any]:
    """Use Prospeo credits to enrich one person. Defaults to verified-email-only."""
    key = secret("PROSPEO_API_KEY")
    if not key:
        return {"ok": False, "error": "PROSPEO_API_KEY is not configured"}

    data: dict[str, Any] = {}
    if full_name:
        data["full_name"] = full_name
    elif first_name and last_name:
        data["first_name"] = first_name
        data["last_name"] = last_name
    if company_website:
        data["company_website"] = normalize_domain(company_website)
    if company_name:
        data["company_name"] = company_name
    if linkedin_url:
        data["linkedin_url"] = linkedin_url

    has_name_company = (
        (data.get("full_name") or (data.get("first_name") and data.get("last_name")))
        and (data.get("company_website") or data.get("company_name"))
    )
    if not (has_name_company or data.get("linkedin_url")):
        return {
            "ok": False,
            "error": "Need first+last/full name plus company_website/company_name, or linkedin_url.",
        }

    return request_json(
        "POST",
        "https://api.prospeo.io/enrich-person",
        headers={"X-KEY": key, "Content-Type": "application/json"},
        json={"only_verified_email": only_verified_email, "data": data},
    )


@mcp.tool()
def prepare_candidates_from_csv(
    csv_path: str,
    output_path: str = "",
    verify_with: str = "none",
    max_rows: int = 25,
) -> dict[str, Any]:
    """Generate guesses from CSV. Columns: first_name,last_name,domain,role."""
    path = Path(csv_path).expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    if not path.exists():
        return {"ok": False, "error": f"CSV not found: {path}"}
    if verify_with not in {"none", "reoon", "hunter"}:
        return {"ok": False, "error": "verify_with must be none, reoon, or hunter"}

    rows: list[dict[str, Any]] = []
    with path.open(newline="") as handle:
        for idx, row in enumerate(csv.DictReader(handle), start=1):
            if idx > max_rows:
                break
            first = row.get("first_name", "")
            last = row.get("last_name", "")
            domain = row.get("domain", "")
            guesses = email_guesses(first, last, domain)
            verification: dict[str, Any] | None = None
            if guesses and verify_with == "reoon":
                verification = reoon_verify_email(guesses[0]["email"], "power")
            elif guesses and verify_with == "hunter":
                verification = hunter_verify_email(guesses[0]["email"])
            scored = role_score(row.get("role", ""))
            rows.append(
                {
                    **row,
                    "domain": normalize_domain(domain),
                    "role_score": scored["score"],
                    "role_reasons": "; ".join(scored["reasons"]),
                    "guesses": guesses,
                    "first_guess": guesses[0]["email"] if guesses else "",
                    "verification": verification,
                }
            )

    if output_path:
        out = Path(output_path).expanduser()
        if not out.is_absolute():
            out = REPO_ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = [
            "first_name",
            "last_name",
            "company",
            "domain",
            "role",
            "linkedin_url",
            "first_guess",
            "role_score",
            "role_reasons",
            "all_guesses",
            "verification_status",
        ]
        with out.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                verification = row.get("verification") or {}
                data = verification.get("data", {}) if isinstance(verification, dict) else {}
                writer.writerow(
                    {
                        "first_name": row.get("first_name", ""),
                        "last_name": row.get("last_name", ""),
                        "company": row.get("company", ""),
                        "domain": row.get("domain", ""),
                        "role": row.get("role", ""),
                        "linkedin_url": row.get("linkedin_url", ""),
                        "first_guess": row.get("first_guess", ""),
                        "role_score": row.get("role_score", ""),
                        "role_reasons": row.get("role_reasons", ""),
                        "all_guesses": ";".join(g["email"] for g in row.get("guesses", [])),
                        "verification_status": data.get("status", ""),
                    }
                )
        return {"ok": True, "count": len(rows), "output_path": str(out), "rows": rows}

    return {"ok": True, "count": len(rows), "rows": rows}


def print_json(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description="Internship outreach MCP and CLI helpers")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("connections")

    guess = sub.add_parser("guess")
    guess.add_argument("--first-name", required=True)
    guess.add_argument("--last-name", required=True)
    guess.add_argument("--domain", required=True)

    verify = sub.add_parser("verify")
    verify.add_argument("--email", required=True)
    verify.add_argument("--provider", choices=("reoon", "hunter"), default="reoon")
    verify.add_argument("--mode", choices=("quick", "power"), default="power")

    prepare = sub.add_parser("prepare-csv")
    prepare.add_argument("--input", required=True)
    prepare.add_argument("--output", default="")
    prepare.add_argument("--verify-with", choices=("none", "reoon", "hunter"), default="none")
    prepare.add_argument("--max-rows", type=int, default=25)

    args = parser.parse_args()
    if args.command == "connections":
        print_json(available_connections())
        return 0
    if args.command == "guess":
        print_json(generate_email_guesses(args.first_name, args.last_name, args.domain))
        return 0
    if args.command == "verify":
        if args.provider == "reoon":
            print_json(reoon_verify_email(args.email, args.mode))
        else:
            print_json(hunter_verify_email(args.email))
        return 0
    if args.command == "prepare-csv":
        print_json(prepare_candidates_from_csv(args.input, args.output, args.verify_with, args.max_rows))
        return 0
    if len(sys.argv) == 1:
        mcp.run()
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

