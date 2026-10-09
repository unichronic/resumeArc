from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30"


def bodyhref(url: str, label: str = "GitHub") -> str:
    return rf"\bodyhref{{{url}}}{{{label}}}"


@dataclass(frozen=True)
class Project:
    title: str
    tech: str
    link: str
    bullets: tuple[str, ...]


@dataclass(frozen=True)
class Target:
    slug: str
    company: str
    role_angle: str
    recipient: str
    subject: str
    attachment: str
    intro: str
    company_read: str
    fit_bullets: tuple[str, ...]
    ask: str
    projects: tuple[str, str, str]
    skills: str
    experience_profile: str


PROJECTS: dict[str, Project] = {
    "hyoka_agent": Project(
        "Hyoka Evaluation/Replay Backend",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, OpenTelemetry, Docker",
        bodyhref("https://github.com/unichronic/hyoka"),
        (
            r"Built an \textbf{AI reliability backend} with trace ingestion, validation runs, replay workers, release gates, project-scoped API keys, \textbf{audit logs}, worker leases, and a dashboard.",
            r"Modeled traces, suites, candidates, gate decisions, artifacts, manifests, and worker state in \textbf{PostgreSQL/SQLite} with SQLAlchemy/Alembic.",
            r"Added evaluator registries, content-addressed artifacts, and controlled promotions so generated outputs could be compared, replayed, and shipped through explicit gates.",
        ),
    ),
    "hyoka_platform": Project(
        "Hyoka Control Plane",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, OpenTelemetry, Docker",
        bodyhref("https://github.com/unichronic/hyoka"),
        (
            r"Built a \textbf{control-plane style backend} for traces, validation suites, candidates, gate decisions, worker leases, API keys, audit logs, and release promotions.",
            r"Designed \textbf{PostgreSQL metadata models} and ingestion APIs so workflow behavior could be inspected, replayed, and compared before promotion.",
        ),
    ),
    "postificus_content": Project(
        "Postificus Content Distribution Platform",
        "Go, Echo, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        bodyhref("https://github.com/unichronic/postificus"),
        (
            r"Built a \textbf{content-distribution backend} with REST APIs, PostgreSQL persistence, Redis autosave, RabbitMQ workers, S3-compatible storage, and live job/status tracking.",
            r"Combined direct APIs with browser-fallback execution for fragmented third-party publishing surfaces where API coverage was incomplete or inconsistent.",
            r"Added \textbf{timeouts, retries, DLQs, circuit breakers, health checks, and Prometheus metrics} so long-running external workflows stayed recoverable.",
        ),
    ),
    "postificus_ops": Project(
        "Postificus Operations Backend",
        "Go, Echo, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        bodyhref("https://github.com/unichronic/postificus"),
        (
            r"Built queue-backed Go services with REST APIs, auth/settings endpoints, PostgreSQL persistence, Redis state, RabbitMQ workers, and durable job status.",
            r"Separated workers, retry queues, failure states, and service health checks across dependent external systems so failures did not cascade through the platform.",
        ),
    ),
    "swish_ops": Project(
        "Swish Support Workflow System",
        "Python, Go, FastAPI, React, PostgreSQL, Redis, Langfuse",
        bodyhref("https://github.com/unichronic/swishagent"),
        (
            r"Built an \textbf{operational support workflow} that pulls order, fleet, trust, evidence, and case context into assessment while deterministic policy code controls final actions.",
            r"Grounded support cases in \textbf{PostgreSQL/Redis state}, modeling active item, issue type, desired resolution, evidence strength, trust score, and escalation path.",
        ),
    ),
    "seaweed_backend": Project(
        "Seaweed Contest Platform",
        "Go, React, PostgreSQL, Redis, Judge0, Docker, Kubernetes",
        bodyhref("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built a \textbf{Go/PostgreSQL platform} for \textbf{500+ concurrent users}, covering registrations, submissions, async judging, admin review, and live ranked leaderboards.",
            r"Integrated Judge0 with async Go dispatch, PostgreSQL result schemas, Redis runtime state, Docker/Kubernetes deployment, and sub-\textbf{5s P95} verdict latency.",
        ),
    ),
    "penny_finance": Project(
        "Penny Lane Capital",
        "Python, Agno, Pydantic, SQLite, yfinance, JSONL",
        bodyhref("https://github.com/unichronic/pennylane"),
        (
            r"Built a \textbf{market-research workflow} with analyst roles, bull/bear debate, trader, risk review, portfolio approval, typed Pydantic state, SQLite checkpoints, and replayable JSONL traces.",
            r"Evaluated decisions with historical-market backtests, reward-loop scorecards, validation harnesses, and baseline comparisons across return, drawdown, win-rate, and risk signals.",
        ),
    ),
}


