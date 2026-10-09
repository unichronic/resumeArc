from __future__ import annotations

import csv
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "early_startups_first8_2026_05_28"
TRACKER = ROOT / "early_startups_bengaluru_gurugram_2026-05-28.csv"


def esc(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def href(url: str, label: str = "GitHub") -> str:
    return rf"\bodyhref{{{url}}}{{{label}}}"


@dataclass(frozen=True)
class Project:
    title: str
    tech: str
    link: str
    bullets: tuple[str, ...]


@dataclass(frozen=True)
class ResumeConfig:
    role_hint: str
    bentham: tuple[str, ...]
    gsoc: tuple[str, ...]
    oss: str | tuple[str, ...]
    projects: tuple[str, str, str]
    skills: tuple[str, str, str]


P = {
    "hyoka_ai": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, Next.js, TypeScript, Docker",
        href("https://github.com/unichronic/hyoka"),
        (
            r"Built an \textbf{AI Reliability \& Evaluation Platform} with \textbf{trace/event ingestion}, \textbf{eval/replay workers}, release gates, promotions, API keys, \textbf{audit logs}, and a Next.js dashboard.",
            r"Modeled traces, suites, candidates, validation runs, \textbf{gate decisions}, artifacts, and manifests in \textbf{PostgreSQL/SQLite} using SQLAlchemy/Alembic, with \textbf{worker leases} for reproducible eval runs.",
        ),
    ),
    "hyoka_atlas": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, Next.js, TypeScript, Docker",
        href("https://github.com/unichronic/hyoka"),
        (
            r"Built an \textbf{AI Reliability \& Evaluation Platform} with \textbf{trace/event ingestion}, \textbf{eval/replay workers}, release gates, promotions, API keys, \textbf{audit logs}, and a Next.js dashboard.",
            r"Modeled traces, suites, candidates, validation runs, \textbf{gate decisions}, artifacts, and manifests in \textbf{PostgreSQL/SQLite} using SQLAlchemy/Alembic for reproducible AI workflow reviews.",
            r"Implemented \textbf{database-backed worker leases}, \textbf{content-addressed artifacts}, and an OpenAI-compatible proxy so generated outputs could be replayed, compared, and promoted through explicit gates.",
        ),
    ),
    "hyoka_agent": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, OpenTelemetry, Next.js, Docker",
        href("https://github.com/unichronic/hyoka"),
        (
            r"Built a framework-neutral \textbf{AI Reliability \& Evaluation Platform} that records \textbf{tool/model/retrieval traces}, runs \textbf{evals and replays}, mines failures, and gates safer configurations before promotion.",
            r"Implemented \textbf{OTLP/OpenInference-style ingestion}, an OpenAI-compatible proxy, evaluator registries, content-addressed artifacts, API keys, signed manifests, and \textbf{audit logs}.",
        ),
    ),
    "hyoka_bhindi": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, OpenTelemetry, Next.js, Docker",
        href("https://github.com/unichronic/hyoka"),
        (
            r"Built a framework-neutral \textbf{AI Reliability \& Evaluation Platform} that records tool/model/retrieval traces, runs evals and replays, mines failures, and gates safer configurations before promotion.",
            r"Designed \textbf{PostgreSQL/SQLite metadata models} for traces, suites, candidates, validation runs, gate decisions, artifacts, manifests, and project-scoped API keys.",
            r"Implemented \textbf{database-backed worker leases}, evaluator registries, OTLP/OpenInference-style ingestion, signed manifests, and audit logs so generated outputs stayed replayable and inspectable.",
        ),
    ),
    "hyoka_health": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, OpenTelemetry, Next.js, Docker",
        href("https://github.com/unichronic/hyoka"),
        (
            r"Built an \textbf{AI Reliability \& Evaluation Platform} for \textbf{traceable validation runs}, replayable runs, release gates, promotions, audit logs, and project-scoped API keys.",
            r"Designed \textbf{reproducible worker execution} with database leases, content-addressed artifacts, signed manifests, OTLP/OpenInference ingestion, and \textbf{Postgres-backed metadata}.",
        ),
    ),
    "hyoka_cent": Project(
        "Hyoka",
        "Python, FastAPI, PostgreSQL, SQLAlchemy, OpenTelemetry, Next.js, Docker",
        href("https://github.com/unichronic/hyoka"),
        (
            r"Built an \textbf{AI Reliability \& Evaluation Platform} for traceable validation runs, replayable runs, release gates, promotions, audit logs, and project-scoped API keys.",
            r"Designed \textbf{Postgres-backed metadata} for traces, suites, candidates, validation runs, gate decisions, artifacts, and manifests so AI outputs could be reproduced and inspected.",
            r"Implemented worker leases, content-addressed artifacts, signed manifests, and OTLP/OpenInference ingestion for long-running eval jobs and generated outputs.",
        ),
    ),
    "postificus_backend": Project(
        "Postificus",
        "Go, Echo, React, Vite, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built a \textbf{full-stack workflow app} with \textbf{REST APIs}, auth/settings endpoints, \textbf{PostgreSQL persistence}, Redis cache/autosave, RabbitMQ jobs, S3-compatible storage, and live publication status.",
            r"Added \textbf{retries, DLQs, circuit breakers}, health checks, and \textbf{Prometheus metrics} so long-running API/browser workflows stayed observable and recoverable under unreliable integrations.",
        ),
    ),
    "postificus_ops": Project(
        "Postificus",
        "Go, Echo, React, Vite, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built \textbf{queue-backed Go services} for fragmented external publishing workflows, combining \textbf{direct APIs} with browser-fallback execution when third-party platforms were inconsistent.",
            r"Used \textbf{RabbitMQ workers}, Redis state, PostgreSQL persistence, \textbf{DLQs, retries, circuit breakers}, and Prometheus health metrics to make failures inspectable and recoverable.",
        ),
    ),
    "postificus_atlas": Project(
        "Postificus",
        "Go, Echo, React, Vite, PostgreSQL, Redis, RabbitMQ, Docker, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built \textbf{workflow backend services} for fragmented external platforms, combining \textbf{direct APIs} with browser-fallback execution when third-party systems were inconsistent or incomplete.",
            r"Used \textbf{RabbitMQ workers}, Redis state, PostgreSQL persistence, \textbf{DLQs, retries, circuit breakers}, and Prometheus metrics to keep long-running jobs inspectable and recoverable.",
            r"Shipped a \textbf{React/Vite operations surface} for auth/settings, draft status, autosave, S3-compatible artifacts, and publication state so operators could inspect work before final execution.",
        ),
    ),
    "swish_ops": Project(
        "Swish Support System",
        "Python, Go, FastAPI, React, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built an \textbf{operational decision workflow} that pulls \textbf{order, kitchen, fleet, trust, and evidence context} into LLM assessment while deterministic policy controls refunds, coupons, and escalations.",
            r"Modeled support cases as \textbf{policy-bound workflow state}, including \textbf{evidence strength}, issue type, active item, trust score, desired resolution, and escalation path.",
        ),
    ),
    "swish_atlas": Project(
        "Swish Support System",
        "Python, Go, FastAPI, React, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built a \textbf{policy-grounded AI workflow} where LLM assessment reads operational context, but \textbf{deterministic services} decide the final refund, coupon, remake, or escalation action.",
            r"Modeled case state with \textbf{evidence strength}, issue type, active item, trust score, desired resolution, and escalation path so decisions were inspectable instead of prompt-only.",
        ),
    ),
    "swish_agent": Project(
        "Swish Support System",
        "Python, Go, FastAPI, React, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built a \textbf{policy-grounded AI support workflow} where LLM reasoning proposes actions, but deterministic services enforce refund, remake, coupon, trust, and escalation rules.",
            r"Carried \textbf{customer/order/evidence context} across turns and traced high-risk decisions with Langfuse/local logs so agent behavior stayed inspectable instead of prompt-only.",
        ),
    ),
    "seaweed": Project(
        "Seaweed Contest Platform",
        "Go, React, Vite, PostgreSQL, Redis, Judge0, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built a \textbf{full-stack contest platform} for \textbf{500+ concurrent users}, covering registration, problem pages, submissions, automated judging, admin review, and live ranked leaderboards.",
            r"Integrated \textbf{Judge0} with async Go dispatch, \textbf{PostgreSQL result schemas/materialized views}, Redis runtime state, and Docker/Kubernetes deployment, reaching \textbf{sub-5s P95 verdict latency}.",
        ),
    ),
    "penny": Project(
        "Penny Lane Capital",
        "Python, Pydantic, SQLite, Vector Memory, JSONL",
        "",
        (
            r"Built a \textbf{multi-agent research workflow} with analyst, debate, risk, and portfolio-style stages using typed \textbf{Pydantic state}, SQLite checkpoints, vector memory, and JSONL traces.",
            r"Added \textbf{semantic lesson retrieval} and validation harnesses so decisions could be replayed, compared, and inspected across changing market assumptions.",
        ),
    ),
}


