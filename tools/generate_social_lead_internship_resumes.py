from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

import generate_email_lead_internship_resumes as email_batch
import generate_next_internship_resumes as next_batch
import generate_selected_internship_resumes as base


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "social_leads_2026_05_26"


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
PROJECTS.update(next_batch.PROJECTS)
PROJECTS.update(email_batch.PROJECTS)
PROJECTS.update(
    {
        "hyoka_agent_ops": base.Project(
            "Hyoka",
            "Python, FastAPI, PostgreSQL, OpenTelemetry, SQLAlchemy, Typer, Docker",
            "",
            (
                r"Built an \textbf{AI-agent reliability control plane} with SDK/proxy/OTLP trace ingestion, evaluator registries, replay modes, failure mining, validation runs, release gates, promotions, and audit logs.",
                r"Implemented worker-owned leases, content-addressed artifacts, signed manifests, project API keys, SQLAlchemy/Alembic models, and reproducible runs around immutable inputs.",
            ),
        ),
        "hyoka_backend_platform": base.Project(
            "Hyoka",
            "Python, FastAPI, PostgreSQL, SQLite, SQLAlchemy, OpenTelemetry, Docker",
            "",
            (
                r"Built a \textbf{Python/FastAPI backend platform} for \textbf{trace ingestion}, \textbf{eval/replay workers}, validation runs, \textbf{release gates}, promotion state, and \textbf{audit logs}.",
                r"Implemented \textbf{SQLAlchemy/Alembic} models, \textbf{PostgreSQL/SQLite} storage paths, project API keys, \textbf{worker leases}, signed manifests, and reproducible runs around immutable inputs.",
            ),
        ),
        "hyoka_platform_dashboard": base.Project(
            "Hyoka",
            "Python, FastAPI, PostgreSQL, Next.js, TypeScript, OpenTelemetry, Docker",
            "",
            (
                r"Built backend and dashboard paths for operating agent behavior, including trace ingestion, suites, candidates, validation runs, promotion state, audit history, and gate decisions.",
                r"Designed project-scoped API keys, worker leases, signed manifests, JSON schema checks, replay artifacts, and containerized Postgres-backed services.",
            ),
        ),
        "omni_speech_loop": base.Project(
            "Omni-SSM Voice Agent",
            "Python, PyTorch, ONNX Runtime, Sherpa-ONNX, Moonshine, Piper",
            "",
            (
                r"Built a supporting \textbf{speech/AI engineering project} with STT/TTS experiments, Moonshine Hindi ASR tuning, ONNX Runtime, Sherpa-ONNX, Piper TTS, and provider-profile checks.",
                r"Tracked WER, first-audio latency, memory usage, manifest-driven datasets, and partial fine-tuning runs so model behavior stayed measurable and debuggable.",
            ),
        ),
        "swish_policy_ai": base.Project(
            "Swish Support System",
            "Python, FastAPI, React, PostgreSQL/pgvector, Redis, Langfuse",
            base.href("https://github.com/unichronic/swishagent"),
            (
                r"Built a hybrid AI + rules support workflow where LLM assessments classify ambiguous complaints while deterministic policy code controls refunds, replacements, coupons, and escalations.",
                r"Grounded responses in order, item, evidence, customer, and policy context with pgvector retrieval, Redis state, Langfuse traces, confidence thresholds, and regression cases.",
            ),
        ),
        "swish_backend_platform": base.Project(
            "Swish Support System",
            "Python, FastAPI, PostgreSQL/pgvector, Redis, Langfuse",
            base.href("https://github.com/unichronic/swishagent"),
            (
                r"Built \textbf{Python backend workflows} around \textbf{PostgreSQL/pgvector}, \textbf{Redis} state, case lifecycles, confidence thresholds, and \textbf{deterministic policy execution}.",
                r"Added \textbf{Langfuse traces}, \textbf{regression cases}, grounded context checks, and \textbf{failure-path handling} so multi-turn behavior stayed inspectable and repeatable.",
            ),
        ),
        "seaweed_ownership": base.Project(
            "Seaweed: Contest Platform",
            "TypeScript, React, Next.js, Go, PostgreSQL, Judge0, Firebase, Docker",
            base.href("https://github.com/unichronic/seaweed-fe"),
            (
                r"Built an end-to-end assessment product with auth-gated problem pages, code editor, submissions, admin review, shortlisting, live rankings, and reproducible judging records.",
                r"Implemented Go judging APIs with Judge0, PostgreSQL rankings/materialized views, Redis-backed runtime state, and Docker/Kubernetes deployment for \textbf{500+ concurrent users}.",
            ),
        ),
        "seaweed_platform": base.Project(
            "Seaweed: Contest Platform",
            "Go, TypeScript, React, PostgreSQL, Redis, Judge0, Docker, Kubernetes",
            base.href("https://github.com/unichronic/seaweed-fe"),
            (
                r"Built product and platform paths for registration, submissions, sandboxed code execution, admin review, live rankings, and durable result records across contest traffic.",
                r"Designed async verdict polling, PostgreSQL result schemas, Redis-backed runtime state, Docker/Kubernetes deployment, and \textbf{sub-5s P95 verdict latency}.",
            ),
        ),
        "postificus_workflows": base.Project(
            "Postificus",
            "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
            base.href("https://github.com/unichronic/postificus"),
            (
                r"Built browser-automation-backed product workflows with REST APIs, RabbitMQ workers, Redis autosave, PostgreSQL persistence, durable job status, and recoverable publishing tasks.",
                r"Added retries, DLQs, circuit-breaker isolation, health checks, and Prometheus metrics so long-running API/browser workflows stayed observable and fault-tolerant.",
            ),
        ),
        "penny_financial_agents": base.Project(
            "Penny Lane Capital",
            "Python, Agno, Pydantic, SQLite, Vector Memory, yfinance, JSONL",
            base.href("https://github.com/unichronic/pennylane"),
            (
                r"Built a Python multi-agent research workflow with analyst roles, bull/bear debate, trader, risk review, portfolio approval, typed state, checkpoints, and replayable JSONL traces.",
                r"Evaluated decisions with historical-market backtests, reward-loop scorecards, semantic lesson retrieval, and return, drawdown, win-rate, and risk signals.",
            ),
        ),
    }
)


