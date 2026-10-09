from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "selected_internships"


def href(url: str, label: str = "GitHub") -> str:
    return rf"\bodyhref{{{url}}}{{{label}}}"


@dataclass(frozen=True)
class Project:
    title: str
    tech: str
    link: str
    bullets: tuple[str, str]


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


PROJECTS: dict[str, Project] = {
    "seaweed_fullstack": Project(
        "Seaweed: Contest Platform",
        "TypeScript, React, Next.js, Go, PostgreSQL, Judge0, Firebase",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built a \textbf{React/Next.js assessment UI} with auth-gated problem pages, code editor, submissions, admin review/shortlisting, and live ranked leaderboards.",
            r"Implemented Go judging APIs with Judge0, PostgreSQL rankings/materialized views, Redis-backed runtime state, and Docker/Kubernetes deployment for \textbf{500+ concurrent users} and \textbf{sub-5s P95 verdict latency}.",
        ),
    ),
    "postificus_delivery": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built Go/Echo services for a content distribution platform using browser automation, REST APIs, RabbitMQ workers, Redis autosave, and PostgreSQL persistence.",
            r"Added retries, DLQs, circuit-breaker isolation, health checks, and Prometheus metrics so unreliable external browser/API workflows stayed recoverable across distributed workers.",
        ),
    ),
    "hyoka_fullstack": Project(
        "Hyoka",
        "Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL, Next.js, TypeScript, Docker",
        "",
        (
            r"Built a \textbf{reliability control plane for AI agents} with trace/event ingestion, authenticated APIs, suites, candidates, validation runs, gate decisions, promotions, audit logs, and a Next.js operations dashboard.",
            r"Implemented SQLAlchemy/Alembic metadata models, project-scoped API keys, content-addressed artifacts, signed manifests, worker-owned execution leases, and Docker Compose deployment with Postgres-backed services.",
        ),
    ),
    "hyoka_agent_eval": Project(
        "Hyoka",
        "Python, FastAPI, OpenTelemetry, PostgreSQL, Typer, Next.js, Docker",
        "",
        (
            r"Built a pluggable \textbf{AI-agent evaluation and replay layer} that captures LLM, tool, retrieval, memory, latency, cost, error, and metadata traces through SDK, proxy, event, scrape, and OTLP/JSON ingestion paths.",
            r"Added evaluator registries, replay modes, failure mining, evidence-hashed candidate proposals, validation runs, release gates, signed manifests, and worker leases for controlled agent-behavior promotion.",
        ),
    ),
    "hyoka_research": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, OpenTelemetry, Typer, JSON Schema, Docker",
        "",
        (
            r"Built autonomous self-improvement cycles that mine failed evaluation slices, generate candidate patch bundles, launch validation runs, compare baseline versus candidate behavior, and record gated promotions.",
            r"Designed reproducible replay and evaluation around immutable inputs, content-addressed artifacts, signed run manifests, audit history, JSON schema checks, latency/cost constraints, and LLM-judge hooks.",
        ),
    ),
    "swish_product": Project(
        "Swish Support System",
        "JavaScript, React, Python, PostgreSQL/pgvector, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built a \textbf{hybrid AI + rule-based logic system} where LLM assessments classify messy complaint semantics while deterministic policy code controls refunds, replacements, coupons, and escalations.",
            r"Grounded responses in order, item, evidence, customer, and policy context with PostgreSQL/pgvector, Redis state, Langfuse traces, and regression checks for multi-turn cases.",
        ),
    ),
    "swish_search": Project(
        "Swish Support System",
        "Python, FastAPI, PostgreSQL/pgvector, Redis, Langfuse, React",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built retrieval-backed support workflows where LLM calls use customer, order, item, evidence, and policy context before producing traceable assessments and responses.",
            r"Separated semantic understanding from deterministic action rules, adding confidence thresholds, human handoff paths, Langfuse traces, and regression checks for ambiguous conversations.",
        ),
    ),
    "penny_memory": Project(
        "Penny Lane Capital",
        "Python, Agno, Pydantic, SQLite, Vector Memory, JSONL",
        href("https://github.com/unichronic/pennylane"),
        (
            r"Built a multi-agent research workflow with analyst roles, bull/bear debate, trader, risk review, portfolio approval, typed Pydantic state, SQLite checkpoints, and JSONL traces.",
            r"Implemented \textbf{vector memory} and semantic lesson retrieval so agents could pull similar past decisions into context and inspect retrieval quality through validation harnesses.",
        ),
    ),
    "penny_research": Project(
        "Penny Lane Capital",
        "Python, Agno, Pydantic, SQLite, Vector Memory, yfinance, JSONL",
        href("https://github.com/unichronic/pennylane"),
        (
            r"Built a research workflow with role-specific agents, debate, risk review, portfolio approval, checkpointed state, and replayable JSONL traces for repeated market windows.",
            r"Evaluated decisions with historical-market backtests, reward-loop style scorecards, validation harnesses, and baseline comparisons across return, drawdown, and win-rate signals.",
        ),
    ),
    "seaweed_eval": Project(
        "Seaweed: Contest Platform",
        "Go, React, PostgreSQL, Judge0, Redis, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Architected a full-stack evaluation platform supporting \textbf{500+ concurrent users}, automated judging, live rankings, and reproducible submission/result records.",
            r"Designed async Go dispatch around Judge0 with PostgreSQL result schemas, Redis-backed runtime state, Docker/Kubernetes deployment, and \textbf{sub-5s P95 verdict latency}.",
        ),
    ),
    "invesalius_workflow": Project(
        "Invesalius Medical Imaging Tooling",
        "Python, VTK, wxPython, NumPy, PyTorch, ONNX",
        href("https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5", "GSoC"),
        (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions}, covering preprocessing, orientation correction, model inference, binary masks, and large-volume image paths.",
            r"Reduced processing runtime by \textbf{87\%} with asynchronous and parallel execution while keeping model outputs inspectable through masks and 3D reconstructed surfaces.",
        ),
    ),
    "postificus_automation": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, AWS",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built backend workflows that coordinate content transformation, image storage, autosave, durable job status, and browser automation across external publishing platforms.",
            r"Used RabbitMQ, Redis, PostgreSQL, and Dockerized Go services to keep long-running integrations recoverable, auditable, and simple to operate.",
        ),
    ),
}