SKILLS = {
    "ai": (
        "Python, TypeScript, JavaScript, Go",
        "FastAPI, Next.js, React, Node.js, SQLAlchemy, PyTorch",
        "PostgreSQL, SQLite, Redis, Docker, OpenTelemetry, Prometheus, Langfuse, GitHub Actions",
    ),
    "health": (
        "Python, TypeScript, Go, JavaScript",
        "PyTorch, FastAPI, Next.js, React, SQLAlchemy, VTK, wxPython",
        "ONNX, NumPy, PostgreSQL, Redis, Docker, OpenTelemetry, GitHub Actions",
    ),
    "backend": (
        "Go, Python, TypeScript, JavaScript",
        "Echo, FastAPI, React, Next.js, Node.js, SQLAlchemy",
        "PostgreSQL, Redis, RabbitMQ, Docker, Prometheus, GCP Cloud Run, GitHub Actions",
    ),
    "deeptech": (
        "Python, Go, TypeScript, JavaScript",
        "FastAPI, Echo, Next.js, React, SQLAlchemy, PyTorch",
        "PostgreSQL, Redis, RabbitMQ, Docker, Prometheus, OpenTelemetry, GitHub Actions",
    ),
}


BENTHAM_AI = (
    r"Built \textbf{backend automation} for compliance-sensitive MCA filings with browser execution, \textbf{public-site API lookups}, retries, \textbf{session recovery}, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
    r"Built an \textbf{AI-assisted draft-generation flow} with inspectable outputs before deterministic filing execution, then shipped Dockerized services on \textbf{Google Cloud Run} with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
)
BENTHAM_ATLAS = (
    r"Built \textbf{backend automation} for \textbf{legal/compliance filing workflows} with browser execution, public-site API lookups, retries, \textbf{session recovery}, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
    r"Implemented an \textbf{AI-assisted drafting flow} for company-name suggestions, object descriptions, and filing-field drafts, keeping generated outputs inspectable before \textbf{deterministic workflow execution}.",
    r"Shipped Dockerized Node.js/Go services on \textbf{Google Cloud Run} with \textbf{GitHub Actions} release workflows, improving deployment velocity by \textbf{70\%} for a regulated operations product.",
)
BENTHAM_BHINDI = (
    r"Built \textbf{backend automation} for compliance-sensitive MCA filing workflows with browser execution, public-site API lookups, retries, \textbf{session recovery}, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
    r"Implemented an \textbf{AI-assisted draft-generation flow} for company-name suggestions, object descriptions, and filing-field drafts, keeping generated outputs inspectable before deterministic execution.",
    r"Containerized Node.js/Go services with \textbf{Docker}, deployed them to \textbf{Google Cloud Run}, and automated releases with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
)
BENTHAM_BACKEND = (
    r"Built a resilient \textbf{Puppeteer/Node.js workflow engine} for MCA company-registration filings with retries, \textbf{session recovery}, API-backed checks, and operator checkpoints, reducing manual filing time by \textbf{85\%}.",
    r"Containerized \textbf{backend services} with \textbf{Docker}, deployed them to \textbf{Google Cloud Run}, and automated releases through \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
)

