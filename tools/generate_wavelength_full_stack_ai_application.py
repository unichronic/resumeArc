from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "wavelength_full_stack_ai_2026_05_31"
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
        r"Owned \textbf{backend automation for legal/compliance workflows} at \bodyhref{https://www.bentham.legal/}{Bentham AI}, combining \textbf{browser execution}, public-site API lookups, retries, \textbf{session recovery}, validation checks, and operator checkpoints to reduce manual filing time by \textbf{85\%}.",
        r"Built an \textbf{AI-assisted drafting flow} for company-name suggestions, object descriptions, and filing-field drafts while keeping \textbf{generated outputs inspectable} before deterministic execution.",
        r"Modeled \textbf{screenshots, API responses, generated drafts, form state, and failures} as recoverable workflow records, making ambiguous external-system failures easier to \textbf{debug and re-run}.",
        r"Shipped Dockerized \textbf{Node.js/Go services} on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
    )
    gsoc = (
        r"Integrated \textbf{Python medical-imaging workflows} for \textbf{95 anatomical brain regions}, wiring preprocessing, \textbf{PyTorch/TorchScript}, ONNX/TinyGrad execution paths, generated artifacts, and correctness checks into Invesalius.",
        r"Built \textbf{model-output inspection} paths around generated masks, label remapping, orientation checks, progress reporting, and reproducible artifact debugging.",
        r"Reduced expensive processing runtime by \textbf{87\%} through async/parallel execution while debugging \textbf{GPU/CPU paths}, large data movement, and output correctness.",
    )
    projects = (
        project(
            "Swish Food-Delivery Support Automation",
            "Python, FastAPI, React, PostgreSQL, Redis, Langfuse",
            BASE.bodyhref("https://github.com/unichronic/swishagent"),
            (
                r"Built an \textbf{LLM-assisted support workflow} with \textbf{FastAPI services} and a \textbf{React/Vite UI}, carrying order, kitchen, fleet, trust, evidence, issue, and conversation context across user-facing decisions.",
                r"Kept compensation actions \textbf{policy-bound} while AI handled \textbf{messy customer language}; \textbf{PostgreSQL/Redis} stored session state, issue signals, trust context, and follow-up behavior.",
                r"Added \textbf{Langfuse/local traces}, optional Hyoka trace export, pytest regressions, response-quality checks, and \textbf{deterministic fallbacks} so AI behavior stayed inspectable.",
            ),
        ),
        project(
            "Hyoka Agent Reliability Layer",
            "Python, FastAPI, SQLAlchemy, PostgreSQL, OpenTelemetry",
            BASE.bodyhref("https://github.com/unichronic/hyoka"),
            (
                r"Built an \textbf{agent reliability and evaluation layer}: \textbf{trace/event ingestion}, \textbf{eval/replay runs}, failure mining, candidate generation, \textbf{release gates}, audit logs, and project-scoped API keys.",
                r"Implemented an \textbf{OpenAI-compatible proxy}, OTLP/OpenInference-style ingestion, worker leases, artifacts, manifests, promotions, and a \textbf{Next.js dashboard} for trace/run/gate inspection.",
                r"Designed \textbf{SQLite/PostgreSQL metadata models} with SQLAlchemy/Alembic so agent behavior changes could be \textbf{reproduced, compared, promoted, or rolled back} safely.",
            ),
        ),
        project(
            "Postificus Content Distribution Engine",
            "Go, Echo, React, Vite, PostgreSQL, Redis/RabbitMQ, Go-Rod",
            BASE.bodyhref("https://github.com/unichronic/postificus"),
            (
                r"Built a full-stack \textbf{content distribution product} with \textbf{React/Vite editor flows}, platform connection management, activity/status views, and \textbf{Go/Echo REST APIs}.",
                r"Used \textbf{PostgreSQL persistence}, Redis state/cache, \textbf{RabbitMQ retry/DLQ jobs}, Docker services, Prometheus metrics, direct APIs, and \textbf{browser fallback execution} for fragmented third-party platforms.",
                r"Kept long-running external workflows \textbf{recoverable} with saved state, retries, health checks, worker metrics, and clear \textbf{UI status} around publish/sync activity.",
            ),
        ),
        project(
            "Penny Lane Multi-Agent Research Workflow",
            "Python, Agno, Pydantic, SQLite, JSONL, React/Vite",
            BASE.bodyhref("https://github.com/unichronic/pennylane"),
            (
                r"Built a \textbf{multi-agent workflow} with analyst, bull/bear debate, research manager, trader, risk-review, portfolio-approval, and evaluation stages wired through \textbf{typed state}.",
                r"Used \textbf{Pydantic state}, SQLite checkpoints, \textbf{JSONL/full-state traces}, baseline comparisons, validation harnesses, and a \textbf{React/Vite inspection UI} for agent-output review.",
            ),
        ),
    )
    skills = r"""\textbf{Languages}{: TypeScript, JavaScript, Python, Go} \\
   \textbf{Frameworks}{: React, Next.js, FastAPI, Node.js, Echo, SQLAlchemy, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, GCP Cloud Run, GitHub Actions, Langfuse, OpenTelemetry, Prometheus} \\"""

    tex = (
        BASE.LATEX_TEMPLATE
        .replace("%BENTHAM_BULLETS%", "\n".join(item(b) for b in bentham))
        .replace("%GSOC_BULLETS%", "\n".join(item(b) for b in gsoc))
        .replace("%PROJECTS%", "\n".join(projects))
        .replace("%SKILLS%", skills)
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
    tex = tex.replace(open_source_block, "")
    tex = tex.replace(r"\addtolength{\topmargin}{-.98in}", r"\addtolength{\topmargin}{-1.02in}")
    tex = tex.replace(r"\addtolength{\textheight}{2.08in}", r"\addtolength{\textheight}{2.22in}")
    tex = tex.replace(r"\vspace{2pt}", r"\vspace{0pt}")
    tex = tex.replace(r"\newcommand{\resumeItem}[1]{\item{\fontsize{9.05pt}{9.75pt}\selectfont #1\vspace{-0.7pt}}}", r"\newcommand{\resumeItem}[1]{\item{\fontsize{8.8pt}{9.15pt}\selectfont #1\vspace{-0.55pt}}}")
    tex = tex.replace(r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.3pt,topsep=0.9pt,parsep=0pt,partopsep=0pt]}", r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.35pt,topsep=0.55pt,parsep=0pt,partopsep=0pt]}")
    tex = tex.replace(r"\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]", r"\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6.5pt}]")
    return tex


