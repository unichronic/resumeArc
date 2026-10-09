from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

import generate_selected_internship_resumes as base


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "next_applications_2026_05_25"


@dataclass(frozen=True)
class Resume:
    slug: str
    company: str
    role: str
    focus: str
    experience_profile: str
    open_source_profile: str
    project_keys: tuple[str, str, str]
    skills: str
    source: str
    note: str


PROJECTS = dict(base.PROJECTS)
PROJECTS.update(
    {
        "penny_crypto_trading": base.Project(
            "Penny Lane Capital",
            "Python, Agno, Pydantic, SQLite, Vector Memory, yfinance, JSONL",
            base.href("https://github.com/unichronic/pennylane"),
            (
                r"Built a multi-agent market-research workflow with analyst roles, bull/bear debate, trader, risk review, portfolio approval, typed Pydantic state, SQLite checkpoints, and replayable JSONL traces.",
                r"Evaluated decisions with historical-market backtests, reward-loop style scorecards, validation harnesses, and baseline comparisons across return, drawdown, win-rate, and risk signals.",
            ),
        ),
        "hyoka_control_plane": base.Project(
            "Hyoka",
            "Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL, OpenTelemetry, Next.js, Docker",
            "",
            (
                r"Built an \textbf{AI-agent reliability control plane} with SDK/proxy/OTLP trace ingestion, evaluator registries, replay modes, failure mining, validation runs, gate decisions, promotions, and audit logs.",
                r"Implemented worker-owned execution leases, content-addressed artifacts, signed manifests, project-scoped API keys, SQLAlchemy/Alembic models, and a Next.js dashboard for operating agent behavior safely.",
            ),
        ),
        "seaweed_product": base.Project(
            "Seaweed: Contest Platform",
            "TypeScript, React, Next.js, Go, PostgreSQL, Judge0, Firebase, Docker",
            base.href("https://github.com/unichronic/seaweed-fe"),
            (
                r"Built a production-style React/Next.js assessment platform with auth-gated problem pages, code editor, submissions, admin review, shortlisting, and live ranked leaderboards.",
                r"Implemented Go judging APIs with Judge0, PostgreSQL rankings/materialized views, Redis-backed runtime state, and Docker/Kubernetes deployment for \textbf{500+ concurrent users}.",
            ),
        ),
        "postificus_product": base.Project(
            "Postificus",
            "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
            base.href("https://github.com/unichronic/postificus"),
            (
                r"Built browser-automation-backed product workflows with REST APIs, RabbitMQ workers, Redis autosave, PostgreSQL persistence, durable job status, and recoverable external publishing tasks.",
                r"Added retries, DLQs, circuit-breaker isolation, health checks, and Prometheus metrics so long-running API/browser workflows stayed observable and fault-tolerant.",
            ),
        ),
        "swish_ai_product": base.Project(
            "Swish Support System",
            "JavaScript, React, Python, PostgreSQL/pgvector, Redis, Langfuse",
            base.href("https://github.com/unichronic/swishagent"),
            (
                r"Built a hybrid AI + rules support system where LLM assessments classify messy complaint semantics while deterministic policy code controls refunds, replacements, coupons, and escalations.",
                r"Grounded responses in order, item, evidence, customer, and policy context with PostgreSQL/pgvector, Redis state, Langfuse traces, confidence thresholds, and regression checks.",
            ),
        ),
        "invesalius_ai_pipeline": base.Project(
            "Invesalius Medical Imaging Tooling",
            "Python, VTK, wxPython, NumPy, PyTorch, ONNX",
            base.href("https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5", "GSoC"),
            (
                r"Built Python MRI segmentation tooling for \textbf{95 anatomical regions}, covering preprocessing, orientation correction, model inference, generated masks, and large-volume image paths.",
                r"Reduced processing runtime by \textbf{87\%} with asynchronous and parallel execution while keeping model outputs inspectable through masks and 3D reconstructed surfaces.",
            ),
        ),
    }
)


