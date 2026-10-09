from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "sarvam_dubbing_backend_2026_06_03"
BASE_PATH = ROOT / "tools" / "generate_early_startups_rest_materials.py"

SPEC = importlib.util.spec_from_file_location("base_resume_pack", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)


def item(text: str) -> str:
    return rf"\resumeItem{{{text}}}"


def project(title: str, tech: str, link: str, bullets: tuple[str, ...]) -> str:
    bullet_lines = "\n".join(item(bullet) for bullet in bullets)
    return rf"""\resumeProjectHeading
{{\textbf{{{title}}} $|$ \emph{{{tech}}}}}{{{link}}}
\resumeItemListStart
{bullet_lines}
\resumeItemListEnd"""


def build_resume_tex() -> str:
    bentham = (
        r"Built \textbf{backend automation for legal/compliance workflows} at \bodyhref{https://www.bentham.legal/}{Bentham AI}, combining browser execution, public-site API lookups, retries, \textbf{session recovery}, validation checks, and operator checkpoints to reduce manual filing time by \textbf{85\%}.",
        r"Modeled screenshots, API responses, generated drafts, form state, and failures as \textbf{recoverable workflow records}, making ambiguous external-system failures easier to debug and re-run.",
        r"Implemented \textbf{AI-assisted drafting} while keeping generated outputs inspectable before deterministic execution, matching production workflows where model/provider output cannot be trusted blindly.",
        r"Shipped Dockerized \textbf{Node.js/Go backend services} on \textbf{Google Cloud Run} with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
    )
    gsoc = (
        r"Integrated Python model-output workflows for \textbf{95 anatomical brain regions}, wiring preprocessing, PyTorch/TorchScript, ONNX/TinyGrad paths, generated artifacts, and correctness checks into Invesalius.",
        r"Reduced expensive processing runtime by \textbf{87\%} using async/parallel execution while debugging GPU/CPU paths, large data movement, generated masks, and output correctness.",
    )
    projects = (
        project(
            "Swish Support Automation",
            "Python, FastAPI, PostgreSQL, Redis, Langfuse, pytest",
            BASE.bodyhref("https://github.com/unichronic/swishagent"),
            (
                r"Built \textbf{FastAPI support-agent services} with order, kitchen, fleet, trust, evidence, issue, and conversation context flowing through user-facing decisions.",
                r"Implemented \textbf{provider fallback and cooldown handling} for LLM calls, request timeouts, Gemini fallback paths, local JSON/Langfuse traces, and deterministic fallbacks when provider output was unreliable.",
                r"Added a live conversation-suite runner with request timeouts, retry-after handling, session clearing, pytest regressions, and response-quality checks for debugging multi-turn behavior.",
            ),
        ),
        project(
            "Hyoka Agent Reliability Layer",
            "Python, FastAPI, Pydantic, SQLAlchemy, PostgreSQL, OpenTelemetry",
            BASE.bodyhref("https://github.com/unichronic/hyoka"),
            (
                r"Built a \textbf{FastAPI agent reliability layer}: trace/event ingestion, eval/replay runs, failure mining, release gates, audit logs, project-scoped API keys, and worker leases.",
                r"Implemented an \textbf{OpenAI-compatible proxy}, OTLP/OpenInference-style ingestion, Python SDK hooks for LLM/tool/retrieval events, artifacts, manifests, and promotions.",
                r"Designed \textbf{typed metadata models} with SQLAlchemy/Alembic so agent behavior changes could be reproduced, compared, promoted, or rolled back safely.",
            ),
        ),
        project(
            "Postificus Content Distribution Engine",
            "Go, Echo, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
            BASE.bodyhref("https://github.com/unichronic/postificus"),
            (
                r"Built Go/Echo \textbf{REST APIs and worker services} with PostgreSQL persistence, Redis state/cache, RabbitMQ retry/DLQ jobs, Docker services, and Prometheus metrics.",
                r"Kept long-running external workflows recoverable with saved state, retries, health checks, browser fallback execution, worker metrics, and clear UI status around publish/sync activity.",
            ),
        ),
        project(
            "Penny Lane Multi-Agent Workflow",
            "Python, Agno, Pydantic, SQLite, JSONL, React/Vite",
            BASE.bodyhref("https://github.com/unichronic/pennylane"),
            (
                r"Built a \textbf{multi-agent workflow} with analyst, debate, manager, risk-review, portfolio-approval, and evaluation stages wired through typed Pydantic state.",
                r"Used SQLite checkpoints, JSONL/full-state traces, baseline comparisons, validation harnesses, and a React/Vite inspection UI to review pipeline outputs across runs.",
            ),
        ),
    )
    skills = r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Pydantic, SQLAlchemy, Node.js, Echo, React, Next.js, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, GCP Cloud Run, GitHub Actions, OpenTelemetry, Prometheus, Langfuse, ONNX} \\"""

    tex = (
        BASE.LATEX_TEMPLATE
        .replace("%BENTHAM_BULLETS%", "\n".join(item(b) for b in bentham))
        .replace("%GSOC_BULLETS%", "\n".join(item(b) for b in gsoc))
        .replace("%PROJECTS%", "\n".join(projects))
        .replace("%SKILLS%", skills)
    )
    tex = tex.replace(
        "{B.E. Artificial Intelligence and Machine Learning}{}",
        "{B.E. Artificial Intelligence and Machine Learning, 3rd Year}{}",
    )
    open_source_block = r"""
\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
\textbf{Open Source} & \bodyhref{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}{\textit{Contributions}} \\
\end{tabular*}
\resumeItemListStart
\resumeItem{Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway, Kyverno, Invesalius, Tiled, CRIU, and VideoLAN}, spanning backend failover behavior, parser robustness, security validation, compatibility fixes, and data/artifact correctness.}
\resumeItemListEnd
"""
    replacement = r"""