def build_email_md() -> str:
    email_body = build_email_body()
    pitch = build_pitch()
    return f"""# Wavelength - Full Stack + AI

To: jayanth@heywavelength.com

Subject: Full stack + AI role - via Akash Singh

{email_body}

## Short Elevator Pitch

{pitch}
"""


def build_email_body() -> str:
    return """Hi Jayanth,

I heard about the Wavelength opening from Akash Singh and went through the JD. The part that stood out to me was that you are not just building another wrapper around an LLM; it looks like the hard part is product, agent behavior, context, trust, and fast iteration for a very human use case.

Quick pitch: I am Shuvam, a B.E. AIML student in Bengaluru who likes building end-to-end systems more than isolated demos. I have worked on FastAPI/Node/Go backends, React/Next product surfaces, Postgres/Redis state, Docker/GCP deployments, and AI workflows that are traceable instead of opaque. At Bentham AI (https://www.bentham.legal/), I built backend automation for compliance workflows and reduced manual filing time by 85%. In Hyoka, I built an agent reliability layer with traces, eval/replay runs, release gates, audit logs, and an OpenAI-compatible proxy. In Swish, I built an LLM-assisted support workflow where AI handled messy user language but deterministic policy still controlled refunds, coupons, and escalations. I also built a multi-agent workflow in Penny Lane with typed state, checkpoints, traces, and a React/Vite inspection UI.

React Native would be the ramp area for me, but the surrounding pieces are very close to work I have already done: React/Next interfaces, production-style APIs, databases, queues, deployment flows, and AI-agent infrastructure. The ownership-heavy founding engineer setup is exactly the kind of environment I am looking for.

I am based in Bengaluru for college, so HSR in-office is workable for me. I have attached a resume tailored to the role.

Best,
Shuvam Pal
LinkedIn: https://linkedin.com/in/shuvampal3960
GitHub: https://github.com/unichronic"""


def build_pitch() -> str:
    return "I looked into Wavelength and I think I can help on the full-stack AI layer: building product features, backend APIs, Postgres/Redis state, agent workflows, and reliability around LLM behavior. My strongest work is not just prompts, but making AI features inspectable, recoverable, and useful inside real user workflows."


def build_email_txt() -> str:
    return """To: jayanth@heywavelength.com
Subject: Full stack + AI role - via Akash Singh

""" + build_email_body() + """

Short elevator pitch:
""" + build_pitch() + """
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
    tex_path = OUT_DIR / "wavelength_full_stack_ai_resume.tex"
    md_path = OUT_DIR / "wavelength_mail_and_pitch.md"
    txt_path = OUT_DIR / "wavelength_gmail_ready_mail.txt"
    tex_path.write_text(build_resume_tex(), encoding="utf-8")
    md_path.write_text(build_email_md(), encoding="utf-8")
    txt_path.write_text(build_email_txt(), encoding="utf-8")
    compile_pdf(tex_path)
    print(tex_path)
    print(tex_path.with_suffix(".pdf"))
    print(md_path)
    print(txt_path)


if __name__ == "__main__":
    main()
