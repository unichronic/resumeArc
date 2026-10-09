from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "recent_interns"


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
    fit: str
    source: str
    focus: str
    experience_profile: str
    project_keys: tuple[str, str, str]
    skills: str
    gap_note: str


PROJECTS = {
    "swish_ai_backend": Project(
        "Swish Support System",
        "Python, Go, FastAPI, Gin, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built an \textbf{AI-assisted support backend} where LLM calls classify messy customer complaints, intent, severity, ambiguity, and photo-evidence usefulness while deterministic code controls refund, replacement, coupon, and escalation policy.",
            r"Maintained per-conversation context, evidence artifacts, order/customer state, and traceable actions across multi-turn workflows with PostgreSQL, Redis, Langfuse/local traces, and regression tests for edge cases.",
        ),
    ),
    "swish_agent_eval": Project(
        "Swish Support System",
        "Python, Go, FastAPI, Gin, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built AI workflow infrastructure for support conversations with context memory, policy-grounded action selection, multimodal evidence checks, and traceable LLM assessment outputs.",
            r"Separated semantic understanding from deterministic business rules so ambiguous or high-risk cases could be logged, reviewed, and handled through safe fallbacks instead of prompt-only decisions.",
        ),
    ),
    "seaweed_backend": Project(
        "Seaweed Contest Platform",
        "Go, PostgreSQL, Redis, Judge0, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built backend services for registration, code submissions, sandboxed Judge0 execution, scoring, and live contest rankings across \textbf{500+ concurrent users}.",
            r"Designed async Go dispatch, verdict polling, PostgreSQL result schemas, Redis-backed runtime state, and Docker/Kubernetes deployment on AWS, reaching \textbf{sub-5s P95 verdict latency}.",
        ),
    ),
    "seaweed_platform": Project(
        "Seaweed Contest Platform",
        "Go, PostgreSQL, Redis, Judge0, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built a backend-heavy contest platform with async judging, score calculation, live rankings, runtime state, and deployment paths across Docker/Kubernetes on AWS.",
            r"Modeled durable users/submissions/results in PostgreSQL and used Redis for low-latency contest state, keeping evaluation workflows responsive under concurrent contest load.",
        ),
    ),
    "postificus_automation": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built Go/Echo backend services for a content distribution platform using browser automation, REST APIs, RabbitMQ workers, Redis autosave, and PostgreSQL persistence.",
            r"Added retries, DLQs, circuit-breaker isolation, health checks, and Prometheus metrics so unreliable external browser/API workflows stayed recoverable across distributed workers.",
        ),
    ),
    "postificus_scraping": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built browser-automation workers around dynamic third-party publishing flows where sessions, page timing, external UI changes, and partial failures had to be handled explicitly.",
            r"Designed queue-backed execution with Redis/PostgreSQL state, retries, DLQs, circuit breakers, and failure telemetry to make automation bugs inspectable and recoverable.",
        ),
    ),
    "murdoc_security": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Built a self-hosted \textbf{AI security gateway} for LLM, HTTP-tool, and MCP traffic with route profiles, request scoring, runtime policy checks, and allow/block decisions before downstream execution.",
            r"Added RBAC runtime settings, PII redaction, audit logs, attack-lab validation, OpenTelemetry traces, Prometheus metrics, and health checks for policy and failure visibility.",
        ),
    ),
    "murdoc_observability": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Instrumented an AI gateway with OpenTelemetry traces, Prometheus metrics, route profiles, health checks, and audit records tying model/tool requests to policy outcomes.",
            r"Built replayable decision records for prompt, tool, retrieval, and output layers so high-risk AI behavior could be correlated with request context and failure modes.",
        ),
    ),
    "penny_agents": Project(
        "Penny Lane Capital",
        "Python, Agno, Pydantic, SQLite, yfinance, JSONL",
        "",
        (
            r"Built an Agno workflow with analyst roles, bull/bear debate, trader, risk review, portfolio approval, typed Pydantic state, SQLite checkpoints, decision memory, and JSONL traces.",
            r"Evaluated agent decisions with historical-market backtests, reward loops, validation harnesses, and baseline comparisons, keeping reasoning and state transitions inspectable.",
        ),
    ),
    "penny_memory": Project(
        "Penny Lane Capital",
        "Python, Agno, Pydantic, SQLite, yfinance, JSONL",
        "",
        (
            r"Built a multi-agent research workflow with role-specific analysts, debate, risk review, portfolio approval, checkpointed state, and decision memory for repeated market windows.",
            r"Added replayable traces, validation harnesses, and scorecards so agent behavior, memory use, and decision quality could be inspected instead of treated as a black box.",
        ),
    ),
}