EXPERIENCE = {
    "teal_fullstack": {
        "bentham": (
            r"Owned product-facing automation features in a small engineering team, turning ambiguous MCA filing steps into reliable Node.js/Puppeteer workflows with operator checkpoints.",
            r"Built backend validation, retries, public-site API lookups, and recoverable session state, reducing manual filing time by \textbf{85\%}.",
            r"Shipped Dockerized services on Google Cloud Run with GitHub Actions releases, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Contributed production-grade Python features inside a mature open-source application, coordinating model outputs, UI paths, generated artifacts, and user inspection workflows.",
            r"Reduced expensive image-processing runtime by \textbf{87\%} through async/parallel execution while preserving correctness on large data paths.",
            r"Worked through unfamiliar code quickly across VTK, wxPython, NumPy, PyTorch/ONNX-adjacent inference, and label-mapping logic.",
        ),
    },
    "aicte_fullstack": {
        "bentham": (
            r"Built full-stack workflow automation around structured forms, public-site data lookups, browser actions, backend state, and operator-visible failure recovery.",
            r"Implemented JavaScript/Node.js services that generated validated AI-assisted drafts before handing them into filing automation, cutting manual effort by \textbf{85\%}.",
            r"Packaged and deployed services with Docker, Google Cloud Run, and GitHub Actions, improving release speed by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python tooling for MRI segmentation workflows, connecting preprocessing, model inference, generated masks, and 3D visualization in an existing desktop application.",
            r"Improved runtime by \textbf{87\%} with asynchronous and parallel execution over large medical-image volumes.",
            r"Debugged cross-module integration issues across Python data handling, NumPy, PyTorch/ONNX-style inference, and VTK/wxPython UI behavior.",
        ),
    },
    "ai_systems": {
        "bentham": (
            r"Built an AI-assisted workflow for structured company-registration drafts, combining prompt outputs, operator validation, public-site API lookups, retries, and automation handoff.",
            r"Implemented async backend execution with browser automation, session recovery, state validation, and failure-aware retries, reducing manual filing time by \textbf{85\%}.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python medical-image segmentation tooling across \textbf{95 brain subparts}, covering preprocessing, orientation correction, model inference, generated masks, and large MRI data paths.",
            r"Reduced segmentation runtime by \textbf{87\%} using asynchronous and parallel execution while preserving inspection workflows for generated masks and 3D surfaces.",
            r"Debugged model-output pipeline issues across conformation, label mapping, PyTorch/ONNX-style inference, and binary mask generation inside a mature open-source codebase.",
        ),
    },
    "crypto_ai": {
        "bentham": (
            r"Built failure-aware automation around multi-step public-site workflows with retries, state validation, session recovery, API lookups, and operator checkpoints.",
            r"Optimized an AI-assisted drafting pipeline that generated structured suggestions and carried validated outputs into downstream automation.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python inference workflows inside a mature open-source application, integrating preprocessing, model execution, output validation, and inspectable generated artifacts.",
            r"Reduced processing runtime by \textbf{87\%} with asynchronous and parallel execution across heavy data paths.",
            r"Worked through reliability issues across large inputs, typed outputs, label mapping, and PyTorch/ONNX-style model integration.",
        ),
    },
    "factech_saas": {
        "bentham": (
            r"Built operational SaaS automation for multi-step filings where each browser/API action recorded recoverable state, validation errors, and operator checkpoints.",
            r"Reduced manual filing time by \textbf{85\%} by hardening flaky public-site workflows with retries, session recovery, and backend state validation.",
            r"Used Docker, Cloud Run, and GitHub Actions to keep deployments repeatable and reduce release friction by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Improved reliability and performance inside a large open-source Python application with image-processing, model-output, and visualization workflows.",
            r"Reduced runtime by \textbf{87\%} by splitting expensive processing into asynchronous and parallel paths.",
            r"Debugged mature-codebase issues across UI, data transformation, generated artifacts, and PyTorch/ONNX-adjacent integration points.",
        ),
    },
    "dafi_web3": {
        "bentham": (
            r"Built and deployed Node.js automation services that combined backend APIs, browser automation, generated AI-assisted drafts, validation, and user-visible recovery states.",
            r"Reduced manual workflow time by \textbf{85\%} while keeping long-running automation steps recoverable through retries and session-state checks.",
            r"Handled Docker packaging, Google Cloud Run deployment, and GitHub Actions release automation for faster iteration.",
        ),
        "gsoc": (
            r"Built Python features in a mature open-source codebase, integrating model inference, generated artifacts, performance-sensitive processing, and UI inspection paths.",
            r"Cut processing runtime by \textbf{87\%} using async/parallel execution over large input data.",
            r"Adapted quickly across unfamiliar systems including VTK/wxPython UI code, NumPy data paths, and PyTorch/ONNX-style inference behavior.",
        ),
    },
}