EXPERIENCE = {
    "fullstack_delivery": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js workflow engine} for MCA company-registration filings, reducing manual filing time by \textbf{85\%} through state recovery, retries, and public-site API lookups.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across customer workflow preparation.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions}, integrating model inference, preprocessing, generated masks, and 3D visualization into an existing application.",
            r"Reduced processing runtime by \textbf{87\%} using asynchronous and parallel execution across expensive image-processing workflows.",
            r"Debugged integration issues across PyTorch/ONNX-style inference, label mapping, VTK/wxPython UI paths, and large-volume medical data handling.",
        ),
    },
    "ai_search": {
        "bentham": (
            r"Built an \textbf{AI-assisted workflow} for company-registration drafts, combining structured prompt outputs, operator validation, public-site API lookups, and automation handoff.",
            r"Implemented async backend execution with retries, session recovery, browser automation, and state validation, reducing manual filing time by \textbf{85\%}.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python medical-image segmentation tooling for \textbf{95 brain subparts}, covering preprocessing, orientation correction, model inference, generated masks, and large-volume MRI data paths.",
            r"Reduced segmentation runtime by \textbf{87\%} using asynchronous and parallel execution while preserving inspection workflows for generated masks and 3D surfaces.",
            r"Debugged model-output pipeline issues across conformation, label mapping, PyTorch/ONNX-style inference, and binary mask generation inside a mature open-source codebase.",
        ),
    },
    "research_systems": {
        "bentham": (
            r"Built an AI-assisted workflow for structured company-registration drafts, using public-site API lookups, operator validation, retries, and automation handoff across multi-step filings.",
            r"Reduced manual filing time by \textbf{85\%} by implementing session recovery, browser automation, state validation, and failure-aware backend execution.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built scientific Python tooling for MRI segmentation across \textbf{95 anatomical regions}, handling preprocessing, orientation correction, deep-learning inference, and generated-mask workflows.",
            r"Reduced runtime by \textbf{87\%} using asynchronous and parallel execution over large medical-image volumes while preserving inspectable outputs.",
            r"Improved 3D reconstructed surface visualization and debugged data/model-output issues inside a mature open-source medical-imaging codebase.",
        ),
    },
}