EXPERIENCE = {
    "oss_builder": {
        "bentham": (
            r"Owned product-facing automation features in a small team, turning ambiguous MCA filing steps into reliable Node.js/Puppeteer workflows with operator checkpoints.",
            r"Built backend validation, retries, public-site API lookups, and recoverable session state, reducing manual filing time by \textbf{85\%}.",
            r"Shipped Dockerized services on Google Cloud Run with GitHub Actions releases, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Contributed production-grade Python features inside a mature open-source application, coordinating model outputs, UI paths, generated artifacts, and user inspection workflows.",
            r"Reduced expensive image-processing runtime by \textbf{87\%} through async/parallel execution while preserving correctness on large data paths.",
            r"Worked through unfamiliar code quickly across VTK, wxPython, NumPy, PyTorch/ONNX-adjacent inference, and label-mapping logic.",
        ),
    },
    "banking_core": {
        "bentham": (
            r"Built regulated-workflow automation around company-registration filings, combining structured backend state, public-site API lookups, operator review, retries, and browser execution.",
            r"Reduced manual filing time by \textbf{85\%} by hardening multi-step workflows with session recovery, state validation, and failure-aware execution.",
            r"Packaged and deployed services with Docker, Google Cloud Run, and GitHub Actions so releases stayed repeatable under fast iteration.",
        ),
        "gsoc": (
            r"Built Python tooling in a mature open-source codebase, integrating preprocessing, model execution, generated masks, large data paths, and inspection flows.",
            r"Reduced runtime by \textbf{87\%} using asynchronous and parallel execution over expensive NumPy/PyTorch-style workflows.",
            r"Debugged cross-module issues across UI, data transformation, generated artifacts, label mapping, and model-output handling.",
        ),
    },
    "agent_infra": {
        "bentham": (
            r"Built an AI-assisted workflow for structured filing drafts, combining prompt outputs, operator validation, public-site API lookups, retries, and automation handoff.",
            r"Implemented async backend execution with browser automation, session recovery, state validation, and failure-aware retries, reducing manual effort by \textbf{85\%}.",
            r"Containerized services with Docker, deployed to Google Cloud Run, and automated releases through GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python medical-image segmentation tooling across \textbf{95 brain subparts}, covering preprocessing, orientation correction, model inference, generated masks, and large MRI data paths.",
            r"Reduced segmentation runtime by \textbf{87\%} using asynchronous and parallel execution while preserving inspection workflows for generated masks and 3D surfaces.",
            r"Debugged model-output pipeline issues across conformation, label mapping, PyTorch/ONNX-style inference, and binary mask generation inside a mature codebase.",
        ),
    },
    "medical_robotics": {
        "bentham": (
            r"Built production automation that connected Node.js services, browser workflows, API lookups, operator validation, Docker, Cloud Run, and GitHub Actions.",
            r"Handled unreliable external workflows with retries, session recovery, state validation, and visible checkpoints, reducing manual filing time by \textbf{85\%}.",
            r"Worked close to product constraints where generated drafts had to remain inspectable before downstream automation executed.",
        ),
        "gsoc": (
            r"Built scientific Python tooling for MRI segmentation across \textbf{95 anatomical regions}, handling preprocessing, orientation correction, model inference, masks, and 3D visualization.",
            r"Reduced runtime by \textbf{87\%} using asynchronous and parallel execution over large medical-image volumes while preserving inspectable outputs.",
            r"Debugged data/model-output issues inside a mature medical-imaging app across VTK, wxPython, NumPy, PyTorch, and ONNX-adjacent paths.",
        ),
    },
    "diagnostics_ai": {
        "bentham": (
            r"Built production workflow software with API lookups, browser automation, validation checkpoints, retry handling, and human-reviewable state for high-friction filings.",
            r"Reduced manual filing time by \textbf{85\%} by turning repeated operational steps into recoverable backend workflows.",
            r"Used Docker, Google Cloud Run, and GitHub Actions to keep service deployment and iteration predictable.",
        ),
        "gsoc": (
            r"Integrated Python model-output workflows into medical-imaging tooling, covering preprocessing, segmentation masks, label mapping, large MRI volumes, and visual inspection.",
            r"Reduced runtime by \textbf{87\%} through asynchronous and parallel execution while keeping outputs traceable through generated masks and 3D surfaces.",
            r"Worked through correctness issues across NumPy data handling, PyTorch/ONNX-style inference, VTK rendering paths, and wxPython UI integration.",
        ),
    },
    "speech_product": {
        "bentham": (
            r"Built AI-assisted product workflows where generated drafts were validated, corrected, and carried into deterministic automation instead of being treated as opaque model output.",
            r"Added retries, state validation, session recovery, and operator checkpoints around unreliable browser/API flows, reducing manual effort by \textbf{85\%}.",
            r"Shipped Dockerized services through Google Cloud Run and GitHub Actions, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python inference tooling in a mature open-source app, connecting preprocessing, model execution, generated outputs, and user-facing inspection flows.",
            r"Reduced runtime by \textbf{87\%} with async/parallel execution over large input data while preserving output correctness.",
            r"Debugged integration problems across model outputs, array transforms, UI rendering, and performance-sensitive processing paths.",
        ),
    },
    "backend_platform": {
        "bentham": (
            r"Built production \textbf{backend automation} with Node.js services, public-site API lookups, browser execution, \textbf{retries}, \textbf{session recovery}, and \textbf{state validation}.",
            r"Kept long-running workflows \textbf{recoverable and inspectable}, reducing manual filing time by \textbf{85\%} across high-friction operational steps.",
            r"Shipped \textbf{Dockerized services} through \textbf{Google Cloud Run} and \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built \textbf{Python tooling} inside a mature open-source application, working across large data paths, generated artifacts, model outputs, and user-facing inspection workflows.",
            r"Reduced runtime by \textbf{87\%} with \textbf{async/parallel execution} and debugged correctness issues across NumPy, PyTorch/ONNX-style outputs, label mapping, and UI integration.",
            r"Adapted changes to existing architecture, maintainer feedback, and reliability constraints rather than treating the codebase as a greenfield project.",
        ),
    },
    "ai_product": {
        "bentham": (
            r"Built data-backed automation flows that combined generated drafts, public-site API lookups, validation, retries, and operator review before execution.",
            r"Reduced manual filing time by \textbf{85\%} through backend state checks, failure recovery, and repeatable browser automation.",
            r"Deployed Dockerized services through Google Cloud Run and GitHub Actions, improving iteration speed by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python ML tooling for MRI segmentation across \textbf{95 anatomical regions}, covering preprocessing, inference integration, generated masks, and large-array data paths.",
            r"Reduced runtime by \textbf{87\%} using asynchronous and parallel execution over expensive NumPy/PyTorch-style workflows.",
            r"Validated model outputs through inspectable masks and 3D surfaces while debugging label mapping and data-orientation issues.",
        ),
    },
    "cloudops": {
        "bentham": (
            r"Containerized automation services with Docker, deployed on Google Cloud Run, and wired GitHub Actions releases for repeatable production updates.",
            r"Built recoverable service execution around retries, state validation, session recovery, public-site API lookups, and operator-visible failure states.",
            r"Improved deployment velocity by \textbf{70\%} while reducing manual filing time by \textbf{85\%} through backend workflow automation.",
        ),
        "gsoc": (
            r"Reduced runtime by \textbf{87\%} using async/parallel execution over large medical-image processing paths in a mature Python application.",
            r"Debugged production-style issues across Linux development environments, large files, NumPy/PyTorch-style workloads, generated artifacts, and UI integration.",
            r"Adapted changes to existing project conventions while working through maintainer review and compatibility constraints.",
        ),
    },
    "enterprise_platform": {
        "bentham": (
            r"Built resilient backend automation for high-friction public-site workflows with retries, session recovery, API lookups, state validation, and operator checkpoints.",
            r"Reduced manual filing time by \textbf{85\%} and kept generated workflow state inspectable before execution.",
            r"Used Docker, Cloud Run, and GitHub Actions to keep releases repeatable and improve deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python features inside a mature open-source application, integrating model outputs, generated artifacts, performance-sensitive processing, and UI inspection paths.",
            r"Cut runtime by \textbf{87\%} using async/parallel execution over large input data.",
            r"Worked through integration issues across VTK/wxPython UI code, NumPy data paths, PyTorch/ONNX-style inference, and label mapping.",
        ),
    },
}