OPEN_SOURCE = {
    "fullstack_product": (
        r"Contributed maintainer-reviewed patches across \textbf{Tiled}, \textbf{Kuadrant MCP Gateway}, \textbf{Kyverno}, VideoLAN, CRIU, and IOOS, spanning UI/compatibility fixes, backend integration behavior, parser robustness, and Zip Slip path validation.",
    ),
    "ai_systems": (
        r"Contributed to \textbf{Kuadrant MCP Gateway} reliability behavior, \textbf{Kyverno} policy/infrastructure paths, and IOOS/Tiled data or visualization tooling under maintainer review.",
    ),
    "crypto_ai": (
        r"Contributed reliability and systems patches across \textbf{Kuadrant MCP Gateway}, Kyverno, CRIU, VideoLAN, and Tiled, including backend-outage grace handling, parser robustness, and security-validation paths.",
    ),
}


SKILLS = {
    "crypto": r"""\textbf{Languages}{: Python, TypeScript, Go, SQL, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Next.js, React, Node.js, Agno, PyTorch, Echo} \\
   \textbf{Tools}{: PostgreSQL, SQLite, Redis, Vector Memory, OpenTelemetry, Docker, GCP, GitHub Actions, JSONL} \\""",
    "teal": r"""\textbf{Languages}{: JavaScript, TypeScript, Python, Go, SQL} \\
   \textbf{Frameworks}{: React, Next.js, Node.js, Express, FastAPI, Echo, PyTorch} \\
   \textbf{Tools}{: MongoDB, PostgreSQL, Redis, Docker, AWS, GCP, GitHub Actions, Firebase Auth, Judge0} \\""",
    "python_fullstack": r"""\textbf{Languages}{: Python, JavaScript, TypeScript, Go, SQL} \\
   \textbf{Frameworks}{: FastAPI, React, Next.js, Node.js, Express, Echo, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, MySQL, SQLite, Redis, Docker, AWS, GCP, GitHub Actions, Postman, Firebase} \\""",
    "ripik": r"""\textbf{Languages}{: Python, TypeScript, Go, SQL, C++} \\
   \textbf{Frameworks}{: FastAPI, PyTorch, React, Next.js, Node.js, Agno, VTK, wxPython} \\
   \textbf{Tools}{: PostgreSQL/pgvector, Redis, SQLite, Vector Memory, OpenTelemetry, Docker, GCP, GitHub Actions, Langfuse, ONNX} \\""",
    "factech": r"""\textbf{Languages}{: JavaScript, TypeScript, Python, Go, SQL} \\
   \textbf{Frameworks}{: React, Next.js, Node.js, Express, FastAPI, Echo} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, GitHub Actions, GCP, Prometheus, Langfuse, Postman, Firebase} \\""",
    "dafi": r"""\textbf{Languages}{: JavaScript, TypeScript, Python, Go, SQL} \\
   \textbf{Frameworks}{: React, Next.js, Node.js, Express, FastAPI, Echo, Agno} \\
   \textbf{Tools}{: PostgreSQL, MongoDB, Redis, Docker, Git, GitHub Actions, GCP, OpenTelemetry, JSONL} \\""",
}


