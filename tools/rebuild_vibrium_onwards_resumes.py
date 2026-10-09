from __future__ import annotations

import importlib.util
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30"

BASE_PATH = ROOT / "tools" / "generate_early_startups_rest_materials.py"
SPEC = importlib.util.spec_from_file_location("base_resume_pack", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)


@dataclass(frozen=True)
class Project:
    title: str
    tech: str
    link: str
    bullets: tuple[str, ...]


@dataclass(frozen=True)
class ResumeTarget:
    attachment: str
    experience: str
    gsoc: str
    projects: tuple["ProjectRef", ...]
    skills: str


@dataclass(frozen=True)
class ProjectRef:
    key: str
    bullet_limit: int | None = None


def ref(key: str, bullet_limit: int | None = None) -> ProjectRef:
    return ProjectRef(key, bullet_limit)


def bodyhref(url: str, label: str = "GitHub") -> str:
    return BASE.bodyhref(url, label)


EXPERIENCE = {
    "backend": (
        r"Built \textbf{backend automation for legal/compliance filing workflows} with browser execution, public-site API lookups, retries, \textbf{session recovery}, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Modeled generated drafts, API responses, screenshots, form state, and failure checkpoints as \textbf{recoverable workflow records} so broken external-system steps could be inspected and re-run safely.",
        r"Implemented an \textbf{AI-assisted drafting flow} for company-name suggestions, object descriptions, and filing-field drafts while keeping generated outputs inspectable before deterministic backend execution.",
        r"Shipped Dockerized \textbf{Node.js/Go backend services} on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
    ),
    "platform": (
        r"Built backend automation around public-site API lookups, browser execution, retries, \textbf{session recovery}, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Structured API responses, screenshots, generated drafts, form state, and failure checkpoints as \textbf{debuggable workflow records} for unreliable external systems.",
        r"Containerized Node.js/Go services with \textbf{Docker}, deployed on \textbf{Google Cloud Run}, and wired \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
        r"Kept generated drafts and workflow outputs inspectable before final execution, matching regulated-product needs around traceability, review, and rollback.",
    ),
    "health": (
        r"Built backend automation for compliance-sensitive workflows with public-site API lookups, retries, \textbf{session recovery}, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Modeled generated drafts, API responses, screenshots, form state, and failure checkpoints as \textbf{reviewable workflow records} for human inspection before final execution.",
        r"Implemented inspectable draft generation so generated outputs could be checked before deterministic backend execution.",
        r"Shipped Dockerized Node.js/Go services on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
    ),
    "finance": (
        r"Built backend automation for \textbf{compliance-sensitive workflows} with browser execution, public-site API lookups, retries, session recovery, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Modeled generated drafts, API responses, screenshots, form state, and failure checkpoints as \textbf{audit-friendly workflow records} for debugging and re-running external-system failures.",
        r"Implemented generated-draft review paths where output had to stay inspectable before deterministic filing execution.",
        r"Shipped Dockerized Node.js/Go backend services on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
    ),
}


GSOC = {
    "default": (
        r"Integrated \textbf{Python workflows} for \textbf{95 anatomical brain regions}, wiring preprocessing, PyTorch/TorchScript and ONNX/TinyGrad execution paths, generated artifacts, and correctness checks into Invesalius.",
        r"Built model-output inspection paths around generated masks, label remapping, orientation checks, progress reporting, and reproducible artifact debugging.",
        r"Reduced expensive processing runtime by \textbf{87\%} through async/parallel execution while debugging GPU/CPU paths, large data movement, and output correctness.",
    ),
    "data": (
        r"Integrated Python data-processing workflows for \textbf{95 anatomical brain regions}, wiring preprocessing, model execution, generated artifacts, progress reporting, and correctness checks into a mature application.",
        r"Debugged large data paths, generated outputs, label correctness, GPU/CPU behavior, and reproducible inspection flows across medical-imaging datasets.",
        r"Reduced processing runtime by \textbf{87\%} through async/parallel execution while keeping output correctness and reviewability intact.",
    ),
    "health": (
        r"Built \textbf{medical-imaging segmentation workflows} for \textbf{95 anatomical brain regions}, integrating preprocessing, PyTorch/TorchScript and ONNX/TinyGrad inference, generated masks, and 3D inspection paths.",
        r"Worked with NIfTI/MGZ MRI data, voxel conformation, thick-slice datasets, sagittal label remapping, LUT mapping, binary masks, and quick QC/debugging checks.",
        r"Reduced expensive MRI-processing runtime by \textbf{87\%} through async/parallel execution while debugging orientation, label correctness, GPU/CPU paths, and reproducible output inspection.",
    ),
}