SKILLS = {
    "backend": r"""\textbf{Languages}{: Go, Python, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, Echo, Gin, SQLAlchemy} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, GCP Cloud Run, GitHub Actions, Prometheus, OpenTelemetry, REST APIs} \\""",
    "ai_backend": r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, SQLAlchemy, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, GCP Cloud Run, GitHub Actions, OpenTelemetry, Prometheus, Langfuse, REST APIs} \\""",
    "fintech": r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Next.js, Echo, SQLAlchemy, Pydantic} \\
   \textbf{Tools}{: PostgreSQL, SQLite, Redis, RabbitMQ, Docker, GCP Cloud Run, GitHub Actions, Prometheus, OpenTelemetry, REST APIs} \\""",
    "cloud": r"""\textbf{Languages}{: Go, Python, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, Node.js, React, Echo, SQLAlchemy} \\
   \textbf{Tools}{: Docker, Kubernetes, GCP Cloud Run, GitHub Actions, PostgreSQL, Redis, RabbitMQ, Prometheus, OpenTelemetry, REST APIs} \\""",
    "health": r"""\textbf{Languages}{: Python, Go, TypeScript, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, React, Next.js, Node.js, SQLAlchemy, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, OpenTelemetry, Prometheus, Langfuse, GitHub Actions, REST APIs, ONNX} \\""",
}


EXPERIENCE = {
    "backend": (
        r"Built filing-workflow backend automation with browser execution, public-site REST/API lookups, \textbf{retries}, \textbf{session recovery}, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Modeled API responses, screenshots, generated drafts, form state, and failure checkpoints as \textbf{recoverable workflow records} for debugging and re-running unreliable external-system steps.",
        r"Shipped Dockerized \textbf{Node.js/Go backend services} on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
    ),
    "ai_backend": (
        r"Built backend automation for compliance-sensitive workflows with browser execution, public-site API lookups, retries, \textbf{session recovery}, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Implemented a draft-generation flow for company-name suggestions, object descriptions, and filing-field drafts while keeping generated outputs inspectable before deterministic execution.",
        r"Shipped Dockerized Node.js/Go backend services on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
    ),
    "cloud": (
        r"Built filing-workflow backend automation with REST/API lookups, retries, session recovery, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Containerized Node.js/Go services with \textbf{Docker}, deployed on \textbf{Google Cloud Run}, and wired \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%}.",
        r"Modeled API responses, generated drafts, form state, screenshots, and failure checkpoints as recoverable workflow records for debugging unreliable external systems.",
    ),
    "health": (
        r"Built backend automation for compliance workflows with public-site API lookups, retries, session recovery, validation checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
        r"Implemented draft-generation and reviewable workflow state so generated outputs stayed inspectable before deterministic backend execution.",
        r"Shipped Dockerized Node.js/Go services on Google Cloud Run with GitHub Actions release workflows, improving deployment velocity by \textbf{70\%}.",
    ),
}


GSOC = {
    "default": (
        r"Integrated \textbf{Python workflows} for \textbf{95 anatomical brain regions}, wiring preprocessing, PyTorch/TorchScript and ONNX/TinyGrad execution paths, generated artifacts, and correctness checks into Invesalius.",
        r"Reduced processing runtime by \textbf{87\%} through async/parallel execution while debugging large data paths, orientation, label correctness, GPU/CPU execution, and reproducible output inspection.",
    ),
    "health": (
        r"Built \textbf{medical-imaging segmentation workflows} for \textbf{95 anatomical brain regions}, integrating preprocessing, PyTorch/TorchScript and ONNX/TinyGrad inference, generated masks, and 3D inspection paths.",
        r"Reduced expensive MRI-processing runtime by \textbf{87\%} through async/parallel execution while debugging orientation, label correctness, GPU/CPU paths, and reproducible output inspection.",
    ),
    "data": (
        r"Integrated Python data-processing workflows for \textbf{95 anatomical brain regions}, wiring preprocessing, model execution, generated artifacts, and correctness checks into a mature open-source application.",
        r"Reduced processing runtime by \textbf{87\%} through async/parallel execution while debugging large data paths, label correctness, and reproducible output inspection.",
    ),
}