RESUMES = [
    Resume(
        "proofbuild_crypto_ai_trading_agent_resume",
        "proof_of_Build",
        "AI + Crypto Software Engineer Intern",
        "AI trading agent, strategy/research workflows, backtesting, risk checks, FastAPI/Postgres/Redis backend",
        "crypto_ai",
        "crypto_ai",
        ("penny_crypto_trading", "hyoka_control_plane", "postificus_product"),
        SKILLS["crypto"],
        "https://proofbuild.lovable.app/p/34cf4cc4-611d-494d-9924-221951f0def0",
        "Strong on AI-agent infrastructure, market-research/backtest workflow, and backend reliability; weaker on Solidity/live exchange APIs, so present as fast learner with strong safety/evaluation instincts.",
    ),
    Resume(
        "teal_full_stack_software_engineer_intern_resume",
        "Teal India",
        "Intern - Software Engineer - Full Stack",
        "MERN/Next.js, applied AI, product engineering, automation, ambiguity, Bangalore",
        "teal_fullstack",
        "fullstack_product",
        ("seaweed_product", "swish_ai_product", "postificus_product"),
        SKILLS["teal"],
        "https://wellfound.com/jobs/3712550-intern-software-engineer-full-stack",
        "Very strong fit. Lead with React/Next, backend APIs, automation, product ownership, and ability to work from Bengaluru.",
    ),
    Resume(
        "aicte_python_full_stack_internship_resume",
        "AICTE Internship Portal",
        "Python Full Stack Internship",
        "Python, FastAPI, React, REST APIs, databases, deployment, student internship portal",
        "aicte_fullstack",
        "fullstack_product",
        ("hyoka_fullstack", "seaweed_fullstack", "postificus_automation"),
        SKILLS["python_fullstack"],
        "https://internship.aicte-india.org",
        "Use only after finding the exact official AICTE portal listing. The AlexaHire page is an aggregator, not the final source of truth.",
    ),
    Resume(
        "ripik_ai_engineer_intern_resume",
        "Ripik.ai",
        "Intern - AI Engineer",
        "Python, LLMs, model workflows, AI/ML product features, demos/POCs, Noida WFO",
        "ai_systems",
        "ai_systems",
        ("hyoka_control_plane", "swish_ai_product", "penny_crypto_trading"),
        SKILLS["ripik"],
        "https://ripiktechnologyprivatelimited.keka.com/careers/jobdetails/129796?source=linkedin",
        "Very strong AI-engineering fit if Noida office is acceptable. Emphasize Python, LLM/eval systems, model integration, and clear product documentation.",
    ),
    Resume(
        "factech_ai_full_stack_intern_resume",
        "Factech",
        "AI Engineer / Full Stack Intern",
        "AI-assisted product engineering, facility-management SaaS, full-stack implementation, testing, practical automation",
        "factech_saas",
        "fullstack_product",
        ("hyoka_fullstack", "postificus_product", "swish_ai_product"),
        SKILLS["factech"],
        "https://factech.ai/career/",
        "Public AI Engineer Intern post was not verified on Factech's own site. Use this for the social comment/DM or AI-assisted full-stack roles.",
    ),
    Resume(
        "dafi_labs_mern_blockchain_intern_resume",
        "Dafi Labs",
        "MERN / Blockchain Development Intern",
        "MERN, AI-assisted development, blockchain learning, remote internship, product delivery",
        "dafi_web3",
        "crypto_ai",
        ("seaweed_product", "penny_crypto_trading", "postificus_product"),
        SKILLS["dafi"],
        "https://empradar.ai/job/b8325489-6c0d-45ad-b31f-e89a0d01582e?utm_source=widget&utm_medium=embed&utm_campaign=dafilabs-b864",
        "Apply to both Blockchain Development Intern and MERN Stack Intern. Be honest that blockchain is a learning target while JavaScript/product/backend work is already strong.",
    ),
]


def render_project(key: str) -> str:
    project = PROJECTS[key]
    return rf"""
\resumeProjectHeading
{{\textbf{{{project.title}}} $|$ \emph{{{project.tech}}}}}{{{project.link}}}
\resumeItemListStart
\resumeItem{{{project.bullets[0]}}}
\resumeItem{{{project.bullets[1]}}}
\resumeItemListEnd
"""