PROJECTS = {
    "hyoka_agent": Project(
        "Hyoka Agent Reliability Layer",
        "Python, FastAPI, SQLAlchemy, PostgreSQL, OpenTelemetry",
        bodyhref("https://github.com/unichronic/hyoka"),
        (
            r"Built a pluggable \textbf{agent reliability and self-improvement layer} that captures traces, evaluates behavior, mines failures, replays candidates, and promotes safer configs through release gates.",
            r"Implemented authenticated trace/event ingestion, suites, candidates, runs, gate decisions, promotions, API keys, audit logs, artifacts, and manifests on \textbf{FastAPI + SQLAlchemy/Alembic}.",
            r"Added OTLP/OpenInference-style ingestion, an OpenAI-compatible proxy, Python SDK hooks, Typer CLI workflows, and a Next.js dashboard for trace/run/gate inspection.",
        ),
    ),
    "hyoka_platform": Project(
        "Hyoka Agent Reliability Layer",
        "Python, FastAPI, SQLAlchemy, PostgreSQL, OpenTelemetry",
        bodyhref("https://github.com/unichronic/hyoka"),
        (
            r"Built the production core for an \textbf{agent reliability layer}: trace ingestion, eval/replay runs, failure mining, candidate generation, gate decisions, promotions, artifacts, manifests, and audit logs.",
            r"Designed \textbf{SQLite/PostgreSQL metadata models} for traces, suites, candidates, runs, artifacts, manifests, worker leases, gate decisions, and promotions using SQLAlchemy/Alembic.",
            r"Implemented database-backed worker leases, content-addressed artifacts, HMAC-signed manifests, API-key isolation, and Docker Compose services for server, worker, proxy, dashboard, and Postgres.",
        ),
    ),
    "hyoka_audit": Project(
        "Hyoka Agent Reliability Layer",
        "Python, FastAPI, SQLAlchemy, PostgreSQL, OpenTelemetry",
        bodyhref("https://github.com/unichronic/hyoka"),
        (
            r"Built trace/evaluation infrastructure for existing AI agents with canonical trace ingestion, validation runs, gate decisions, audit logs, project-scoped API keys, and replayable workflow records.",
            r"Stored artifacts, manifests, candidates, evaluation results, and promotion metadata in \textbf{SQLite/PostgreSQL} so agent behavior changes could be inspected and reproduced.",
        ),
    ),
    "postificus_ops": Project(
        "Postificus Content Distribution Engine",
        "Go, Echo, React, PostgreSQL, Redis/RabbitMQ, Go-Rod",
        bodyhref("https://github.com/unichronic/postificus"),
        (
            r"Built a centralized \textbf{content distribution engine} for writing once and publishing technical posts across Medium, Dev.to, and LinkedIn while preserving canonical URL/SEO ownership.",
            r"Split the Go/Echo backend into API and worker paths, using PostgreSQL persistence, Redis caching, RabbitMQ queues with retry/DLQ handling, and Prometheus metrics.",
            r"Implemented direct platform API flows where available and \textbf{Go-Rod browser automation} as fallback for platforms without reliable write APIs.",
        ),
    ),
    "postificus_content": Project(
        "Postificus Content Distribution Engine",
        "Go, Echo, React, PostgreSQL, Redis/RabbitMQ, Go-Rod",
        bodyhref("https://github.com/unichronic/postificus"),
        (
            r"Built a technical-blogging \textbf{content distribution engine} with a React/Vite/Tiptap editor, platform connection management, and publishing flows for Medium, Dev.to, and LinkedIn.",
            r"Implemented Go/Echo REST APIs, PostgreSQL persistence, Redis caching, RabbitMQ job queues, Supabase/S3-compatible storage, and live publish/activity status surfaces.",
            r"Combined direct APIs with \textbf{Go-Rod browser fallback} for fragmented publishing surfaces, including retry/DLQ handling and Prometheus instrumentation around worker jobs.",
        ),
    ),
    "swish_ops": Project(
        "Swish Food-Delivery Support Automation",
        "Python, FastAPI, React, PostgreSQL, Redis, Langfuse",
        bodyhref("https://github.com/unichronic/swishagent"),
        (
            r"Built \textbf{customer-support automation for Swish food delivery} with FastAPI services, Postgres/Redis infrastructure, and a React/Vite UI for testing support flows.",
            r"Modeled complaints using order, kitchen, fleet, trust, fraud/evidence, issue signals, and conversation state while deterministic policy code controlled coupons, refunds, replacements, and escalations.",
            r"Added Langfuse/local JSON tracing, optional Hyoka trace export, pytest regression suites, response-quality checks, and session state so support behavior stayed reviewable across follow-ups.",
        ),
    ),
    "swish_care": Project(
        "Swish Food-Delivery Support Automation",
        "Python, FastAPI, React, PostgreSQL, Redis, Langfuse",
        bodyhref("https://github.com/unichronic/swishagent"),
        (
            r"Built support automation for food-delivery complaints with FastAPI services for agent, data, order, kitchen, fleet, trust, fraud, and public API gateway paths.",
            r"Kept final compensation actions policy-bound while AI helped classify messy customer language, affected items, evidence relevance, desired resolution, and reply tone.",
        ),
    ),
    "seaweed_backend": Project(
        "Seaweed Contest Platform",
        "Go, Next.js, PostgreSQL, Firebase Auth, S3, Judge0",
        bodyhref("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built a \textbf{coding contest platform} for live rounds, problem publishing, Firebase-authenticated registrations, submissions, admin controls, and public leaderboards.",
            r"Implemented Go/Echo APIs over PostgreSQL for contests, problems, submissions, test-case results, rankings, admin flags, and materialized leaderboard refreshes.",
            r"Integrated Judge0 judging, S3 submission storage, Next.js problem/leaderboard/admin pages, and score/attempt aggregation for \textbf{500+ concurrent users}.",
        ),
    ),
    "seaweed_short": Project(
        "Seaweed Contest Platform",
        "Go, Next.js, PostgreSQL, Firebase Auth, S3, Judge0",
        bodyhref("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built backend flows for contest listings, registrations, problem access, code submissions, Judge0 status polling, admin review, and live leaderboard views.",
            r"Used Go/Echo, PostgreSQL, Firebase Auth, S3 submission storage, and Docker deployment paths to support live contest traffic for \textbf{500+ concurrent users}.",
        ),
    ),
    "penny_finance": Project(
        "Penny Lane Capital",
        "Python, Agno, Pydantic, SQLite, yfinance, JSONL",
        bodyhref("https://github.com/unichronic/pennylane"),
        (
            r"Built \textbf{multi-agent trading research software} that runs OHLCV data through analyst reports, bull/bear debate, research manager, trader, risk debate, portfolio approval, and paper evaluation.",
            r"Used Agno Workflow, typed Pydantic state, SQLite checkpoints, JSONL/full-state traces, yfinance market data, optional vector memory, and a React/Vite inspection UI.",
            r"Added paper-style walk-forward backtests, baseline strategies, validation harnesses, no-silent-fallback tests, and reward-loop scorecards for research evaluation.",
        ),
    ),
}