GSOC_AI = (
    r"Integrated a \textbf{FastSurfer CNN segmentation} feature for \textbf{95 anatomical brain regions}, wiring PyTorch/TorchScript, ONNX/TinyGrad inference, model selection, and device paths into Invesalius.",
    r"Built preprocessing/postprocessing for \textbf{NIfTI/MGZ MRI data}, including voxel conformation, \textbf{label remapping}, binary masks, QC checks, and an \textbf{87\%} runtime reduction with async/parallel execution.",
)
GSOC_CENT = (
    r"Integrated a \textbf{FastSurfer CNN segmentation} feature for \textbf{95 anatomical brain regions}, wiring PyTorch/TorchScript, ONNX/TinyGrad inference, plane-specific models, and device selection into Invesalius.",
    r"Built ML preprocessing/postprocessing for \textbf{NIfTI/MGZ MRI data}, including voxel conformation, thick-slice datasets, multi-view aggregation, sagittal label remapping, LUT mapping, and generated \textbf{binary masks}.",
    r"Reduced runtime by \textbf{87\%} using async/parallel execution while debugging \textbf{orientation, label correctness, GPU/CPU paths}, progress reporting, and 3D inspection flows.",
)
GSOC_SHORT = (
    r"Built \textbf{Python medical-imaging segmentation tooling} for \textbf{95 anatomical brain regions}, integrating model inference, preprocessing, generated masks, and 3D inspection workflows into Invesalius.",
    r"Reduced expensive MRI-processing runtime by \textbf{87\%} through async/parallel execution while debugging \textbf{orientation, label correctness}, and GPU/CPU execution paths.",
)