def render_resume(resume: Resume) -> str:
    exp = EXPERIENCE[resume.experience_profile]
    open_source = OPEN_SOURCE[resume.open_source_profile][0]
    projects = "\n".join(render_project(key) for key in resume.project_keys)
    return rf"""{base.PREAMBLE}
\begin{{center}}
    {{\Huge \scshape Shuvam Pal}} \\ \vspace{{1pt}}
    \small \raisebox{{-0.1\height}}\faPhone\ +91 85830 54679 ~
    \href{{mailto:ishuvam.pal@gmail.com}}{{\raisebox{{-0.2\height}}\faEnvelope\ {{ishuvam.pal@gmail.com}}}} ~
    \href{{https://linkedin.com/in/shuvampal3960}}{{\raisebox{{-0.2\height}}\faLinkedin\ {{Shuvam Pal}}}}  ~
    \href{{https://github.com/unichronic}}{{\raisebox{{-0.2\height}}\faGithub\ {{unichronic}}}}
    \vspace{{-8pt}}
\end{{center}}

\section{{Education}}
\resumeSubHeadingListStart
  \resumeSubheading
    {{Dayananda Sagar College of Engineering}}{{Bengaluru, India}}
    {{B.E. Artificial Intelligence and Machine Learning}}{{}}
\resumeSubHeadingListEnd

\section{{Experience}}
\resumeSubHeadingListStart

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://www.bentham.legal/}}{{Bentham AI}}}} & \textit{{Dec 2025 -- Feb 2026}} \\
\textit{{Backend Engineering Intern: Node.js, JavaScript, Go, Docker, GCP, GitHub Actions}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
\resumeItem{{{exp["bentham"][0]}}}
\resumeItem{{{exp["bentham"][1]}}}
\resumeItem{{{exp["bentham"][2]}}}
\resumeItemListEnd

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5}}{{Google Summer of Code}}}} & \textit{{May 2025 -- Sept 2025}} \\
\textit{{Mentee at Invesalius: Python, VTK, wxPython, NumPy, PyTorch, ONNX}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
\resumeItem{{{exp["gsoc"][0]}}}
\resumeItem{{{exp["gsoc"][1]}}}
\resumeItem{{{exp["gsoc"][2]}}}
\resumeItemListEnd

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{Open Source}} & \bodyhref{{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}}{{\textit{{Contributions}}}} \\
\end{{tabular*}}
\resumeItemListStart
\resumeItem{{{open_source}}}
\resumeItemListEnd

\resumeSubHeadingListEnd

\section{{Projects}}
\resumeSubHeadingListStart
{projects}
\resumeSubHeadingListEnd

\section{{Technical Skills}}
\begin{{itemize}}[leftmargin=0.15in, label={{}}]
  \small{{\item{{
   {resume.skills}
  }}}}
\end{{itemize}}

\end{{document}}
"""


def write_report() -> Path:
    rows = [
        "# Next Internship Tailored Resumes",
        "",
        "Generated by `tools/generate_next_internship_resumes.py`.",
        "",
        "| Company | Role | Resume PDF | Focus | Source | Note |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for resume in RESUMES:
        rows.append(
            f"| {resume.company} | {resume.role} | `{resume.slug}.pdf` | "
            f"{resume.focus} | {resume.source} | {resume.note} |"
        )
    path = OUT_DIR / "resume_fit_report.md"
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return path


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tex_paths: list[Path] = []
    for resume in RESUMES:
        path = OUT_DIR / f"{resume.slug}.tex"
        path.write_text(render_resume(resume), encoding="utf-8")
        tex_paths.append(path)

    report = write_report()
    failures: list[str] = []
    for path in tex_paths:
        result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-output-directory",
                str(OUT_DIR),
                str(path),
            ],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            failures.append(path.name)

    for pattern in ("*.aux", "*.log", "*.out"):
        for path in OUT_DIR.glob(pattern):
            path.unlink()

    print(f"Generated {len(tex_paths)} TeX resumes in {OUT_DIR.relative_to(ROOT)}")
    print(f"Wrote fit report to {report.relative_to(ROOT)}")
    print(f"Compiled {len(tex_paths) - len(failures)} PDFs")
    if failures:
        print("Failures:")
        for name in failures:
            print(f"  {name}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