TARGETS: tuple[Target, ...] = (
    Target(
        "vibrium",
        "Vibrium",
        "AI Agents / Backend Reliability Intern",
        "",
        "Backend/AI reliability internship inquiry - Vibrium",
        "vibrium_ai_backend_intern_resume.pdf",
        "I spent time reading about Vibrium's enterprise agentic AI work and wanted to reach out for backend or AI reliability internship opportunities.",
        "What stood out to me is that enterprise voice and digital workers need more than model calls: they need reliable tool execution, integrations, traces, evals, and customer-specific workflow automation.",
        (
            "Hyoka is directly relevant because I built trace ingestion, validation runs, replay workers, release gates, audit logs, and worker leases for AI workflows.",
            "Swish maps to enterprise agent grounding: operational context, deterministic policy, PostgreSQL/Redis state, evidence strength, and escalation paths.",
            "Postificus gives the backend reliability side: queues, retries, DLQs, circuit breakers, health checks, and Prometheus metrics around unreliable external integrations.",
        ),
        "If there is room for an intern around agents, integrations, backend workflow reliability, eval tooling, or observability, I would be glad to help.",
        ("hyoka_agent", "swish_ops", "postificus_ops"),
        SKILLS["ai_backend"],
        "ai_backend",
    ),
    Target(
        "ateli",
        "Ateli",
        "Marketplace Backend / Internal Tools Intern",
        "",
        "Backend internship inquiry - Ateli",
        "ateli_backend_intern_resume.pdf",
        "I looked into Ateli and liked the problem you are working on: reducing chaos in design and site execution by connecting architects, vendors, and execution partners.",
        "The backend problem seems practical and operational: vendor onboarding, material/order state, project handovers, inventory visibility, dashboards, and internal tools for urgent site workflows.",
        (
            "Postificus is my closest match because it handles fragmented external workflows with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, and status tracking.",
            "Swish is relevant for operational state modeling: evidence, issue type, desired resolution, trust/context, and escalation path.",
            "Seaweed shows I can build user-facing backend platforms with Go, PostgreSQL, Redis, async workers, and consistent live rankings under concurrent load.",
        ),
        "If you are open to interns, I would be interested in helping with backend APIs, marketplace operations, vendor/internal tools, or workflow automation.",
        ("postificus_content", "swish_ops", "seaweed_backend"),
        SKILLS["backend"],
        "backend",
    ),
    Target(
        "kluisz_ai",
        "Kluisz.ai",
        "Cloud Platform / Backend Intern",
        "",
        "Backend/platform internship inquiry - Kluisz.ai",
        "kluisz_ai_platform_intern_resume.pdf",
        "I looked into Kluisz.ai/NAVA and the AI-native cloud platform direction stood out to me.",
        "The work seems to sit around control planes, workload orchestration, observability, developer tooling, and reliable cloud operations for AI workloads.",
        (
            "At Bentham AI (https://www.bentham.legal/), I shipped Dockerized backend services on Cloud Run with GitHub Actions and improved deployment velocity by 70%.",
            "Postificus is relevant because it uses workers, queues, retries, health checks, Prometheus metrics, PostgreSQL, Redis, and RabbitMQ around long-running jobs.",
            "Hyoka adds the control-plane side: trace ingestion, worker leases, API keys, audit logs, validation runs, and release gates.",
        ),
        "If there is scope for an intern on backend services, platform tooling, workload reliability, observability, or internal developer tools, I would be excited to contribute.",
        ("postificus_ops", "hyoka_platform", "seaweed_backend"),
        SKILLS["cloud"],
        "cloud",
    ),
    Target(
        "stch",
        "STCH",
        "Backend / AI Product Intern",
        "enquiry@stch.ai",
        "Backend/product engineering internship inquiry - STCH",
        "stch_backend_product_intern_resume.pdf",
        "I looked into STCH and liked the idea of building AI-enabled software around fabric R&D and manufacturing workflows.",
        "The interesting backend work seems to be around structured experiment data, workflow states, dashboards, search/recommendation, and integrations with production systems.",
        (
            "Hyoka fits this kind of work because it treats generated outputs as things to evaluate, replay, gate, audit, and promote rather than just accept blindly.",
            "Postificus is relevant for backend workflow reliability: REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, circuit breakers, and Prometheus metrics.",
            "My GSoC work with Invesalius also gave me experience debugging data correctness and generated artifacts inside a mature technical application.",
        ),
        "If there is room for an intern on backend APIs, AI workflow tooling, data capture, internal dashboards, or product engineering, I would be glad to help.",
        ("hyoka_agent", "postificus_ops", "seaweed_backend"),
        SKILLS["ai_backend"],
        "ai_backend",
    ),
    Target(
        "grevoro",
        "Grevoro",
        "Python/Data Backend Intern",
        "info@grevoro.com",
        "Backend/data internship inquiry - Grevoro",
        "grevoro_backend_data_intern_resume.pdf",
        "I looked into Grevoro and liked that the work is tied to low-carbon industrial operations rather than a purely software-only product.",
        "If Grevoro builds internal software, the useful areas seem to be operational data workflows, process metrics, reporting, monitoring, and tools around manufacturing execution.",
        (
            "Postificus shows my backend reliability experience: REST APIs, queues, Redis/PostgreSQL state, retries, DLQs, health checks, and metrics around long-running workflows.",
            "At Bentham AI (https://www.bentham.legal/), I built automation around messy external systems with API lookups, session recovery, validation checks, and operator checkpoints.",
            "My GSoC work involved heavy Python data-processing paths, generated artifacts, correctness checks, and runtime optimization in a mature application.",
        ),
        "If there is room for an intern on Python/data workflows, internal tools, monitoring, operational dashboards, or backend automation, I would be interested.",
        ("postificus_ops", "hyoka_platform", "seaweed_backend"),
        SKILLS["backend"],
        "backend",
    ),
    Target(
        "pred",
        "PRED",
        "Backend / Real-Time Systems Intern",
        "",
        "Backend systems internship inquiry - PRED",
        "pred_backend_systems_intern_resume.pdf",
        "I looked into PRED and the sports prediction exchange angle stood out because the backend has to be correct, live, and observable.",
        "A prediction exchange likely needs real-time data ingestion, user/account state, market/order state, settlement logic, monitoring, and guardrails around risky workflows.",
        (
            "Postificus gives the queue/reliability piece: RabbitMQ workers, retries, DLQs, circuit breakers, Redis/PostgreSQL state, health checks, and metrics.",
            "Seaweed maps to live state and concurrency: Go services, PostgreSQL, Redis, async workers, and live ranked leaderboards for 500+ concurrent users.",
            "Penny Lane is relevant to the decision/risk side: market research workflows, typed state, backtests, scorecards, and replayable traces.",
        ),
        "If you are open to interns, I would be interested in backend work around APIs, data feeds, real-time state, risk/settlement workflows, or observability.",
        ("postificus_ops", "seaweed_backend", "penny_finance"),
        SKILLS["fintech"],
        "backend",
    ),
    Target(
        "aamra_seniors_club",
        "Aamra Seniors Club",
        "Backend / Ops Tooling Intern",
        "",
        "Backend/internal tools internship inquiry - Aamra",
        "aamra_seniors_club_backend_ops_intern_resume.pdf",
        "I looked into Aamra and liked that it is a real care/service operation, not just a generic health app.",
        "For a senior-care day club, useful software seems to be around member records, scheduling, check-ins, family communication, follow-ups, and internal operations tooling.",
        (
            "Swish is my closest project because it models support/care-like operational state: case context, evidence strength, desired resolution, trust/context, and escalation paths.",
            "At Bentham AI (https://www.bentham.legal/), I built backend automation around multi-step workflows, API lookups, validation checks, and operator checkpoints.",
            "Seaweed shows I can ship user-facing backend flows with Go, PostgreSQL, Redis, async workers, and stable behavior under concurrent users.",
        ),
        "If there is room for an intern on internal tools, member/scheduling systems, backend APIs, dashboards, or care-ops workflow automation, I would be glad to help.",
        ("swish_ops", "seaweed_backend", "postificus_ops"),
        SKILLS["health"],
        "health",
    ),
    Target(
        "puresta",
        "Puresta",
        "ML / Healthtech Backend Intern",
        "",
        "ML/backend internship inquiry - Puresta",
        "puresta_ml_backend_intern_resume.pdf",
        "I looked into Puresta and the health plus beauty direction, especially AI-assisted skin analysis and dermatology workflows, felt close to work I have already done.",
        "The product direction seems to need image/data pipelines, model-output evaluation, consultation workflows, ecommerce/backend state, and reliable health-data handling.",
        (
            "My GSoC work with Invesalius is directly relevant: I integrated segmentation workflows for 95 anatomical regions, generated masks, correctness checks, and optimized heavy image-processing paths by 87%.",
            "Hyoka adds the evaluation/replay side: trace ingestion, validation runs, release gates, audit logs, and reviewable generated outputs.",
            "Swish and Postificus show backend product reliability around operational workflows, PostgreSQL/Redis state, retries, status tracking, and human-reviewable decisions.",
        ),
        "If there is scope for an intern around image/health AI workflows, backend APIs, consultation/product workflows, or eval/replay tooling, I would be very interested.",
        ("hyoka_agent", "swish_ops", "postificus_ops"),
        SKILLS["health"],
        "health",
    ),
    Target(
        "frex",
        "Frex",
        "Fintech Backend Intern",
        "support@frexpay.com",
        "Backend internship inquiry - Frex",
        "frex_fintech_backend_intern_resume.pdf",
        "I looked into Frex and liked the focus on simplifying international money movement.",
        "The backend problems around cross-border payments seem to be reliability-heavy: partner APIs, workflow validation, compliance/KYC steps, audit trails, retries, and operational dashboards.",
        (
            "At Bentham AI (https://www.bentham.legal/), I built backend automation for compliance-sensitive workflows with API lookups, retries, session recovery, validation checks, and checkpoints.",
            "Hyoka is relevant because it models audit logs, validation runs, gate decisions, worker leases, and replayable workflow records.",
            "Postificus adds the integration reliability side with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, circuit breakers, and metrics.",
        ),
        "If there is room for an intern on backend APIs, partner integrations, KYC/compliance tooling, audit logs, or operational workflow reliability, I would be glad to contribute.",
        ("hyoka_platform", "postificus_ops", "seaweed_backend"),
        SKILLS["fintech"],
        "backend",
    ),
    Target(
        "ilios_72",
        "ILIOS 72 Alternative Capital",
        "Fintech Data / Backend Intern",
        "investorrelations@ILIOS72altcap.co.in",
        "Backend/data internship inquiry - ILIOS 72",
        "ilios_72_fintech_data_intern_resume.pdf",
        "I looked into ILIOS 72 and liked the research-backed alternative capital/wealth platform direction.",
        "Even at an early stage, investment platforms usually need clean data workflows: research records, reporting, dashboards, audit trails, portfolio/investor views, and internal tools.",
        (
            "Penny Lane Capital is directly relevant because I built a market-research workflow with analyst roles, risk review, typed state, checkpoints, backtests, scorecards, and replayable traces.",
            "Hyoka adds the auditability side: validation runs, gate decisions, audit logs, worker leases, and reviewable workflow records.",
            "Postificus shows backend reliability around REST APIs, PostgreSQL/Redis state, queues, retries, DLQs, circuit breakers, health checks, and metrics.",
        ),
        "If there is scope for an intern around backend APIs, research/reporting workflows, investor dashboards, analytics tooling, or audit-ready records, I would be interested.",
        ("penny_finance", "hyoka_platform", "postificus_ops"),
        SKILLS["fintech"],
        "backend",
    ),
)