EXPERIENCE = {
    "ai_backend": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js workflow} for MCA filings with session handling, CAPTCHA handoff, retries, and state recovery, reducing manual filing time by \textbf{85\%}.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized backend services with Docker, wired GitHub Actions deployments to Google Cloud Run, and improved release velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python medical-image segmentation tooling for \textbf{95 brain subparts}, handling preprocessing, orientation correction, model inference, generated masks, and large-volume data paths.",
            r"Reduced segmentation runtime by \textbf{87\%} using asynchronous and parallel execution while preserving inspection workflows for generated masks and 3D surfaces.",
            r"Debugged complex pipeline issues across conformation, orientation, label mapping, PyTorch/ONNX-style inference, and binary mask generation in a mature open-source codebase.",
        ),
    },
    "backend_systems": {
        "bentham": (
            r"Built a resilient browser-automation backend for MCA filings with retries, session recovery, public-site API lookups, and state validation, reducing manual filing time by \textbf{85\%}.",
            r"Optimized an AI-assisted company-registration pipeline for name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across workflow preparation.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions}, integrating model inference, preprocessing, and visualization into an existing medical-imaging application.",
            r"Reduced processing time by \textbf{87\%} through async/parallel execution and fewer repeated passes across large medical volumes.",
            r"Contributed production-facing changes under open-source review constraints, compatibility concerns, and careful debugging across existing workflows.",
        ),
    },
    "platform_security": {
        "bentham": (
            r"Built containerized backend services and browser-automation workflows for MCA filings, adding retries, state recovery, CI/CD, and Google Cloud Run deployment paths.",
            r"Optimized an AI-assisted company-registration pipeline and operational workflow around public registry lookups, generated drafts, and filing-state checks.",
            r"Improved release velocity by \textbf{70\%} by wiring Dockerized services to GitHub Actions and deployable cloud environments.",
        ),
        "gsoc": (
            r"Built medical-image segmentation tooling for \textbf{95 brain subparts} with reproducible preprocessing, inference, masks, and visualization outputs.",
            r"Reduced segmentation runtime by \textbf{87\%} while debugging correctness issues across large-volume data, generated masks, and 3D surface workflows.",
            r"Contributed patches across mature open-source workflows while preserving compatibility with existing user paths.",
        ),
    },
}


SKILLS = {
    "ai_backend": r"""\textbf{Languages}{: Python, Go, TypeScript, C++} \\
   \textbf{Frameworks}{: FastAPI, Gin, Echo, Node.js, Agno, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, Kubernetes, AWS, GCP, OpenTelemetry, Prometheus, Langfuse, GitHub Actions} \\""",
    "backend_systems": r"""\textbf{Languages}{: Go, Python, TypeScript, C++} \\
   \textbf{Frameworks}{: Echo, FastAPI, Gin, Node.js} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, AWS, GCP, Prometheus, OpenTelemetry, GitHub Actions} \\""",
    "platform_security": r"""\textbf{Languages}{: Go, Python, TypeScript, C++} \\
   \textbf{Frameworks}{: FastAPI, Echo, Gin, Node.js} \\
   \textbf{Tools}{: Kubernetes, Docker, PostgreSQL, Redis, OpenTelemetry, Prometheus, MCP, GitHub Actions, AWS, GCP} \\""",
}