\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
\textbf{Open Source} & \bodyhref{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}{\textit{Contributions}} \\
\end{tabular*}
\resumeItemListStart
\resumeItem{Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway, Kyverno, Invesalius, CRIU, and VideoLAN}, spanning backend reliability, security validation, parser robustness, compatibility fixes, and artifact correctness.}
\resumeItemListEnd
"""
    tex = tex.replace(open_source_block, replacement)
    tex = tex.replace(r"\addtolength{\topmargin}{-.98in}", r"\addtolength{\topmargin}{-.97in}")
    tex = tex.replace(r"\addtolength{\textheight}{2.08in}", r"\addtolength{\textheight}{2.18in}")
    tex = tex.replace(r"\vspace{2pt}", r"\vspace{0pt}")
    tex = tex.replace(r"\newcommand{\resumeItem}[1]{\item{\fontsize{9.05pt}{9.75pt}\selectfont #1\vspace{-0.7pt}}}", r"\newcommand{\resumeItem}[1]{\item{\fontsize{8.85pt}{9.25pt}\selectfont #1\vspace{-0.5pt}}}")
    tex = tex.replace(r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.3pt,topsep=0.9pt,parsep=0pt,partopsep=0pt]}", r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.35pt,topsep=0.55pt,parsep=0pt,partopsep=0pt]}")
    tex = tex.replace(r"\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]", r"\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6.5pt}]")
    return tex


def build_application_note() -> str:
    return """# Sarvam - Intern Backend Engineering, Dubbing Pipeline

## Why I fit this role

This role is stronger for me than the ML & Speech Data Pipeline role because the JD is about production backend engineering for a complex async dubbing pipeline: FastAPI/Python, external provider APIs, retry logic, structured logging, timeout handling, provider abstractions, typed Python, tests, mocking, and observability.

My closest match is Swish, where I built FastAPI services around provider fallback, request timeouts, cooldown handling, local/Langfuse traces, deterministic fallbacks, and a live conversation-suite runner with retry-after handling and pytest regression checks. Hyoka is also directly relevant: FastAPI trace/event ingestion, OpenAI-compatible proxy, Python SDK hooks, worker leases, eval/replay runs, typed metadata models, and release gates.

For Sarvam specifically, I would position myself as someone who can read production Python code, trace data flow across async/provider-heavy paths, make failures visible, and improve reliability without overcomplicating the architecture.

## Application answer / short note

I am interested in this role because Sarvam's dubbing pipeline is exactly the kind of backend problem I enjoy: a production Python/FastAPI system where translation, TTS, QC, provider APIs, retries, timeouts, and observability all have to work together reliably. I am more drawn to making real AI pipelines robust than building isolated demos.

My closest work is Swish, where I built FastAPI support-agent services with provider fallback, request timeouts, cooldown handling, local/Langfuse traces, deterministic fallbacks, retry-aware test runners, and pytest regression checks. I also built Hyoka, a FastAPI agent reliability layer with trace ingestion, replay/eval runs, worker leases, typed metadata models, an OpenAI-compatible proxy, and Python SDK hooks. At Bentham AI (https://www.bentham.legal/), I worked on production workflow automation with retries, session recovery, checkpoints, Docker, Cloud Run, and GitHub Actions.

I think I can be useful on this internship because I am comfortable reading unfamiliar code, tracing data flow through backend systems, adding typed interfaces/configs, making failures observable, and improving retry/fallback behavior around external services.
"""


def build_gmail_ready_mail() -> str:
    return """Subject: Backend Engineering Intern - Dubbing Pipeline

Hi Sarvam team,

I am applying for the Backend Engineering internship on the dubbing pipeline. The role stood out because it is not a generic AI internship; it is production backend work around translation, TTS, QC, provider APIs, retries, timeouts, fallback behavior, and observability.

My closest work is Swish, where I built FastAPI support-agent services with provider fallback, cooldown handling, request timeouts, Gemini fallback paths, local JSON/Langfuse traces, retry-aware conversation test runs, and pytest regression checks. I also built Hyoka, a FastAPI reliability layer for AI agents with trace/event ingestion, eval/replay runs, worker leases, typed metadata, an OpenAI-compatible proxy, and Python SDK hooks.

At Bentham AI (https://www.bentham.legal/), I worked on backend workflow automation for legal/compliance filings with retries, session recovery, validation checkpoints, and Dockerized services on Cloud Run.

I think I can be useful on this pipeline because I am comfortable reading unfamiliar backend code, tracing data flow through provider-heavy systems, and making failures easier to classify, retry, log, and recover from without making the design messy.

I have attached my resume. Would be glad to discuss how I can contribute.

Best,
Shuvam
"""


def compile_pdf(tex_path: Path) -> None:
    for _ in range(2):
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
            cwd=tex_path.parent,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tex_path = OUT_DIR / "sarvam_dubbing_backend_resume.tex"
    note_path = OUT_DIR / "sarvam_dubbing_application_note.md"
    mail_path = OUT_DIR / "sarvam_dubbing_gmail_ready_mail.txt"
    tex_path.write_text(build_resume_tex(), encoding="utf-8")
    note_path.write_text(build_application_note(), encoding="utf-8")
    mail_path.write_text(build_gmail_ready_mail(), encoding="utf-8")
    compile_pdf(tex_path)
    print(tex_path)
    print(tex_path.with_suffix(".pdf"))
    print(note_path)
    print(mail_path)


if __name__ == "__main__":
    main()