LATEX_TEMPLATE = r"""% Tailored early-startup resume
\documentclass[letterpaper,11pt]{article}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage[normalem]{ulem}
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
\setlength{\footskip}{4.1pt}
\addtolength{\oddsidemargin}{-0.62in}
\addtolength{\evensidemargin}{-0.52in}
\addtolength{\textwidth}{1.22in}
\addtolength{\topmargin}{-.98in}
\addtolength{\textheight}{2.08in}
\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}
\titleformat{\section}{\vspace{-6pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]
\pdfgentounicode=1
\newcommand{\resumeItem}[1]{\item{\fontsize{9.05pt}{9.75pt}\selectfont #1\vspace{-0.7pt}}}
\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & \textbf{\small #2} \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}
\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{1.0\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & \textbf{\small #2}\\
    \end{tabular*}\vspace{-4pt}
}
\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}, itemsep=0.6pt, topsep=0pt, parsep=0pt, partopsep=0pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.3pt,topsep=0.9pt,parsep=0pt,partopsep=0pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-3pt}}

\begin{document}

\begin{center}
    {\Huge \scshape Shuvam Pal} \\ \vspace{1pt}
    \small \raisebox{-0.1\height}\faPhone\ +91 85830 54679 ~
    \href{mailto:ishuvam.pal@gmail.com}{\raisebox{-0.2\height}\faEnvelope\ {ishuvam.pal@gmail.com}} ~
    \href{https://linkedin.com/in/shuvampal3960}{\raisebox{-0.2\height}\faLinkedin\ {Shuvam Pal}} ~
    \href{https://github.com/unichronic}{\raisebox{-0.2\height}\faGithub\ {unichronic}}
    \vspace{-8pt}
\end{center}

\section{Education}
\resumeSubHeadingListStart
  \resumeSubheading
    {Dayananda Sagar College of Engineering}{Bengaluru, India}
    {B.E. Artificial Intelligence and Machine Learning}{}
\resumeSubHeadingListEnd

\section{Experience}
\resumeSubHeadingListStart
\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
\textbf{\bodyhref{https://www.bentham.legal/}{Bentham AI}} & \textit{Dec 2025 -- Feb 2026} \\
\textit{Backend Engineering Intern: Node.js, JavaScript, Go, Docker, GCP, GitHub Actions} & \textit{Remote} \\
\end{tabular*}
\vspace{-4pt}
\resumeItemListStart
%BENTHAM_BULLETS%
\resumeItemListEnd
\vspace{2pt}

\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
\textbf{\bodyhref{https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5}{Google Summer of Code}} & \textit{May 2025 -- Sept 2025} \\
\textit{Mentee at Invesalius: Python, VTK, wxPython, NumPy, PyTorch, ONNX} & \textit{Remote} \\
\end{tabular*}
\vspace{-4pt}
\resumeItemListStart
%GSOC_BULLETS%
\resumeItemListEnd
\vspace{2pt}

\item
\begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
\textbf{Open Source} & \bodyhref{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}{\textit{Contributions}} \\
\end{tabular*}
\resumeItemListStart
\resumeItem{Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway, Kyverno, Invesalius, Tiled, CRIU, and VideoLAN}, spanning backend failover behavior, parser robustness, security validation, compatibility fixes, and data/artifact correctness.}
\resumeItemListEnd
\resumeSubHeadingListEnd

\section{Projects}
\resumeSubHeadingListStart
%PROJECTS%
\resumeSubHeadingListEnd

\section{Technical Skills}
\begin{itemize}[leftmargin=0.15in, label={}, topsep=0pt, itemsep=0pt, parsep=0pt, partopsep=0pt]
  \item{\fontsize{9.6pt}{10.0pt}\selectfont
   %SKILLS%
  }
\end{itemize}

\end{document}
"""


