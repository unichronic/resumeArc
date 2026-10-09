from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "future_agi_applied_ai_2026_06_03"
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
        r"Modeled screenshots, API responses, generated drafts, form state, and failures as \textbf{recoverable workflow records}, making customer-facing workflow failures easier to debug and re-run.",
        r"Shipped Dockerized \textbf{Node.js/Go backend services} on \textbf{Google Cloud Run} with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
    )
    gsoc = (
        r"Contributed to Invesalius through \textbf{Google Summer of Code}, integrating Python workflows for \textbf{95 anatomical brain regions} with PyTorch/TorchScript, ONNX/TinyGrad paths, generated artifacts, and correctness checks.",
        r"Reduced expensive processing runtime by \textbf{87\%} through async/parallel execution while debugging GPU/CPU paths, large data movement, generated masks, and output correctness.",
    )
    projects = (
        project(
            "Hyoka Agent Reliability Layer",
            "Python, FastAPI, SQLAlchemy, PostgreSQL, OpenTelemetry, Next.js",
            BASE.bodyhref("https://github.com/unichronic/hyoka"),
            (
                r"Built a developer-facing \textbf{AI-agent reliability layer}: trace/event ingestion, \textbf{eval/replay runs}, failure mining, candidate generation, release gates, audit logs, and project-scoped API keys.",
                r"Implemented an \textbf{OpenAI-compatible proxy}, OTLP/OpenInference-style ingestion, \textbf{Python SDK hooks}, worker leases, artifacts, manifests, promotions, and a Next.js dashboard for trace/run/gate inspection.",
                r"Designed SQLite/PostgreSQL metadata models with SQLAlchemy/Alembic so agent behavior changes could be \textbf{reproduced, compared, promoted, or rolled back} safely.",
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
            "Penny Lane Multi-Agent Workflow",
            "Python, Agno, Pydantic, SQLite, JSONL, React/Vite",
            BASE.bodyhref("https://github.com/unichronic/pennylane"),
            (
                r"Built a \textbf{multi-agent workflow} with analyst, bull/bear debate, research manager, trader, risk-review, portfolio-approval, and evaluation stages wired through typed state.",
                r"Used \textbf{Pydantic state}, SQLite checkpoints, JSONL/full-state traces, baseline comparisons, validation harnesses, and a React/Vite inspection UI for reviewing agent outputs.",
            ),
        ),
        project(
            "Postificus Content Distribution Engine",
            "Go, Echo, React, PostgreSQL, Redis, RabbitMQ, Docker",
            BASE.bodyhref("https://github.com/unichronic/postificus"),
            (
                r"Built Go/Echo REST APIs and worker services with PostgreSQL persistence, Redis state/cache, RabbitMQ retry/DLQ jobs, Docker services, and Prometheus metrics.",
                r"Kept fragmented external workflows recoverable with saved state, retries, health checks, browser fallback execution, and clear UI status around publish/sync activity.",
            ),
        ),
    )
    skills = r"""\textbf{Languages}{: Python, TypeScript, JavaScript, Go} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, Echo, SQLAlchemy, PyTorch, Pydantic} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, GCP Cloud Run, GitHub Actions, OpenTelemetry, Langfuse, ONNX, REST APIs} \\"""

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


def build_application_note() -> str:
    return """# Future AGI - Applied AI / Developer Experience Intern

## Why This Role

I am interested in Future AGI because the product sits exactly in the part of AI engineering I have been building around: not just creating agents, but making them measurable, observable, debuggable, and safe enough for production use. The Applied AI / Developer Experience role stood out because it combines customer debugging, SDK/product integration, open-source work, examples, docs, and turning real implementation pain into better tools for developers.

My closest project is Hyoka, where I built an agent reliability layer with trace/event ingestion, eval/replay runs, failure mining, release gates, audit logs, an OpenAI-compatible proxy, Python SDK hooks, and a Next.js inspection dashboard. I also built Swish, an LLM-assisted support workflow where AI handled messy user language but deterministic policy controlled refunds, replacements, and escalations, with Langfuse/local traces and regression checks.

That is why this role feels like a strong fit: I have already spent time with the same kind of problems Future AGI is solving - traces, evals, guardrails, developer ergonomics, and making AI behavior easier to explain. I would like to work directly with customers, understand where they get stuck, and turn those learnings into better SDKs, examples, docs, and demos.

## Short Pitch

I build applied AI systems where the important part is not only the model call, but the surrounding reliability layer: traces, evals, replay, policy boundaries, recoverable workflows, and clear developer-facing examples. Future AGI's Applied AI role is a strong fit because Hyoka and Swish already map to the customer integration, SDK, observability, and AI evaluation problems the role focuses on.

## Possible Mail

Subject: Applied AI / Developer Experience Intern

Hi Future AGI team,

I came across the Applied AI / Developer Experience Intern role and wanted to apply because it is very close to the kind of AI engineering work I have been building.

My strongest fit is Hyoka, an agent reliability layer I built with trace/event ingestion, eval/replay runs, failure mining, release gates, audit logs, an OpenAI-compatible proxy, Python SDK hooks, and a Next.js dashboard for inspecting agent behavior. I also built Swish, an LLM-assisted support workflow with FastAPI, PostgreSQL/Redis state, Langfuse/local traces, regression checks, and deterministic policy boundaries around refunds and escalations.

What interests me about Future AGI is that the role is not just about using LLMs, but helping developers integrate, debug, evaluate, and observe AI systems in production. I would enjoy working with customers, finding where they get stuck, and turning those learnings into SDK improvements, docs, examples, and demos.

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
    tex_path = OUT_DIR / "future_agi_applied_ai_resume.tex"
    note_path = OUT_DIR / "future_agi_application_note.md"
    tex_path.write_text(build_resume_tex(), encoding="utf-8")
    note_path.write_text(build_application_note(), encoding="utf-8")
    compile_pdf(tex_path)
    print(tex_path)
    print(tex_path.with_suffix(".pdf"))
    print(note_path)


if __name__ == "__main__":
    main()