OPEN_SOURCE = {
    "fullstack_delivery": (
        r"Contributed maintainer-reviewed patches to \textbf{Invesalius} medical-imaging UI/compatibility paths, \textbf{Tiled} editor workflows, \textbf{Kuadrant MCP Gateway} reliability code, and \textbf{Kyverno} policy/infrastructure paths, plus parsing/security fixes such as Zip Slip path validation.",
    ),
    "ai_search": (
        r"Contributed to \textbf{Invesalius} model-output and PyTorch/ONNX-adjacent workflows, plus \textbf{IOOS/Tiled} data and visualization tooling and VideoLAN/CRIU parsing or systems robustness fixes under maintainer review.",
    ),
    "research_systems": (
        r"Contributed to research-adjacent open source including \textbf{Invesalius} medical-imaging workflows, \textbf{IOOS} scientific-data tooling, and \textbf{Tiled} map/visual editor code, plus compatibility and security-validation fixes.",
    ),
    "agent_infra": (
        r"Contributed to \textbf{Kuadrant MCP Gateway} backend-outage grace handling with recovery/removal test coverage, plus \textbf{Kyverno} policy/infrastructure context and Invesalius reliability fixes under maintainer review.",
    ),
}


SKILLS = {
    "aidash": r"""\textbf{Languages}{: Python, TypeScript, Go, SQL, C++} \\
   \textbf{Frameworks}{: React, Next.js, Node.js, FastAPI, Echo, Gin, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, SQLAlchemy, Redis, RabbitMQ, Docker, GCP, AWS, GitHub Actions, Firebase, Prometheus} \\""",
    "ai_search": r"""\textbf{Languages}{: Python, TypeScript, Go, C++} \\
   \textbf{Frameworks}{: PyTorch, FastAPI, Node.js, React, Next.js, Agno} \\
   \textbf{Tools}{: PostgreSQL/pgvector, Redis, SQLite, Vector Memory, Langfuse, OpenTelemetry, Docker, GCP, GitHub Actions, ONNX} \\""",
    "research": r"""\textbf{Languages}{: Python, C++, Go, TypeScript, SQL} \\
   \textbf{Frameworks}{: PyTorch, FastAPI, Node.js, React, VTK, wxPython, Agno} \\
   \textbf{Tools}{: NumPy, PostgreSQL, SQLite, Redis, Vector Memory, OpenTelemetry, Docker, GitHub Actions, ONNX, JSONL} \\""",
    "openrag": r"""\textbf{Languages}{: Python, TypeScript, JavaScript, Go} \\
   \textbf{Frameworks}{: FastAPI, React, Next.js, Node.js, Gin, Echo, Agno, PyTorch} \\
   \textbf{Tools}{: PostgreSQL/pgvector, Redis, SQLite, Vector Memory, Langfuse, OpenTelemetry, Docker, GCP, GitHub Actions, Prometheus} \\""",
}