def project_latex(key: str) -> str:
    p = PROJECTS[key]
    link = p.link
    bullets = "\n".join(rf"\resumeItem{{{b}}}" for b in p.bullets)
    return rf"""\resumeProjectHeading
{{\textbf{{{p.title}}} $|$ \emph{{{p.tech}}}}}{{{link}}}
\resumeItemListStart
{bullets}
\resumeItemListEnd"""


def resume_tex(target: Target) -> str:
    gsoc_key = "health" if target.experience_profile == "health" else "data" if target.slug == "grevoro" else "default"
    return (
        LATEX_TEMPLATE
        .replace("%BENTHAM_BULLETS%", "\n".join(rf"\resumeItem{{{b}}}" for b in EXPERIENCE[target.experience_profile]))
        .replace("%GSOC_BULLETS%", "\n".join(rf"\resumeItem{{{b}}}" for b in GSOC[gsoc_key]))
        .replace("%PROJECTS%", "\n".join(project_latex(k) for k in target.projects))
        .replace("%SKILLS%", target.skills)
    )


def email_markdown(target: Target) -> str:
    body_lines = [
        "Hi " + target.company.split()[0] + " team,",
        "",
        target.intro,
        "",
        target.company_read,
        "",
        "My closest relevant work:",
        "",
    ]
    body_lines.extend(f"- {b}" for b in target.fit_bullets)
    body_lines.extend([
        "",
        target.ask + " I have attached my resume for context.",
        "",
        "Regards,",
        "Shuvam Pal",
        "https://github.com/unichronic",
        "https://linkedin.com/in/shuvampal3960",
    ])
    body = "\n".join(body_lines)
    return f"""# {target.company} Email Draft

## Recipient

{target.recipient if target.recipient else "No verified public email in tracker. Use founder/key-person LinkedIn, company LinkedIn, or website contact route."}

## Subject

{target.subject}

## Attachment

`{target.attachment}`

## Body

{body}
"""