COMMON_OSS_AI = (
    r"Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway, Kyverno, Invesalius, Tiled, CRIU, and VideoLAN}, spanning backend failover behavior, security validation, parser robustness, and artifact correctness."
)
COMMON_OSS_HEALTH = (
    r"Contributed maintainer-reviewed patches across \textbf{Invesalius, IOOS, Tiled, VideoLAN, CRIU, Kyverno, and Kuadrant}, spanning medical/scientific data correctness, parser safety, compatibility fixes, and backend reliability."
)
COMMON_OSS_BACKEND = (
    r"Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway, Kyverno, CRIU, Invesalius, Tiled, and VideoLAN}, working inside mature codebases on reliability, security validation, and compatibility fixes."
)


CONFIGS: dict[str, ResumeConfig] = {
    "Atlas": ResumeConfig(
        "AI Backend / Product Engineering Intern",
        BENTHAM_ATLAS,
        GSOC_SHORT,
        COMMON_OSS_AI,
        ("hyoka_atlas", "postificus_atlas", "swish_atlas"),
        SKILLS["ai"],
    ),
    "Bhindi AI": ResumeConfig(
        "AI Engineer / Agent Reliability Intern",
        BENTHAM_BHINDI,
        GSOC_SHORT,
        COMMON_OSS_AI,
        ("hyoka_bhindi", "postificus_atlas", "swish_agent"),
        SKILLS["ai"],
    ),
    "Cent": ResumeConfig(
        "ML / Healthtech Backend Intern",
        BENTHAM_BACKEND,
        GSOC_CENT,
        COMMON_OSS_HEALTH,
        ("hyoka_cent", "swish_ops", "postificus_backend"),
        SKILLS["health"],
    ),
    "Maieutic Semiconductor": ResumeConfig(
        "AI Tooling / Backend Intern",
        BENTHAM_AI,
        GSOC_AI,
        COMMON_OSS_AI,
        ("hyoka_agent", "penny", "postificus_backend"),
        SKILLS["deeptech"],
    ),
    "Pulse": ResumeConfig(
        "Healthtech Backend / Data Tooling Intern",
        BENTHAM_BACKEND,
        GSOC_AI,
        COMMON_OSS_HEALTH,
        ("hyoka_health", "postificus_backend", "swish_ops"),
        SKILLS["health"],
    ),
    "Trupeer Ai": ResumeConfig(
        "AI Product / Backend Intern",
        BENTHAM_AI,
        GSOC_SHORT,
        COMMON_OSS_AI,
        ("hyoka_agent", "postificus_ops", "seaweed"),
        SKILLS["ai"],
    ),
    "Enerzolve Smart Technologies": ResumeConfig(
        "Backend / Platform Intern",
        BENTHAM_BACKEND,
        GSOC_SHORT,
        COMMON_OSS_BACKEND,
        ("postificus_ops", "hyoka_health", "seaweed"),
        SKILLS["deeptech"],
    ),
    "Sedna Horeca": ResumeConfig(
        "Backend / Platform Intern",
        BENTHAM_BACKEND,
        GSOC_SHORT,
        COMMON_OSS_BACKEND,
        ("swish_ops", "postificus_backend", "seaweed"),
        SKILLS["backend"],
    ),
}