RESUMES = [
    Resume(
        "neosapien",
        "NeoSapien",
        "Backend Intern",
        "Strong",
        "LinkedIn post within last month",
        "conversation-intelligence backend, event-driven APIs, memory/context, production debugging",
        "ai_backend",
        ("swish_ai_backend", "seaweed_backend", "postificus_automation"),
        SKILLS["ai_backend"],
        "Strong fit. Swish maps directly to conversation understanding and memory; Seaweed/Postificus support backend scale and async execution.",
    ),
    Resume(
        "sarvam_inference",
        "Sarvam",
        "Backend Intern - Inference Pipelines & Diagnostics",
        "Strong",
        "Sarvam careers, crawled within last week",
        "LLM inference services, diagnostics APIs, observability, routing, backend data pipelines",
        "ai_backend",
        ("swish_ai_backend", "murdoc_observability", "seaweed_backend"),
        SKILLS["ai_backend"],
        "Strong fit for backend/inference infra. Resume should not claim model training depth; it focuses on APIs, diagnostics, observability, and GSoC inference optimization.",
    ),
    Resume(
        "sarvam_on_device",
        "Sarvam",
        "Backend Intern - On Device AI",
        "Good",
        "Sarvam careers/Indeed, crawled today",
        "backend APIs, LLM API integrations, SQL/NoSQL, cloud, data pipelines for AI products",
        "ai_backend",
        ("swish_ai_backend", "penny_memory", "seaweed_backend"),
        SKILLS["ai_backend"],
        "Good fit for backend AI product work. Slight gap: no dedicated on-device/edge deployment project yet.",
    ),
    Resume(
        "enterpret",
        "Enterpret",
        "Software Engineer Intern",
        "Strong",
        "Greenhouse/Wellfound, reposted/crawled within last week",
        "AI-native customer feedback infrastructure, backend scale, AWS/serverless, distributed systems",
        "backend_systems",
        ("swish_ai_backend", "seaweed_platform", "postificus_automation"),
        SKILLS["backend_systems"],
        "Strong fit. Prior internship, backend systems, AI-assisted workflows, and debugging-heavy projects match the listing.",
    ),
    Resume(
        "cloudflare",
        "Cloudflare",
        "Software Engineer Intern - Bengaluru",
        "Good but high-bar",
        "Official careers/Greenhouse, crawled within last week",
        "Internet-scale systems, Go/Rust/C++/Python, security, reliability, developer platform",
        "platform_security",
        ("seaweed_platform", "murdoc_security", "postificus_automation"),
        SKILLS["platform_security"],
        "Good but high-bar. Resume has systems/open-source/backend signal, but lacks direct Internet-scale networking experience.",
    ),
    Resume(
        "cloudsek_backend_intern",
        "CloudSEK",
        "SDE - Backend - Intern",
        "Strong",
        "Official Greenhouse, crawled within last week",
        "cybersecurity backend, NodeJS/Go, APIs, SQL, Docker/Kubernetes, cloud/security products",
        "platform_security",
        ("murdoc_security", "postificus_automation", "seaweed_backend"),
        SKILLS["platform_security"],
        "Strong fit. Murdoc maps to security/backend; Postificus and Seaweed show Go services, state, workers, and deployment.",
    ),
    Resume(
        "anakin",
        "Anakin",
        "Software Engineering Intern - Backend / Systems / Scraping Infrastructure",
        "Strong",
        "Wellfound, posted within last month",
        "backend systems, scraping/web automation infra, debugging, reliability, data pipelines",
        "backend_systems",
        ("postificus_scraping", "seaweed_backend", "murdoc_observability"),
        SKILLS["backend_systems"],
        "Very strong fit. Postificus is directly relevant to browser automation, unreliable external flows, retries, and debugging.",
    ),
    Resume(
        "nirmata",
        "Nirmata",
        "Software Engineer Intern, India",
        "Strong",
        "Official Greenhouse, crawled yesterday",
        "cloud-native microservices, Kubernetes, Docker, Prometheus, Kyverno, observability",
        "platform_security",
        ("seaweed_platform", "murdoc_observability", "postificus_automation"),
        SKILLS["platform_security"],
        "Strong fit. Add Kyverno OSS contribution in outreach; resume already has Kubernetes/Docker/Prometheus/OpenTelemetry signal.",
    ),
    Resume(
        "skyclad",
        "Skyclad Ventures",
        "AI Engineering Intern",
        "Good",
        "Wellfound, posted today/recently active",
        "agentic workflows, retrieval pipelines, evaluation harnesses, production AI systems",
        "ai_backend",
        ("swish_agent_eval", "penny_memory", "murdoc_security"),
        SKILLS["ai_backend"],
        "Good fit for AI-product engineering. Gap: no standalone RAG/vector-store project in the top three, though Penny Lane memory helps.",
    ),
    Resume(
        "platformatory",
        "Platformatory",
        "Software Product Intern - Platform",
        "Medium",
        "Wellfound, crawled within last month",
        "Kafka private cloud, platform engineering, Go/Python, Kubernetes, Docker, APIs",
        "platform_security",
        ("seaweed_platform", "postificus_automation", "murdoc_observability"),
        SKILLS["platform_security"],
        "Medium fit. Strong Kubernetes/backend basis, but lacks direct Kafka/Helm project experience.",
    ),
    Resume(
        "prepairo",
        "PrepAiro",
        "Backend / Full Stack Intern - Python",
        "Good",
        "Wellfound, reposted yesterday",
        "Python/FastAPI backend, AI tutor, RAG/agentic frameworks, production applications",
        "ai_backend",
        ("swish_ai_backend", "seaweed_backend", "penny_memory"),
        SKILLS["ai_backend"],
        "Good fit for FastAPI + AI workflow backend. Gap: dedicated education/RAG project would make it stronger.",
    ),
    Resume(
        "sapiensu",
        "Sapiensu",
        "Software Engineer Intern",
        "Good",
        "LinkedIn, posted within last week",
        "AI-native risk intelligence, entity graphs, risk scoring, monitoring infra, AI integrations",
        "ai_backend",
        ("penny_memory", "swish_ai_backend", "seaweed_backend"),
        SKILLS["ai_backend"],
        "Good fit for AI integrations and backend systems. Gap: no explicit entity-graph/risk-intelligence project.",
    ),
    Resume(
        "starlly",
        "Starlly Solutions",
        "Product Engineering Intern",
        "Medium / lacks frontend depth",
        "Wellfound crawled today; posting older but recruiter active",
        "backend data modeling, FastAPI/Node APIs, PostgreSQL, operational analytics, LLM API usage",
        "backend_systems",
        ("postificus_automation", "swish_ai_backend", "seaweed_platform"),
        SKILLS["backend_systems"],
        "Medium fit. Backend/data workflow is relevant, but the listing wants stronger frontend and industrial-ops modeling depth; resume intentionally does not inflate frontend depth.",
    ),
    Resume(
        "aurva",
        "Aurva",
        "Software Engineering Intern",
        "Medium / security gap",
        "Wellfound, last-month search result",
        "data security, Go, Kubernetes, platform intern, observability/security systems",
        "platform_security",
        ("murdoc_security", "seaweed_platform", "postificus_automation"),
        SKILLS["platform_security"],
        "Medium fit. Security/backend/Kubernetes are relevant, but resume lacks eBPF or direct database-security telemetry.",
    ),
    Resume(
        "mercator",
        "Mercator",
        "Software Engineer Intern",
        "Good if eligible",
        "Ashby, crawled within last month",
        "AI/LLM workflows, backend and simulation infrastructure, supply-chain agents",
        "ai_backend",
        ("penny_memory", "swish_ai_backend", "seaweed_platform"),
        SKILLS["ai_backend"],
        "Good AI/backend fit, but US on-site and supply-chain simulation domain are constraints.",
    ),
    Resume(
        "espa_labs",
        "Espa Labs",
        "Software Engineer Intern",
        "Good if eligible",
        "Ashby, crawled within last month",
        "agentic AI assistant, backend infrastructure, productivity workflows, core services",
        "ai_backend",
        ("swish_agent_eval", "penny_memory", "postificus_automation"),
        SKILLS["ai_backend"],
        "Good AI-product/backend fit. Gap: no direct calendar/email assistant project.",
    ),
    Resume(
        "taktile",
        "Taktile",
        "Software Engineer Intern",
        "Good if eligible",
        "Ashby, crawled within last month",
        "Python/FastAPI backend, AWS serverless, automated decisioning, distributed systems",
        "backend_systems",
        ("seaweed_platform", "swish_ai_backend", "postificus_automation"),
        SKILLS["backend_systems"],
        "Good backend/distributed-systems fit; location is Europe hybrid.",
    ),
    Resume(
        "simular",
        "Simular",
        "Software Engineer Intern",
        "Good if eligible",
        "Ashby/Simplify, crawled within last month",
        "AI agents, backend/product features, automation, deployment scripts",
        "ai_backend",
        ("postificus_scraping", "swish_agent_eval", "penny_memory"),
        SKILLS["ai_backend"],
        "Good fit for agents and automation. Gap: no direct on-device agent project.",
    ),
    Resume(
        "root_access",
        "Root Access",
        "Software Engineer Intern",
        "Good if eligible",
        "Ashby, crawled within last month",
        "developer tooling, build automation, backend apps, AI-powered engineering workflows",
        "backend_systems",
        ("seaweed_backend", "postificus_automation", "murdoc_observability"),
        SKILLS["backend_systems"],
        "Good devtools/backend fit. Gap: no dedicated CLI/build-system project.",
    ),
    Resume(
        "phonely",
        "Phonely",
        "Software Engineer Intern",
        "Good if eligible",
        "Ashby, crawled yesterday",
        "AI voice systems, debugging customer issues, backend tooling, monitoring workflows",
        "ai_backend",
        ("swish_agent_eval", "postificus_automation", "murdoc_observability"),
        SKILLS["ai_backend"],
        "Good AI-ops/debugging fit. Gap: no direct realtime voice/audio project.",
    ),
    Resume(
        "readily",
        "Readily",
        "Full-Stack Engineering Intern",
        "Medium / lacks frontend depth",
        "YC, crawled within last week",
        "healthcare compliance AI, backend APIs, AI integrations, Postgres, product ownership",
        "ai_backend",
        ("swish_ai_backend", "seaweed_backend", "penny_memory"),
        SKILLS["ai_backend"],
        "Medium fit. GSoC healthcare context helps, but the listing wants stronger frontend depth and healthcare compliance domain context.",
    ),
    Resume(
        "cekura",
        "Cekura",
        "AI Engineer Intern",
        "Strong if eligible",
        "YC/job boards, crawled within last month",
        "conversational-agent testing, evaluation, monitoring, LLM/voice/chat reliability",
        "ai_backend",
        ("swish_agent_eval", "murdoc_observability", "penny_memory"),
        SKILLS["ai_backend"],
        "Strong conceptual fit. Swish maps well to conversational AI evaluation and tracing; gap is no direct voice-agent testing project.",
    ),
    Resume(
        "paragon",
        "Paragon",
        "Forward Deployed Engineer Intern",
        "Good if eligible",
        "YC, crawled within last month",
        "industrial AI agents, customer workflows, integrations, evals, production code",
        "ai_backend",
        ("swish_ai_backend", "penny_memory", "postificus_automation"),
        SKILLS["ai_backend"],
        "Good builder/FDE fit. Gap: no industrial-sales/RFQ workflow domain project.",
    ),
    Resume(
        "ironclad",
        "Ironclad",
        "Software Engineer Intern",
        "Medium if eligible",
        "Ashby, crawled within last month",
        "AI contracting workflows, product/backend/platform teams, workflow systems",
        "backend_systems",
        ("swish_ai_backend", "postificus_automation", "seaweed_backend"),
        SKILLS["backend_systems"],
        "Medium fit. Workflow/backend skills are relevant, but no contract/legal domain project.",
    ),
    Resume(
        "tenex_ai",
        "TENEX.AI",
        "Software Engineer Intern",
        "Medium if eligible",
        "Ashby, crawled within last week",
        "AI-native MDR, backend APIs, cybersecurity automation, full-stack debugging",
        "platform_security",
        ("murdoc_security", "postificus_automation", "seaweed_backend"),
        SKILLS["platform_security"],
        "Medium fit. Security/backend is relevant, but the listing expects broader full-stack comfort and is US on-site.",
    ),
]


PREAMBLE = r"""% Generated recent-intern resume. Source: tools/generate_recent_intern_resumes.py
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
\newcommand{\resumeItem}[1]{\item\small{{#1 \vspace{-2pt}}}}
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
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
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
\textit{{Backend Engineering Intern: Go, Node.js, Docker, GCP, Puppeteer, GitHub Actions}} & \textit{{Remote}} \\
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
\resumeItem{{Contributed patches across Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, working inside maintainer review processes for reliability, security, and integration quality.}}
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
        "# Last-30-Day Internship Resume Fit Report",
        "",
        "Generated by `tools/generate_recent_intern_resumes.py`.",
        "",
        "| Company | Role | Fit | Resume PDF | Source | Gap / caution |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for resume in RESUMES:
        rows.append(
            f"| {resume.company} | {resume.role} | {resume.fit} | "
            f"`{resume.slug}_resume.pdf` | {resume.source} | {resume.gap_note} |"
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