OPEN_SOURCE = {
    "oss_heavy": (
        r"Contributed maintainer-reviewed patches across \textbf{Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant MCP Gateway}, including medical-imaging workflow fixes, parser robustness, Zip Slip path validation, and cloud-native reliability paths.",
    ),
    "agent_reliability": (
        r"Contributed to \textbf{Kuadrant MCP Gateway} backend-outage grace handling, \textbf{Kyverno} policy/infrastructure paths, and IOOS/Tiled data or visualization tooling under maintainer review.",
    ),
    "medical_scientific": (
        r"Contributed to research-adjacent open source including \textbf{Invesalius} medical-imaging workflows, \textbf{IOOS} scientific-data tooling, and \textbf{Tiled} visualization code, plus compatibility and security-validation fixes.",
    ),
    "systems_cloud": (
        r"Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway} and \textbf{Kyverno}, plus CRIU, VideoLAN, Tiled, IOOS, and Invesalius, spanning backend integration behavior, parser robustness, security validation, and compatibility fixes.",
    ),
}


SKILLS = {
    "fullstack_startup": r"""\textbf{Languages}{: TypeScript, JavaScript, Python, Go, SQL} \\
   \textbf{Frameworks}{: React, Next.js, Node.js, FastAPI, Echo, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, GCP, AWS, GitHub Actions, OpenTelemetry, Prometheus} \\""",
    "agent_ai": r"""\textbf{Languages}{: Python, TypeScript, Go, SQL, JavaScript} \\
   \textbf{Frameworks}{: FastAPI, React, Next.js, Node.js, Agno, PyTorch, ONNX Runtime} \\
   \textbf{Tools}{: PostgreSQL/pgvector, Redis, SQLite, Vector Memory, Docker, GCP, GitHub Actions, OpenTelemetry, Langfuse, JSONL} \\""",
    "medical_robotics": r"""\textbf{Languages}{: Python, TypeScript, Go, SQL, C++} \\
   \textbf{Frameworks}{: PyTorch, FastAPI, React, Next.js, VTK, wxPython, Echo} \\
   \textbf{Tools}{: NumPy, ONNX, PostgreSQL, Redis, Docker, GCP, GitHub Actions, OpenTelemetry, Prometheus, Judge0} \\""",
    "speech_ai": r"""\textbf{Languages}{: Python, TypeScript, JavaScript, Go, SQL} \\
   \textbf{Frameworks}{: PyTorch, FastAPI, React, Next.js, Node.js, ONNX Runtime} \\
   \textbf{Tools}{: Sherpa-ONNX, PostgreSQL/pgvector, Redis, Docker, GCP, GitHub Actions, OpenTelemetry, Langfuse, JSONL} \\""",
    "backend_platform": r"""\textbf{Languages}{: Python, SQL, TypeScript, JavaScript, Go} \\
   \textbf{Frameworks}{: FastAPI, SQLAlchemy, React, Next.js, Node.js, PyTorch, ONNX Runtime} \\
   \textbf{Tools}{: PostgreSQL/pgvector, SQLite, Redis, Docker, Kubernetes, GCP, GitHub Actions, OpenTelemetry, Langfuse, Judge0} \\""",
    "cloudops": r"""\textbf{Languages}{: Python, Go, TypeScript, SQL, Shell} \\
   \textbf{Frameworks}{: FastAPI, Echo, Node.js, React, Next.js} \\
   \textbf{Tools}{: Linux, Docker, Kubernetes, AWS, GCP, PostgreSQL, Redis, RabbitMQ, GitHub Actions, OpenTelemetry, Prometheus} \\""",
    "enterprise": r"""\textbf{Languages}{: Go, Python, TypeScript, JavaScript, SQL} \\
   \textbf{Frameworks}{: FastAPI, Echo, React, Next.js, Node.js, PyTorch} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, Kubernetes, AWS, GCP, GitHub Actions, OpenTelemetry, Prometheus, Judge0} \\""",
}