def read_body_from_email_md(path: str) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    marker = "## Body"
    if marker in text:
        return text.split(marker, 1)[1].strip()
    marker = "## Email"
    if marker in text:
        return text.split(marker, 1)[1].strip()
    return text.strip()


def app_script(drafts: list[dict[str, str]]) -> str:
    # Keep bodies literal and Gmail-ready. No markdown bold markers in bodies.
    return """/**
 * Gmail draft creator for early-startup internship outreach.
 *
 * How to use:
 * 1. Open https://script.google.com and create a new Apps Script project.
 * 2. Upload or sync the PDFs from startup_email_attachments_2026_05_30/ to one Google Drive folder.
 * 3. Paste the folder ID from the Drive URL in CONFIG.resumeDriveFolderId.
 * 4. Paste this whole file into Code.gs.
 * 5. Run previewDrafts() and previewResumeAttachments() to inspect logs.
 * 6. Run createDrafts().
 * 7. Approve Gmail and Drive access once.
 *
 * Notes:
 * - This creates Gmail drafts only. It does not send emails.
 * - If `to` is blank, the draft is created to your own Gmail address and the
 *   subject is prefixed with [ADD TO]. Replace the recipient manually in Gmail.
 * - Apps Script cannot read local paths or local/Colab Drive mounts directly.
 *   resumePath is only used to derive the PDF filename, which is looked up in
 *   Google Drive.
 * - If CONFIG.requireResumeAttachment is true, a draft is skipped when its
 *   matching PDF cannot be found in Drive.
 */

const CONFIG = {
  labelName: 'early-startup-internship-drafts',
  dryRun: false,
  dedupe: true,
  attachResumes: true,
  requireResumeAttachment: true,
  // Paste the ID from a Drive folder URL. Leave blank to search all visible Drive files by filename.
  resumeDriveFolderId: '',
  createMissingRecipientDraftsToSelf: true,
  missingRecipientSubjectPrefix: '[ADD TO] ',
};

const DRAFTS = """ + json.dumps(drafts, indent=2) + """;

function previewDrafts() {
  DRAFTS.forEach((draft, index) => {
    const to = clean_(draft.to) || '[ADD TO]';
    Logger.log(`${index + 1}. ${draft.company} -> ${to} | ${draft.subject} | resume: ${draft.resumePath || '[none]'}`);
  });
  Logger.log(`Total drafts: ${DRAFTS.length}`);
}

function previewResumeAttachments() {
  let found = 0;
  let missing = 0;

  DRAFTS.forEach((draft, index) => {
    const fileName = getFileNameFromPath_(draft.resumePath);
    const file = fileName ? findResumeFile_(fileName) : null;

    if (file) {
      found += 1;
      Logger.log(`${index + 1}. FOUND ${draft.company}: ${fileName}`);
    } else {
      missing += 1;
      Logger.log(`${index + 1}. MISSING ${draft.company}: ${fileName || '[no resumePath]'}`);
    }
  });

  Logger.log(`Resume attachments found: ${found}; missing: ${missing}.`);
}

function createDrafts() {
  const label = getOrCreateLabel_(CONFIG.labelName);
  const activeEmail = getSessionEmail_('active');
  const effectiveEmail = getSessionEmail_('effective');
  const selfEmail = activeEmail || effectiveEmail;
  const props = PropertiesService.getUserProperties();

  let created = 0;
  let skipped = 0;

  Logger.log(`Active user email: ${activeEmail || '[blank]'}`);
  Logger.log(`Effective user email: ${effectiveEmail || '[blank]'}`);
  Logger.log(`Draft label: ${CONFIG.labelName}`);

  DRAFTS.forEach((draft, index) => {
    const company = clean_(draft.company) || `Draft ${index + 1}`;
    const originalTo = clean_(draft.to);
    let to = originalTo;
    let subject = clean_(draft.subject) || company;
    let body = String(draft.body || '').trim();

    if (!body) {
      Logger.log(`Skipped ${company}: missing body`);
      skipped += 1;
      return;
    }

    if (!to) {
      if (!CONFIG.createMissingRecipientDraftsToSelf || !selfEmail) {
        Logger.log(`Skipped ${company}: missing recipient`);
        skipped += 1;
        return;
      }
      to = selfEmail;
      subject = `${CONFIG.missingRecipientSubjectPrefix}${subject}`;
      body = `TO FILL: ${company}

${body}`;
    }

    const resumeFileName = getFileNameFromPath_(draft.resumePath);
    const attachments = [];

    if (CONFIG.attachResumes && resumeFileName) {
      const resumeFile = findResumeFile_(resumeFileName);

      if (!resumeFile) {
        Logger.log(`Missing resume attachment for ${company}: ${resumeFileName}`);

        if (CONFIG.requireResumeAttachment) {
          skipped += 1;
          return;
        }
      } else {
        attachments.push(resumeFile.getBlob().setName(resumeFileName));
      }
    }

    const attachmentNames = attachments.map((attachment) => attachment.getName()).join(',');
    const dedupeKey = buildDedupeKey_(company, to, subject, body, attachmentNames);
    if (CONFIG.dedupe && props.getProperty(dedupeKey)) {
      Logger.log(`Skipped duplicate: ${company}`);
      skipped += 1;
      return;
    }

    if (CONFIG.dryRun) {
      Logger.log(`[DRY RUN] ${company} -> ${to} | ${subject} | attachment: ${attachmentNames || '[none]'} | resume: ${draft.resumePath || '[none]'}`);
      created += 1;
      return;
    }

    const options = attachments.length ? { attachments } : {};
    const gmailDraft = GmailApp.createDraft(to, subject, body, options);
    label.addToThread(gmailDraft.getMessage().getThread());
    props.setProperty(dedupeKey, new Date().toISOString());
    Logger.log(`Created draft: ${company} -> ${to} | attachment: ${attachmentNames || '[none]'} | resume: ${draft.resumePath || '[none]'}`);
    created += 1;
  });

  Logger.log(`Done. Created ${created}; skipped ${skipped}.`);
  Logger.log(`Verify in Gmail with: in:drafts label:${CONFIG.labelName}`);
}

function resetDraftDedupe() {
  PropertiesService.getUserProperties().deleteAllProperties();
  Logger.log('Cleared draft dedupe keys.');
}

function verifyCreatedDrafts() {
  const activeEmail = getSessionEmail_('active');
  const effectiveEmail = getSessionEmail_('effective');
  const query = `in:drafts label:${CONFIG.labelName}`;
  const allDrafts = GmailApp.getDrafts();
  const threads = GmailApp.search(query, 0, 100);

  Logger.log(`Active user email: ${activeEmail || '[blank]'}`);
  Logger.log(`Effective user email: ${effectiveEmail || '[blank]'}`);
  Logger.log(`Total drafts visible to this script: ${allDrafts.length}`);
  Logger.log(`Draft search query: ${query}`);
  Logger.log(`Matching draft threads found: ${threads.length}`);
}

function getOrCreateLabel_(name) {
  const existing = GmailApp.getUserLabelByName(name);
  return existing || GmailApp.createLabel(name);
}

function clean_(value) {
  return String(value || '').trim();
}

function buildDedupeKey_(company, to, subject, body, attachmentNames) {
  const raw = [company, to, subject, body, attachmentNames || ''].join('\\n');
  const digest = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, raw);
  return `draft:${Utilities.base64EncodeWebSafe(digest)}`;
}

function getFileNameFromPath_(path) {
  const parts = String(path || '').split('/');
  return clean_(parts[parts.length - 1]);
}

function findResumeFile_(fileName) {
  if (!fileName) {
    return null;
  }

  const folderId = clean_(CONFIG.resumeDriveFolderId);
  const files = folderId
    ? DriveApp.getFolderById(folderId).getFilesByName(fileName)
    : DriveApp.getFilesByName(fileName);

  return files.hasNext() ? files.next() : null;
}

function getSessionEmail_(kind) {
  try {
    const user = kind === 'effective' ? Session.getEffectiveUser() : Session.getActiveUser();
    return user && user.getEmail ? String(user.getEmail() || '').trim() : '';
  } catch (error) {
    return '';
  }
}
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    drafts: list[dict[str, str]] = []

    for t in TARGETS:
        tex_name = t.attachment.replace(".pdf", ".tex")
        email_path = OUT_DIR / f"{t.slug}_email.md"
        (OUT_DIR / tex_name).write_text(resume_tex(t), encoding="utf-8")
        if not email_path.exists():
            email_path.write_text(email_markdown(t), encoding="utf-8")
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_name], cwd=OUT_DIR, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_name], cwd=OUT_DIR, check=True, stdout=subprocess.DEVNULL)
        drafts.append({
            "company": t.company,
            "to": t.recipient,
            "subject": t.subject,
            "resumePath": f"tailored_resumes/early_startups_rest_2026_05_30/{t.attachment}",
            "body": read_body_from_email_md(str(email_path.relative_to(ROOT))),
        })

    readme_lines = [
        "# Early Startup Rest Application Pack",
        "",
        "| Company | Angle | Resume | Email draft | Recipient |",
        "|---|---|---|---|---|",
    ]
    for t in TARGETS:
        readme_lines.append(
            f"| {t.company} | {t.role_angle} | `{t.attachment}` | `{t.slug}_email.md` | {t.recipient or 'LinkedIn/contact route'} |"
        )
    (OUT_DIR / "README.md").write_text("\n".join(readme_lines) + "\n", encoding="utf-8")
    (OUT_DIR / "early_startups_rest_gmail_drafts.gs").write_text(app_script(drafts), encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "tools" / "rebuild_vibrium_onwards_resumes.py")], check=True)


if __name__ == "__main__":
    main()