EMAILS = {
    "Atlas": {
        "recipient": "No verified public email in tracker. Use company LinkedIn or founder route.",
        "subject": "Internship inquiry - AI backend / workflow reliability",
        "body": """Hi Atlas team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. I was reading about Atlas and the idea of helping accounting firms scale with AI felt very close to the kind of systems work I enjoy: messy workflows, reliable execution, and making AI outputs inspectable enough for real use.

The closest overlap is my work at Bentham AI. I built backend automation for legal/compliance filing workflows with browser execution, public-site API lookups, retries, session recovery, and operator checkpoints, reducing manual filing time by 85%. I also worked on AI-assisted draft generation for company-name suggestions, object descriptions, and filing fields where the generated output had to stay inspectable before final execution.

I know legal filings and accounting workflows are not the same thing, but the engineering shape feels similar: professional-service workflows, generated drafts, external systems, validation checkpoints, and a need for reliability more than flashy demos. I’ve also built Hyoka, an AI reliability control plane with traces, eval/replay workers, gates, API keys, audit logs, and a dashboard.

If you are open to interns, I’d be interested in helping with backend, integrations, AI workflow reliability, or internal product tooling. I’ve attached a resume tailored to that kind of work.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Bhindi AI": {
        "recipient": "No verified public email in tracker. Use company LinkedIn/contact route.",
        "subject": "Internship inquiry - AI agents / backend reliability",
        "body": """Hi Bhindi team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. Bhindi’s focus on reducing repetitive work with AI caught my attention because I’ve been building around the less glamorous but important parts of AI systems: traces, evals, replay, tool calls, and making agent behavior easier to trust.

The backend reliability side is where I think I can be most useful. At Bentham AI, I built backend automation for compliance-sensitive filing workflows with browser execution, public-site API lookups, retries, session recovery, and operator checkpoints. It reduced manual filing time by 85%, and the main lesson was that AI-assisted workflows only work well when the surrounding backend is recoverable and inspectable.

I’ve also built Hyoka, an AI workflow reliability layer with trace ingestion, eval/replay workers, validation runs, gates, API keys, audit logs, and Dockerized services. Separately, Postificus gave me hands-on backend reliability work with RabbitMQ workers, Redis/PostgreSQL state, DLQs, retries, circuit breakers, health checks, and Prometheus metrics.

I’d be glad to contribute as an intern on backend reliability, AI workflow infrastructure, integrations, or eval tooling if there is room on the team. I’ve attached my resume for context.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Cent": {
        "recipient": "No verified public email in tracker. Use company LinkedIn/contact route.",
        "subject": "Internship inquiry - ML / healthtech backend",
        "body": """Hi Cent team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. Cent stood out to me because your product sits at a very practical intersection of diagnostics, imaging, biomarkers, and software workflows.

The main reason I’m reaching out is my Google Summer of Code work with Invesalius. I worked on a medical-imaging segmentation pipeline for 95 anatomical brain regions, including FastSurfer-style CNN inference, PyTorch/TorchScript and ONNX/TinyGrad paths, NIfTI/MGZ preprocessing, voxel conformation, label remapping, binary masks, QC/debugging, and 3D inspection flows. I also reduced runtime by 87% through async/parallel execution.

That project made me interested in health software where model outputs and data pipelines have to be correct, inspectable, and useful to real workflows. Alongside that, I’ve built Hyoka for traceable AI evaluation/replay workflows and Swish for policy-grounded operational workflows.

If Cent is open to interns, I’d be interested in ML/data pipeline, healthtech backend, or internal tooling work. I’ve attached a resume tailored to this direction.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Maieutic Semiconductor": {
        "recipient": "Founder LinkedIn routes available in tracker; no verified public email found.",
        "subject": "Internship inquiry - AI tooling / backend systems",
        "body": """Hi Maieutic team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. I came across Maieutic’s work on AI-powered analog IC design and found it interesting because it feels like a place where AI is useful only if the surrounding tooling is reliable, reproducible, and easy for engineers to inspect.

My relevant work includes Hyoka, an AI reliability/control-plane project with trace ingestion, eval/replay workers, validation gates, artifacts, audit logs, and a dashboard. During Google Summer of Code with Invesalius, I also worked on model inference and preprocessing pipelines for medical-image segmentation, including PyTorch/TorchScript and ONNX-style paths, large data handling, and debugging model outputs.

If there is scope for an intern on AI tooling, backend/platform work, Python automation, or evaluation infrastructure, I’d be very interested. I’ve attached my resume.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Pulse": {
        "recipient": "info@pulseio.in",
        "subject": "Internship inquiry - healthtech backend / data tooling",
        "body": """Hi Pulse team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. I’m reaching out because Pulse’s work around medical equipment and healthcare access seems like the kind of place where solid backend/data tooling can quietly make a real difference.

I have some relevant healthtech context from Google Summer of Code with Invesalius, where I worked on Python medical-imaging segmentation for 95 anatomical brain regions, including MRI preprocessing, model inference paths, generated masks, QC/debugging, and runtime optimization. I’ve also worked on backend automation at Bentham AI, where I built recoverable browser/API workflows and deployed Dockerized services on Google Cloud Run.

If you are open to interns, I’d be interested in backend, data/ops tooling, QA automation, or healthtech platform work. I’ve attached a tailored resume for your consideration.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Trupeer Ai": {
        "recipient": "No verified public email in tracker. Use company LinkedIn or Pritish Gupta LinkedIn route.",
        "subject": "Internship inquiry - AI product/backend engineering",
        "body": """Hi Trupeer team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. Trupeer caught my eye because AI video and documentation products need more than generation alone; they need reliable ingestion, async jobs, retries, traces, and a product flow that users can actually depend on.

My closest work is Hyoka, where I built trace ingestion, eval/replay workers, validation gates, audit logs, and a dashboard for AI workflow reliability. I also built Postificus, a Go/React workflow app with RabbitMQ workers, retries, DLQs, browser fallback execution, PostgreSQL/Redis state, and Prometheus metrics.

If there is room for an intern on backend, AI product workflows, integrations, or eval/reliability tooling, I’d be glad to contribute. I’ve attached my resume.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Enerzolve Smart Technologies": {
        "recipient": "contact@enerzolve.com",
        "subject": "Internship inquiry - backend/platform engineering",
        "body": """Hi Enerzolve team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. I saw Enerzolve’s work across deep-tech systems, embedded/power electronics, and smart-grid intelligence, and I wanted to check if you are open to engineering interns.

My strongest fit is backend/platform work around real-world systems that need retries, state, observability, and clean deployment. I built Postificus, a Go workflow system with RabbitMQ workers, Redis/PostgreSQL state, DLQs, circuit breakers, health checks, and Prometheus metrics. At Bentham AI, I built recoverable browser/API automation and deployed Dockerized services on Google Cloud Run with GitHub Actions.

I’d be interested in backend, platform tooling, telemetry/data workflows, or Python automation work. I’ve attached a resume tailored to this direction.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
    "Sedna Horeca": {
        "recipient": "engage@sedna.in",
        "subject": "Internship inquiry - backend/platform engineering",
        "body": """Hi Sedna team,

I’m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. Sedna’s work around backend operations for hospitality stood out to me because it looks like a real operations platform problem: inventory, vendors, order state, dashboards, and workflows that have to keep working even when external pieces are messy.

My relevant work is mostly backend and workflow systems. I built Swish, which models operational support cases with order/evidence/policy context, and Postificus, a Go/React workflow app with PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, circuit breakers, health checks, and Prometheus metrics. At Bentham AI, I also worked on recoverable browser/API automation and deployment on Google Cloud Run.

If you are open to interns, I’d be interested in backend, platform tooling, ops workflows, or full-stack internal tools. I’ve attached my resume.

Regards,
Shuvam Pal
+91 85830 54679
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960
""",
    },
}


PREAMBLE = r"""% Tailored early-startup resume
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
\addtolength{\oddsidemargin}{-0.62in}
\addtolength{\evensidemargin}{-0.52in}
\addtolength{\textwidth}{1.22in}
\addtolength{\topmargin}{-.94in}
\addtolength{\textheight}{1.88in}
\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}
\titleformat{\section}{\vspace{-4pt}\scshape\raggedright\large\bfseries}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]
\pdfgentounicode=1
\newcommand{\resumeItem}[1]{\item{\fontsize{9.7pt}{10.25pt}\selectfont #1\vspace{-0.6pt}}}
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
    \end{tabular*}\vspace{-3pt}
}
\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}, itemsep=1.5pt, topsep=0pt, parsep=0pt, partopsep=0pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.7pt,topsep=1.4pt,parsep=0pt,partopsep=0pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-1pt}}
\begin{document}
"""


def heading() -> str:
    return r"""