RESUMES = [
    Resume(
        "monsoon_tech_intern_resume",
        "Monsoon",
        "Tech Intern",
        "real open-source contributions, fast end-to-end ownership, Hyderabad in-office, shipped code",
        "oss_builder",
        "oss_heavy",
        ("seaweed_ownership", "postificus_workflows", "hyoka_platform_dashboard"),
        SKILLS["fullstack_startup"],
        "https://www.linkedin.com/posts/charann06_tech-intern-at-monsoon-hyderabad-summer-share-7463351262588153856-7oFs",
        "High fit technically because the post explicitly values real OSS and end-to-end ownership. Location is the gating issue: daily Hyderabad in-office.",
    ),
    Resume(
        "banking_stack_tech_intern_resume",
        "Banking Stack",
        "Tech Intern",
        "Bengaluru WFO, 6+ months, banking-stack product, delivered projects, non-vibe-coded engineering",
        "banking_core",
        "systems_cloud",
        ("seaweed_platform", "postificus_workflows", "penny_financial_agents"),
        SKILLS["enterprise"],
        "https://www.linkedin.com/posts/abhijit-das-s_techinternship-internship-ai-share-7463605089983770624-aBJP",
        "Strong if 6 months WFO in Bengaluru is feasible. Lead with shipped systems and financial/domain-adjacent workflow work.",
    ),
    Resume(
        "metronis_foundation_intern_resume",
        "Metronis",
        "Foundation Team Intern",
        "applied ML, backend + infra, eval/training/memory infrastructure for AI agents, remote high-intensity",
        "agent_infra",
        "agent_reliability",
        ("hyoka_agent_ops", "swish_policy_ai", "penny_financial_agents"),
        SKILLS["agent_ai"],
        "mailto:arnav@metronis.space",
        "Very strong fit. Hyoka maps directly to Aegis eval/training/memory infrastructure and should lead the email.",
    ),
    Resume(
        "morphle_software_engineer_intern_resume",
        "Morphle Labs",
        "Software Engineer Intern",
        "AI + robotics, medical imaging, cloud/web projects, low-level/systems thinking, Bangalore",
        "medical_robotics",
        "medical_scientific",
        ("seaweed_platform", "postificus_workflows", "hyoka_platform_dashboard"),
        SKILLS["medical_robotics"],
        "mailto:shrinidhi.jade@morphle.in",
        "Very strong domain fit because of GSoC medical imaging plus shipped web/cloud systems. Mention immediate Bangalore availability clearly.",
    ),
    Resume(
        "sigtuple_software_engineer_intern_resume",
        "SigTuple Technologies",
        "Software Engineer Intern",
        "AI + robotics healthcare diagnostics, Bangalore WFO, 6-month internship, PPO track",
        "diagnostics_ai",
        "medical_scientific",
        ("hyoka_agent_ops", "seaweed_platform", "swish_policy_ai"),
        SKILLS["medical_robotics"],
        "mailto:teamhr@sigtuple.com",
        "Very strong domain fit. GSoC medical imaging and AI/model-output debugging are the clearest hooks.",
    ),
    Resume(
        "binary_ai_intern_resume",
        "Binary form lead",
        "AI Intern",
        "HSR Layout in-office Monday-Saturday, immediate joining, AI product engineering",
        "ai_product",
        "agent_reliability",
        ("hyoka_agent_ops", "swish_policy_ai", "penny_financial_agents"),
        SKILLS["agent_ai"],
        "https://binary.so/em2PZRF",
        "Good AI fit if Monday-Saturday HSR Layout and immediate joining are acceptable. Company name is not visible on the form.",
    ),
    Resume(
        "omli_backend_platform_intern_resume",
        "Omli",
        "Backend / Platform Intern",
        "Python backend, databases, infra/debugging, systems reliability, with AI/ML support when needed",
        "backend_platform",
        "agent_reliability",
        ("hyoka_backend_platform", "seaweed_platform", "omni_speech_loop"),
        SKILLS["backend_platform"],
        "mailto:sidd@omli.in",
        "Excellent backend/platform fit. Lead with Python, databases, reliability/debugging, and keep speech/AI as a secondary supporting signal.",
    ),
    Resume(
        "navi_cloudops_engineer_resume",
        "Navi",
        "CloudOps Engineer - I",
        "AWS/cloud operations, Python/Shell, Linux/networking, Docker/Kubernetes, regulated fintech infra",
        "cloudops",
        "systems_cloud",
        ("postificus_workflows", "seaweed_platform", "hyoka_platform_dashboard"),
        SKILLS["cloudops"],
        "https://navi.turbohire.co/job/publicjobs/57a902de-8498-40b6-b95a-5d5144a825e9",
        "Moderate fit. Strong Docker/backend/reliability, but direct AWS/Terraform/networking depth is weaker than the JD.",
    ),
    Resume(
        "walmart_grad_intern_resume",
        "Walmart Global Tech",
        "Grad Intern - No Work Experience",
        "platform engineering, distributed systems, data platforms, open-source frameworks, Bangalore",
        "enterprise_platform",
        "systems_cloud",
        ("seaweed_platform", "postificus_workflows", "hyoka_platform_dashboard"),
        SKILLS["enterprise"],
        "https://walmart.wd5.myworkdayjobs.com/en-US/WalmartExternal/job/XMLNAME--IND--Grad-Intern---No-Work-Experience_R-2509924",
        "Moderate fit. The provided Workday page currently reports posting unavailable, so apply only if it opens in browser or via a fresh requisition.",
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
\textit{{Product Engineering Intern: Node.js, JavaScript, Go, Docker, GCP, GitHub Actions}} & \textit{{Remote}} \\
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
        "# Social Lead Internship Tailored Resumes",
        "",
        "Generated by `tools/generate_social_lead_internship_resumes.py`.",
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