SKILLS = {
    "backend": r"""\textbf{Languages}{: Go, Python, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, Echo, Gin, SQLAlchemy} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, GCP Cloud Run, GitHub Actions, Prometheus, OpenTelemetry, REST APIs} \\""",
    "ai_backend": r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, SQLAlchemy, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, GCP Cloud Run, GitHub Actions, OpenTelemetry, Prometheus, Langfuse, ONNX, REST APIs} \\""",
    "platform": r"""\textbf{Languages}{: Go, Python, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Echo, Gin, SQLAlchemy} \\
   \textbf{Tools}{: Docker, Kubernetes, GCP Cloud Run, GitHub Actions, PostgreSQL, Redis, RabbitMQ, Prometheus, OpenTelemetry, REST APIs} \\""",
    "finance": r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, Echo, SQLAlchemy, Pydantic} \\
   \textbf{Tools}{: PostgreSQL, SQLite, Redis, RabbitMQ, Docker, GCP Cloud Run, GitHub Actions, Prometheus, OpenTelemetry, REST APIs, JSONL} \\""",
    "health": r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, React, Next.js, Node.js, SQLAlchemy, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, OpenTelemetry, Prometheus, Langfuse, GitHub Actions, ONNX, REST APIs} \\""",
}


TARGETS = {
    "vibrium": ResumeTarget(
        "vibrium_ai_backend_intern_resume.pdf",
        "backend",
        "default",
        (ref("hyoka_agent"), ref("swish_ops"), ref("postificus_ops")),
        SKILLS["ai_backend"],
    ),
    "ateli": ResumeTarget(
        "ateli_backend_intern_resume.pdf",
        "backend",
        "data",
        (ref("postificus_content"), ref("swish_ops", 2), ref("seaweed_backend", 2), ref("hyoka_audit")),
        SKILLS["backend"],
    ),
    "kluisz_ai": ResumeTarget(
        "kluisz_ai_platform_intern_resume.pdf",
        "platform",
        "default",
        (ref("postificus_ops"), ref("hyoka_platform"), ref("seaweed_backend")),
        SKILLS["platform"],
    ),
    "stch": ResumeTarget(
        "stch_backend_product_intern_resume.pdf",
        "backend",
        "data",
        (ref("hyoka_agent"), ref("postificus_ops"), ref("swish_ops", 2), ref("seaweed_short", 1)),
        SKILLS["ai_backend"],
    ),
    "grevoro": ResumeTarget(
        "grevoro_backend_data_intern_resume.pdf",
        "platform",
        "data",
        (ref("postificus_ops"), ref("hyoka_platform"), ref("seaweed_short", 1), ref("swish_care", 1)),
        SKILLS["backend"],
    ),
    "pred": ResumeTarget(
        "pred_backend_systems_intern_resume.pdf",
        "finance",
        "data",
        (ref("seaweed_backend", 2), ref("postificus_ops", 2), ref("penny_finance"), ref("hyoka_audit")),
        SKILLS["finance"],
    ),
    "aamra_seniors_club": ResumeTarget(
        "aamra_seniors_club_backend_ops_intern_resume.pdf",
        "health",
        "health",
        (ref("swish_ops"), ref("seaweed_short", 1), ref("hyoka_audit"), ref("postificus_ops", 2)),
        SKILLS["health"],
    ),
    "puresta": ResumeTarget(
        "puresta_ml_backend_intern_resume.pdf",
        "health",
        "health",
        (ref("hyoka_agent"), ref("swish_care"), ref("postificus_ops", 2), ref("seaweed_short", 1)),
        SKILLS["health"],
    ),
    "frex": ResumeTarget(
        "frex_fintech_backend_intern_resume.pdf",
        "finance",
        "data",
        (ref("hyoka_platform"), ref("postificus_ops"), ref("penny_finance")),
        SKILLS["finance"],
    ),
    "ilios_72": ResumeTarget(
        "ilios_72_fintech_data_intern_resume.pdf",
        "finance",
        "data",
        (ref("penny_finance"), ref("hyoka_platform"), ref("postificus_ops", 2), ref("seaweed_short", 1)),
        SKILLS["finance"],
    ),
}


def project_latex(project_ref: ProjectRef) -> str:
    key = project_ref.key
    project = PROJECTS[key]
    selected_bullets = project.bullets
    if project_ref.bullet_limit is not None:
        selected_bullets = selected_bullets[: project_ref.bullet_limit]
    bullets = "\n".join(rf"\resumeItem{{{bullet}}}" for bullet in selected_bullets)
    return rf"""\resumeProjectHeading
{{\textbf{{{project.title}}} $|$ \emph{{{project.tech}}}}}{{{project.link}}}
\resumeItemListStart
{bullets}
\resumeItemListEnd"""


def build_tex(target: ResumeTarget) -> str:
    # Keep the same resume skeleton used by the corrected resumes, but use denser
    # content so this batch does not look underfilled.
    template = (
        BASE.LATEX_TEMPLATE
        .replace(r"\addtolength{\topmargin}{-.98in}", r"\addtolength{\topmargin}{-1.08in}")
        .replace(r"\addtolength{\textheight}{2.08in}", r"\addtolength{\textheight}{2.32in}")
        .replace(r"\fontsize{9.05pt}{9.75pt}", r"\fontsize{8.82pt}{9.28pt}")
        .replace(r"\fontsize{9.6pt}{10.0pt}", r"\fontsize{9.0pt}{9.25pt}")
    )
    return (
        template
        .replace("%BENTHAM_BULLETS%", "\n".join(rf"\resumeItem{{{bullet}}}" for bullet in EXPERIENCE[target.experience]))
        .replace("%GSOC_BULLETS%", "\n".join(rf"\resumeItem{{{bullet}}}" for bullet in GSOC[target.gsoc]))
        .replace("%PROJECTS%", "\n".join(project_latex(project_ref) for project_ref in target.projects))
        .replace("%SKILLS%", target.skills)
    )


def compile_pdf(tex_path: Path) -> None:
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", tex_path.name],
        cwd=tex_path.parent,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main() -> None:
    for slug, target in TARGETS.items():
        tex_path = OUT_DIR / target.attachment.replace(".pdf", ".tex")
        tex_path.write_text(build_tex(target), encoding="utf-8")
        compile_pdf(tex_path)
        print(f"rebuilt {slug}: {target.attachment}")


if __name__ == "__main__":
    main()