\begin{center}
    {\Huge \scshape Shuvam Pal} \\ \vspace{1pt}
    \small \raisebox{-0.1\height}\faPhone\ +91 85830 54679 ~
    \href{mailto:ishuvam.pal@gmail.com}{\raisebox{-0.2\height}\faEnvelope\ {ishuvam.pal@gmail.com}} ~
    \href{https://linkedin.com/in/shuvampal3960}{\raisebox{-0.2\height}\faLinkedin\ {Shuvam Pal}} ~
    \href{https://github.com/unichronic}{\raisebox{-0.2\height}\faGithub\ {unichronic}}
    \vspace{-8pt}
\end{center}
"""


def education() -> str:
    return r"""
\section{Education}
\resumeSubHeadingListStart
  \resumeSubheading
    {Dayananda Sagar College of Engineering}{Bengaluru, India}
    {B.E. Artificial Intelligence and Machine Learning}{}
\resumeSubHeadingListEnd
"""


def experience(c: ResumeConfig) -> str:
    bentham_bullets = "\n".join(rf"\resumeItem{{{bullet}}}" for bullet in c.bentham)
    gsoc_bullets = "\n".join(rf"\resumeItem{{{bullet}}}" for bullet in c.gsoc)
    oss_bullets = c.oss if isinstance(c.oss, tuple) else (c.oss,)
    oss_items = "\n".join(rf"\resumeItem{{{bullet}}}" for bullet in oss_bullets)
    return rf"""
\section{{Experience}}
\resumeSubHeadingListStart
\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://www.bentham.legal/}}{{Bentham AI}}}} & \textit{{Dec 2025 -- Feb 2026}} \\
\textit{{Backend Engineering Intern: Node.js, JavaScript, Go, Docker, GCP, GitHub Actions}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
{bentham_bullets}
\resumeItemListEnd
\vspace{{4pt}}

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5}}{{Google Summer of Code}}}} & \textit{{May 2025 -- Sept 2025}} \\
\textit{{Mentee at Invesalius: Python, VTK, wxPython, NumPy, PyTorch, ONNX}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
{gsoc_bullets}
\resumeItemListEnd
\vspace{{4pt}}

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{Open Source}} & \bodyhref{{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}}{{\textit{{Contributions}}}} \\
\end{{tabular*}}
\resumeItemListStart
{oss_items}
\resumeItemListEnd
\resumeSubHeadingListEnd
"""


def projects(c: ResumeConfig) -> str:
    chunks = [r"\section{Projects}", r"\resumeSubHeadingListStart"]
    for key in c.projects:
        p = P[key]
        link = p.link if p.link else ""
        chunks.append(
            rf"""\resumeProjectHeading
{{\textbf{{{p.title}}} $|$ \emph{{{p.tech}}}}}{{{link}}}
\resumeItemListStart
{chr(10).join(rf"\resumeItem{{{bullet}}}" for bullet in p.bullets)}
\resumeItemListEnd"""
        )
    chunks.append(r"\resumeSubHeadingListEnd")
    return "\n".join(chunks)


def skills(c: ResumeConfig) -> str:
    languages, frameworks, tools = c.skills
    return rf"""
