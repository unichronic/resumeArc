from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "feedback_backend_genai_2026_06_03"
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
        r"Implemented an \textbf{AI-assisted drafting flow} for company-name suggestions, object descriptions, and filing-field drafts while keeping generated outputs inspectable before deterministic execution.",
        r"Modeled screenshots, API responses, generated drafts, form state, and failures as \textbf{recoverable workflow records}, making ambiguous external-system failures easier to debug and re-run.",
        r"Shipped Dockerized \textbf{Node.js/Go backend services} on \textbf{Google Cloud Run} with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
    )
    gsoc = (
        r"Integrated Python workflows for \textbf{95 anatomical brain regions}, wiring preprocessing, PyTorch/TorchScript, ONNX/TinyGrad execution paths, generated artifacts, and correctness checks into Invesalius.",
        r"Reduced expensive processing runtime by \textbf{87\%} through async/parallel execution while debugging GPU/CPU paths, large data movement, generated masks, and output correctness.",
    )
    projects = (
        project(
            "Hyoka Agent Reliability Layer",
            "Python, FastAPI, SQLAlchemy, PostgreSQL, OpenTelemetry, Next.js",
            BASE.bodyhref("https://github.com/unichronic/hyoka"),
            (
                r"Built a developer-facing \textbf{AI-agent reliability layer}: trace/event ingestion, \textbf{eval/replay runs}, failure mining, candidate generation, release gates, audit logs, and project-scoped API keys.",
                r"Implemented an \textbf{OpenAI-compatible proxy}, OTLP/OpenInference-style ingestion, Python SDK hooks for LLM/tool/retrieval events, worker leases, artifacts, manifests, and promotions.",
                r"Designed SQLite/PostgreSQL models with SQLAlchemy/Alembic so agent behavior changes could be \textbf{reproduced, compared, promoted, or rolled back} safely.",
            ),
        ),
        project(
            "Swish Support Automation",
            "Python, FastAPI, React, PostgreSQL, Redis, Langfuse",
            BASE.bodyhref("https://github.com/unichronic/swishagent"),
            (
                r"Built \textbf{LLM-assisted support automation} with FastAPI services and a React/Vite UI, carrying order, kitchen, fleet, trust, evidence, issue, and conversation context across user-facing decisions.",
                r"Kept refunds, coupons, replacements, and escalations \textbf{policy-bound}; PostgreSQL/Redis stored session state, issue signals, trust context, and follow-up behavior.",
                r"Added \textbf{Langfuse/local traces}, optional Hyoka trace export, pytest regression suites, response-quality checks, and deterministic fallbacks so AI behavior stayed inspectable.",
            ),
        ),
        project(
            "Penny Lane Multi-Agent Research Workflow",
            "Python, Agno, Pydantic, SQLite, JSONL, React/Vite",
            BASE.bodyhref("https://github.com/unichronic/pennylane"),
            (
                r"Built a \textbf{multi-agent research workflow} with analyst, bull/bear debate, research manager, trader, risk-review, portfolio-approval, and evaluation stages wired through typed state.",
                r"Used \textbf{Pydantic state}, SQLite checkpoints, JSONL/full-state traces, yfinance market data, optional vector memory, baseline comparisons, and validation harnesses.",
            ),
        ),
        project(
            "Postificus Content Distribution Engine",
            "Go, Echo, React, PostgreSQL, Redis, RabbitMQ, Docker",
            BASE.bodyhref("https://github.com/unichronic/postificus"),
            (
                r"Built Go/Echo \textbf{REST APIs and worker services} with PostgreSQL persistence, Redis state/cache, RabbitMQ retry/DLQ jobs, Docker services, and Prometheus metrics.",
                r"Kept long-running external workflows recoverable with saved state, retries, health checks, browser fallback execution, and clear UI status around publish/sync activity.",
            ),
        ),
    )
    skills = r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, Echo, SQLAlchemy, PyTorch, Pydantic} \\
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
    tex = tex.replace(r"\addtolength{\topmargin}{-.98in}", r"\addtolength{\topmargin}{-1.03in}")
    tex = tex.replace(r"\addtolength{\textheight}{2.08in}", r"\addtolength{\textheight}{2.23in}")
    tex = tex.replace(r"\vspace{2pt}", r"\vspace{0pt}")
    tex = tex.replace(r"\newcommand{\resumeItem}[1]{\item{\fontsize{9.05pt}{9.75pt}\selectfont #1\vspace{-0.7pt}}}", r"\newcommand{\resumeItem}[1]{\item{\fontsize{8.85pt}{9.25pt}\selectfont #1\vspace{-0.5pt}}}")
    tex = tex.replace(r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.3pt,topsep=0.9pt,parsep=0pt,partopsep=0pt]}", r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.35pt,topsep=0.55pt,parsep=0pt,partopsep=0pt]}")
    tex = tex.replace(r"\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]", r"\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6.5pt}]")
    return tex


def build_mail() -> str:
    return """Subject: Backend + GenAI internship possibility

Hi [Founder Name],

I saw the AI Engineer (Backend + GenAI) role on Whitetable. I understand it is a 5+ year full-time role, so I am not trying to position myself as the senior hire you are looking for there. I wanted to ask if you would consider an intern around the same direction: backend engineering for GenAI systems, agent workflows, evaluation, observability, and production reliability.

My closest work is Hyoka, an AI-agent reliability layer I built with FastAPI, PostgreSQL/SQLite metadata, trace/event ingestion, eval/replay runs, release gates, audit logs, an OpenAI-compatible proxy, and Python SDK hooks for LLM/tool/retrieval events. I also built Swish, an LLM-assisted support workflow with FastAPI, PostgreSQL/Redis state, Langfuse/local traces, regression checks, and deterministic policy boundaries around refunds and escalations. At Bentham AI (https://www.bentham.legal/), I worked on backend automation for compliance workflows with retries, session recovery, checkpoints, Docker, Cloud Run, and GitHub Actions.

I do not have 5 years of experience, and I do not want to overstate that. But I have been building in the same problem area: Python/FastAPI backends, LLM workflows, agent traces/evals, recoverable state, deployment, and debugging AI behavior instead of treating model calls as a black box. If there is room for an intern who can help with backend services, GenAI workflow infrastructure, eval/replay tooling, observability, or internal prototypes, I would be glad to contribute.

I have attached my resume for context.

Best,
Shuvam Pal
LinkedIn: https://linkedin.com/in/shuvampal3960
GitHub: https://github.com/unichronic
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
    tex_path = OUT_DIR / "feedback_backend_genai_resume.tex"
    mail_path = OUT_DIR / "feedback_founder_mail.txt"
    tex_path.write_text(build_resume_tex(), encoding="utf-8")
    mail_path.write_text(build_mail(), encoding="utf-8")
    compile_pdf(tex_path)
    print(tex_path)
    print(tex_path.with_suffix(".pdf"))
    print(mail_path)


if __name__ == "__main__":
    main()