RESUMES = [
    Resume(
        "aidash_software_engineer_intern",
        "AiDASH",
        "Software Engineer Intern",
        "full-stack customer engineering, Python/React/TypeScript, SQL/NoSQL, migrations, product customizations",
        "fullstack_delivery",
        "fullstack_delivery",
        ("seaweed_fullstack", "hyoka_fullstack", "postificus_delivery"),
        SKILLS["aidash"],
        "https://jobhunch.in/jobs/00002P",
        "Best direct fit. Lead with product engineering, React/TypeScript, Python APIs, databases, worker services, and cloud delivery.",
    ),
    Resume(
        "coupang_ai_engineer_search_discovery",
        "Coupang",
        "AI Engineer Intern - Search & Discovery",
        "LLMs, NLP, retrieval, search/recommendation systems, AI evaluation, Python",
        "ai_search",
        "ai_search",
        ("swish_search", "penny_memory", "hyoka_agent_eval"),
        SKILLS["ai_search"],
        "https://www.hirerush.in/jobs/593",
        "Strong AI systems fit, but resume should compensate for no explicit recommender project by emphasizing retrieval, semantic memory, replay, and evaluations.",
    ),
    Resume(
        "flywire_academy_research_intern",
        "FlyWire",
        "Academy Summer Research Intern",
        "computational neuroscience, graph/data analysis, ML, visualization, scientific software",
        "research_systems",
        "research_systems",
        ("hyoka_research", "penny_research", "seaweed_eval"),
        SKILLS["research"],
        "https://codex.flywire.ai/academy_summer_internships",
        "Research fit is carried by GSoC experience plus reproducible evaluation, analysis, and scientific/software tooling projects.",
    ),
    Resume(
        "openrag_ai_engineering_intern",
        "OpenRAG",
        "AI Engineering Intern",
        "RAGbots, generative AI agents, context grounding, evaluation, AI product systems",
        "ai_search",
        "agent_infra",
        ("hyoka_agent_eval", "swish_search", "penny_memory"),
        SKILLS["openrag"],
        "mailto:support@openrag.in",
        "Unverified role, but the strongest cold-email resume is agent reliability + RAG/context grounding + memory/evaluation workflows.",
    ),
    Resume(
        "eximius_ai_research_systems_intern",
        "Eximius Ventures",
        "AI Research & Systems Intern",
        "AI research tooling, market/research workflows, agents, evaluation, backend systems",
        "research_systems",
        "research_systems",
        ("hyoka_research", "penny_research", "swish_search"),
        SKILLS["research"],
        "mailto:hr@eximiusvc.com",
        "No public opening found. This version is for cold email and emphasizes research systems, agent evaluation, and analytical workflows.",
    ),
]


PREAMBLE = r"""% Generated selected-internship resume. Source: tools/generate_selected_internship_resumes.py
\documentclass[letterpaper,11pt]{article}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage[normalem]{ulem}
\let\oldhref\href
\newcommand{\bodyhref}[2]{\href{#1}{\underline{#2}\,\faExternalLink*}}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}
\input{glyphtounicode}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-.76in}
\addtolength{\textheight}{1.48in}
\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}
\titleformat{\section}{\vspace{-5pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]
\pdfgentounicode=1
\newcommand{\resumeItem}[1]{\item\small{{#1 \vspace{-3pt}}}}
\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & \textbf{\small #2} \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}
\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{1.001\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & \textbf{\small #2}\\
    \end{tabular*}\vspace{-7pt}
}
\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-6pt}}
\begin{document}
"""


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
    return rf"""{PREAMBLE}
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
        "# Selected Internship Tailored Resumes",
        "",
        "Generated by `tools/generate_selected_internship_resumes.py`.",
        "",
        "| Company | Role | Resume PDF | Focus | Source | Note |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for resume in RESUMES:
        rows.append(
            f"| {resume.company} | {resume.role} | `{resume.slug}_resume.pdf` | "
            f"{resume.focus} | {resume.source} | {resume.note} |"
        )
    path = OUT_DIR / "resume_fit_report.md"
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return path


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tex_paths: list[Path] = []
    for resume in RESUMES:
        path = OUT_DIR / f"{resume.slug}_resume.tex"
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