\section{{Technical Skills}}
\begin{{itemize}}[leftmargin=0.15in, label={{}}, topsep=0pt, itemsep=0pt, parsep=0pt, partopsep=0pt]
  \item{{\fontsize{{9.6pt}}{{10.0pt}}\selectfont
   \textbf{{Languages}}{{: {languages}}} \\
   \textbf{{Frameworks}}{{: {frameworks}}} \\
   \textbf{{Tools}}{{: {tools}}} \\
  }}
\end{{itemize}}
"""


def resume_tex(company: str, c: ResumeConfig) -> str:
    return "\n".join(
        [
            PREAMBLE,
            heading(),
            education(),
            experience(c),
            projects(c),
            skills(c),
            r"\end{document}",
        ]
    )


def email_md(company: str, email: dict[str, str], resume_pdf: str) -> str:
    return f"""# {company} Email Draft

## Recipient

{email['recipient']}

## Subject

{email['subject']}

## Attachment

`{resume_pdf}`

## Body

{email['body'].strip()}
"""


def compile_pdf(tex_path: Path) -> None:
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
        cwd=tex_path.parent,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(TRACKER.open(newline="", encoding="utf-8")))
    first8 = [r["company"] for r in rows[:8]]
    combined_email = ["# First 8 Early-Startup Email Drafts\n"]
    summary_rows = []

    for company in first8:
        config = CONFIGS[company]
        slug = slugify(company)
        stem = f"{slug}_intern_resume"
        tex_path = OUT_DIR / f"{stem}.tex"
        pdf_path = OUT_DIR / f"{stem}.pdf"
        mail_path = OUT_DIR / f"{slug}_email.md"

        tex_path.write_text(resume_tex(company, config), encoding="utf-8")
        compile_pdf(tex_path)

        email_text = email_md(company, EMAILS[company], pdf_path.name)
        mail_path.write_text(email_text, encoding="utf-8")
        combined_email.append(email_text)
        combined_email.append("\n---\n")
        summary_rows.append((company, config.role_hint, pdf_path, mail_path))

    (OUT_DIR / "first_8_email_drafts.md").write_text("\n".join(combined_email), encoding="utf-8")

    summary = ["# First 8 Application Pack\n", "| Company | Resume angle | Resume | Email draft |", "|---|---|---|---|"]
    for company, role, pdf, mail in summary_rows:
        summary.append(f"| {company} | {role} | `{pdf.name}` | `{mail.name}` |")
    (OUT_DIR / "README.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    print(OUT_DIR)
    for company, _, pdf, mail in summary_rows:
        print(f"{company}: {pdf.name} | {mail.name}")


if __name__ == "__main__":
    main()
