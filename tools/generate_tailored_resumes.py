from __future__ import annotations

import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "tailored_resumes"
OUT_DIR = SOURCE_DIR / "full"


@dataclass(frozen=True)
class Project:
    title: str
    tech: str
    link: str
    bullets: tuple[str, str]


@dataclass(frozen=True)
class ResumeConfig:
    display: str
    profile: str
    projects: tuple[str, str, str]
    skills: str


def href(url: str, label: str = "GitHub") -> str:
    return rf"\bodyhref{{{url}}}{{{label}}}"


PROJECTS: dict[str, Project] = {
    "murdoc_security": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Built a self-hosted \textbf{AI security gateway} for LLM, HTTP tool, and MCP traffic, blocking \textbf{90\%+} of prompt-injection and unsafe-tool attempts across a \textbf{150-case attack corpus} with false positives under \textbf{5\%}.",
            r"Added route profiles, RBAC runtime settings, PII redaction, allow/block rules, \textbf{OpenTelemetry} metrics/traces, health checks, and audit ledgers for \textbf{100\%} of policy decisions.",
        ),
    ),
    "murdoc_routing": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Built an \textbf{AI gateway} for LLM, HTTP tool, and MCP traffic with route profiles, runtime policy checks, request scoring, and replayable decisions before downstream execution.",
            r"Instrumented provider/tool flows with \textbf{OpenTelemetry} traces, Prometheus metrics, audit ledgers, and attack-lab validation so latency, failures, and unsafe actions could be investigated per request.",
        ),
    ),
    "murdoc_observability": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Instrumented an AI gateway with \textbf{OpenTelemetry metrics/traces}, Prometheus health checks, route profiles, and audit logs tying model/tool requests to policy outcomes.",
            r"Built replayable decision records for prompt, tool, retrieval, and output layers so high-risk agent behavior could be correlated with request context and failure modes.",
        ),
    ),
    "murdoc_metadata": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Built a gateway that preserves context around prompts, tools, retrieved data, policy decisions, and outputs, making AI-agent actions inspectable through structured traces and audit ledgers.",
            r"Modeled runtime settings, route profiles, RBAC decisions, and attack-lab outcomes as explicit metadata so agent behavior could be governed, replayed, and debugged.",
        ),
    ),
    "murdoc_cloudsek": Project(
        "Murdoc",
        "Python, FastAPI, MCP, OpenTelemetry, Prometheus, Docker",
        href("https://github.com/unichronic/murdoc"),
        (
            r"Built a self-hosted \textbf{AI security gateway} for LLM, HTTP-tool, and MCP traffic with route profiles, request scoring, allow/block policies, and runtime checks before downstream API execution.",
            r"Blocked \textbf{90\%+} prompt-injection and unsafe-tool attempts across a \textbf{150-case attack corpus} with false positives under \textbf{5\%}; added RBAC, PII redaction, and audit ledgers for \textbf{100\%} of policy decisions.",
        ),
    ),
    "postificus_browser": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, AWS, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built a \textbf{content distribution platform} using Go-Rod browser automation to cross-post to Medium, Dev.to, and Hashnode when direct publishing APIs were insufficient.",
            r"Engineered RabbitMQ workers with DLQs, retries, Redis-backed autosave, circuit breakers, Prometheus metrics, and health checks for long-running third-party browser tasks.",
        ),
    ),
    "postificus_observability": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, AWS, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built observable Go services for a \textbf{content distribution platform} using browser automation, with RabbitMQ workers, DLQs, retries, Redis autosave, and PostgreSQL persistence.",
            r"Added circuit-breaker logic and failure isolation for third-party publishing paths, keeping browser automation failures observable and recoverable instead of cascading through the system.",
        ),
    ),
    "postificus_cloud": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, AWS, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built containerized Go/Rod services for a \textbf{content distribution platform} using browser automation, with async workers, RabbitMQ retries, Redis state, and PostgreSQL persistence.",
            r"Designed the system for operational simplicity, service isolation, and recoverable execution around unreliable external integrations and long-running jobs.",
        ),
    ),
    "postificus_workflow": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, AWS",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built backend workflows for a \textbf{content distribution platform} using browser automation, coordinating content transformation, multi-platform publishing, image storage, autosave, and durable job status.",
            r"Used RabbitMQ, Redis, PostgreSQL, and Dockerized Go services to keep multi-step external integrations recoverable, auditable, and simple to operate.",
        ),
    ),
    "postificus_cloudsek": Project(
        "Postificus",
        "Go, Echo, Rod, PostgreSQL, Redis, RabbitMQ, Docker, AWS, Prometheus",
        href("https://github.com/unichronic/postificus"),
        (
            r"Built Go/Echo backend services for a \textbf{content distribution platform} using browser automation, with REST APIs, RabbitMQ workers, Redis autosave, and PostgreSQL persistence.",
            r"Added DLQs, retries, circuit-breaker isolation, and failure telemetry so unreliable external API/browser workflows stayed recoverable instead of cascading through distributed workers.",
        ),
    ),
    "seaweed_eval": Project(
        "Seaweed: Contest Platform",
        "Go, React, PostgreSQL, Judge0, Redis, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Architected a full-stack contest platform supporting \textbf{500+ concurrent users}, automated judging, live rankings, and feedback loops for programming contest workflows.",
            r"Designed a sandboxed Judge0 pipeline with async Go dispatch, Docker/Kubernetes deployment on AWS, \textbf{sub-5s P95 verdict latency}, per-test telemetry, and PostgreSQL-backed result analysis.",
        ),
    ),
    "seaweed_database": Project(
        "Seaweed: Contest Platform",
        "Go, PostgreSQL, Redis, Judge0, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built a backend-heavy ranking system for \textbf{500+ concurrent users}, using PostgreSQL materialized views and concurrent refreshes to preserve live leaderboard behavior.",
            r"Deployed Dockerized services on Kubernetes/AWS and replaced a Redis + DynamoDB design with PostgreSQL-centered architecture, reducing infrastructure cost by \textbf{~70\%}.",
        ),
    ),
    "seaweed_backend": Project(
        "Seaweed: Contest Platform",
        "Go, PostgreSQL, Redis, Judge0, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built backend services for registration, submissions, sandboxed execution, scoring, and live contest rankings across \textbf{500+ concurrent users}.",
            r"Used async Go workers, Judge0, PostgreSQL, Redis, and Docker/Kubernetes deployment paths on AWS to keep evaluation workflows recoverable under contest load.",
        ),
    ),
    "seaweed_cloudsek": Project(
        "Seaweed: Contest Platform",
        "Go, PostgreSQL, Redis, Judge0, AWS, Docker, Kubernetes",
        href("https://github.com/unichronic/seaweed-fe"),
        (
            r"Built \textbf{Go backend services} for registration, submissions, sandboxed code execution, scoring, and live contest rankings across \textbf{500+ concurrent users}.",
            r"Designed async Judge0 dispatch, PostgreSQL result schemas, Redis-backed runtime state, and Docker/Kubernetes deployment on AWS, achieving \textbf{sub-5s P95 verdict latency}.",
        ),
    ),
    "swish_cx": Project(
        "Swish Support System",
        "Python, Go, FastAPI, Gin, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built an AI support system with per-conversation context for active item, issue type, requested resolution, pending confirmations, and evidence artifacts, achieving \textbf{85\%+} policy-correct resolutions on a \textbf{50-case} eval set.",
            r"Reduced compensation leakage by \textbf{25\%} versus a naive refund baseline by separating semantic understanding from deterministic policy and tracing high-risk cases with \textbf{Langfuse}.",
        ),
    ),
    "swish_workflow": Project(
        "Swish Support System",
        "Python, Go, FastAPI, Gin, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built AI-assisted backend workflows for order status, delays, refunds, trust checks, and escalation using tool calls over operational APIs with PostgreSQL and Redis state.",
            r"Added retrieval-backed responses, confidence thresholds, human handoff paths, conversation memory, and traceable action records for ambiguous or high-risk user workflows.",
        ),
    ),
    "swish_policy": Project(
        "Swish Support System",
        "Python, Go, FastAPI, Gin, PostgreSQL, Redis, Langfuse",
        href("https://github.com/unichronic/swishagent"),
        (
            r"Built policy-grounded support workflows where LLM reasoning proposed actions but deterministic services enforced refund, remake, coupon, trust, and escalation rules.",
            r"Carried customer/order context across turns and traced high-risk decisions with Langfuse/local logs, keeping agent actions inspectable rather than prompt-only.",
        ),
    ),
    "penny_agents": Project(
        "Penny Lane Capital (Tradeage)",
        "Python, Agno, Pydantic, SQLite, yfinance, JSONL",
        "",
        (
            r"Built an \textbf{Agno Workflow} multi-agent research system with analyst roles, bull/bear debate, trader, risk review, and portfolio approval using Pydantic state, checkpoints, memory, and JSONL traces.",
            r"Evaluated agent decisions with historical-market backtests, reward loops, validation harnesses, and \textbf{5 baselines}, producing return, drawdown, and win-rate scorecards across market windows.",
        ),
    ),
    "inference": Project(
        "Distributed Inference Engine",
        "Python, PyTorch, FastAPI, gRPC, CUDA, Docker, Redis",
        "",
        (
            r"Built a \textbf{distributed inference engine} to run models larger than a single consumer GPU by coordinating token generation across heterogeneous nodes with speculative decoding.",
            r"Designed streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing to balance latency, throughput, and worker availability across local and remote inference workers.",
        ),
    ),
    "edge_inference": Project(
        "Distributed Inference Engine",
        "Python, PyTorch, FastAPI, gRPC, CUDA, Docker, Redis",
        "",
        (
            r"Built a distributed inference runtime across heterogeneous consumer hardware, coordinating speculative decoding, worker health, streaming responses, and request routing under hardware constraints.",
            r"Tracked throughput, latency, token acceptance, and memory-utilization signals to reason about low-latency generation and edge-style runtime coordination.",
        ),
    ),
}


SKILLS: dict[str, str] = {
    "ai_infra": r"""\textbf{Languages}{: Python, Go, TypeScript, C++} \\
   \textbf{Frameworks}{: FastAPI, Echo, Node.js, Express, PyTorch, gRPC} \\
   \textbf{Tools}{: Redis, PostgreSQL, Docker, Prometheus, OpenTelemetry, RabbitMQ} \\""",
    "security": r"""\textbf{Languages}{: Go, Python, TypeScript} \\
   \textbf{Frameworks}{: FastAPI, Gin, Echo, Node.js} \\
   \textbf{Tools}{: MCP, OpenTelemetry, Prometheus, PostgreSQL, Redis, Docker, GitHub Actions} \\""",
    "security_backend": r"""\textbf{Languages}{: Go, JavaScript/TypeScript, Python} \\
   \textbf{Frameworks}{: Echo, FastAPI, Gin, Express, GraphQL} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, GitHub Actions, Prometheus, OpenTelemetry, GCP, AWS} \\""",
    "observability": r"""\textbf{Languages}{: Go, Python, TypeScript} \\
   \textbf{Frameworks}{: FastAPI, Echo, Gin, Node.js} \\
   \textbf{Tools}{: OpenTelemetry, Prometheus, Langfuse, PostgreSQL, Redis, RabbitMQ, Docker, GitHub Actions} \\""",
    "database": r"""\textbf{Languages}{: Go, Python, TypeScript, C++} \\
   \textbf{Frameworks}{: FastAPI, Echo, Node.js, gRPC} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, Prometheus, AWS, GitHub Actions} \\""",
    "cloud": r"""\textbf{Languages}{: Go, Python, TypeScript} \\
   \textbf{Frameworks}{: Echo, FastAPI, Gin, Node.js} \\
   \textbf{Tools}{: Docker, Google Cloud Run, GitHub Actions, PostgreSQL, Redis, RabbitMQ, Prometheus, AWS} \\""",
    "workflow": r"""\textbf{Languages}{: Python, Go, TypeScript} \\
   \textbf{Frameworks}{: FastAPI, Gin, Echo, Node.js, Agno} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, Langfuse, OpenTelemetry, GitHub Actions, AWS} \\""",
    "devtools": r"""\textbf{Languages}{: Go, Python, TypeScript} \\
   \textbf{Frameworks}{: FastAPI, Echo, Node.js, React} \\
   \textbf{Tools}{: Judge0, PostgreSQL, Redis, Docker, GitHub Actions, OpenTelemetry, Prometheus} \\""",
    "browser": r"""\textbf{Languages}{: Go, Python, TypeScript} \\
   \textbf{Frameworks}{: Echo, FastAPI, Node.js, React} \\
   \textbf{Tools}{: Go-Rod, Puppeteer, RabbitMQ, Redis, PostgreSQL, Docker, Prometheus, OpenTelemetry} \\""",
}


CONFIGS: dict[str, ResumeConfig] = {
    "apica": ResumeConfig("Apica", "observability", ("postificus_observability", "murdoc_observability", "swish_workflow"), SKILLS["observability"]),
    "atlas": ResumeConfig("Atlas", "finance_workflow", ("swish_workflow", "postificus_workflow", "seaweed_backend"), SKILLS["workflow"]),
    "atlan": ResumeConfig("Atlan", "metadata", ("murdoc_metadata", "penny_agents", "swish_workflow"), SKILLS["workflow"]),
    "auctor": ResumeConfig("Auctor", "workflow", ("swish_workflow", "postificus_workflow", "seaweed_backend"), SKILLS["workflow"]),
    "azul": ResumeConfig("Azul", "runtime", ("seaweed_database", "inference", "postificus_observability"), SKILLS["database"]),
    "browser_use": ResumeConfig("Browser Use", "browser", ("postificus_browser", "murdoc_routing", "penny_agents"), SKILLS["browser"]),
    "cast_ai": ResumeConfig("CAST AI", "cloud", ("inference", "postificus_cloud", "murdoc_observability"), SKILLS["cloud"]),
    "chainguard": ResumeConfig("Chainguard", "security", ("murdoc_security", "postificus_cloud", "inference"), SKILLS["security"]),
    "clickhouse": ResumeConfig("ClickHouse", "database", ("inference", "seaweed_database", "postificus_observability"), SKILLS["database"]),
    "cloud_in": ResumeConfig("Cloud.in", "cloud", ("postificus_cloud", "seaweed_backend", "murdoc_observability"), SKILLS["cloud"]),
    "cloudsek": ResumeConfig("CloudSEK", "security_backend", ("murdoc_cloudsek", "postificus_cloudsek", "seaweed_cloudsek"), SKILLS["security_backend"]),
    "cloudthat": ResumeConfig("CloudThat Technologies", "cloud", ("postificus_cloud", "seaweed_backend", "murdoc_observability"), SKILLS["cloud"]),
    "cockroachdb": ResumeConfig("CockroachDB", "database", ("seaweed_database", "postificus_observability", "inference"), SKILLS["database"]),
    "coderabbit": ResumeConfig("CodeRabbit", "devtools", ("seaweed_eval", "murdoc_routing", "penny_agents"), SKILLS["devtools"]),
    "concerto_by_trianz": ResumeConfig("Concerto by Trianz", "cloud", ("postificus_cloud", "seaweed_backend", "murdoc_metadata"), SKILLS["cloud"]),
    "coralogix": ResumeConfig("Coralogix", "observability", ("postificus_observability", "murdoc_observability", "swish_policy"), SKILLS["observability"]),
    "deccan_ai": ResumeConfig("Deccan AI", "devtools", ("seaweed_eval", "penny_agents", "postificus_browser"), SKILLS["devtools"]),
    "digital_paani": ResumeConfig("Digital Paani", "ops_workflow", ("postificus_workflow", "swish_workflow", "seaweed_backend"), SKILLS["workflow"]),
    "dragonfly": ResumeConfig("Dragonfly", "database", ("seaweed_database", "inference", "postificus_observability"), SKILLS["database"]),
    "grafana_labs": ResumeConfig("Grafana Labs", "observability", ("postificus_observability", "murdoc_observability", "swish_policy"), SKILLS["observability"]),
    "hackerrank": ResumeConfig("HackerRank", "devtools", ("seaweed_eval", "penny_agents", "murdoc_routing"), SKILLS["devtools"]),
    "i2k2": ResumeConfig("i2k2 Networks", "security", ("postificus_cloud", "murdoc_security", "seaweed_backend"), SKILLS["security"]),
    "ibm_cloudability": ResumeConfig("IBM Cloudability", "cloud", ("postificus_cloud", "seaweed_database", "murdoc_observability"), SKILLS["cloud"]),
    "kong": ResumeConfig("Kong", "ai_gateway", ("murdoc_routing", "postificus_observability", "inference"), SKILLS["ai_infra"]),
    "manageengine": ResumeConfig("ManageEngine", "observability", ("postificus_observability", "swish_cx", "murdoc_observability"), SKILLS["observability"]),
    "miniorange": ResumeConfig("miniOrange", "security", ("murdoc_security", "swish_policy", "postificus_cloud"), SKILLS["security"]),
    "mintlify": ResumeConfig("Mintlify", "devtools", ("postificus_workflow", "seaweed_eval", "swish_workflow"), SKILLS["devtools"]),
    "neodocs": ResumeConfig("NeoDocs", "workflow", ("swish_workflow", "seaweed_backend", "postificus_workflow"), SKILLS["workflow"]),
    "neosoft_cloud": ResumeConfig("NeoSOFT Cloud", "cloud", ("postificus_cloud", "seaweed_backend", "murdoc_observability"), SKILLS["cloud"]),
    "novaflow": ResumeConfig("Novaflow", "workflow", ("inference", "seaweed_backend", "penny_agents"), SKILLS["ai_infra"]),
    "oceanbase": ResumeConfig("OceanBase", "database", ("seaweed_database", "inference", "postificus_observability"), SKILLS["database"]),
    "one2n": ResumeConfig("One2N", "cloud", ("postificus_cloud", "seaweed_backend", "murdoc_observability"), SKILLS["cloud"]),
    "openrouter": ResumeConfig("OpenRouter", "ai_infra", ("inference", "murdoc_routing", "swish_workflow"), SKILLS["ai_infra"]),
    "pulse": ResumeConfig("Pulse", "workflow", ("swish_workflow", "inference", "seaweed_eval"), SKILLS["workflow"]),
    "redis": ResumeConfig("Redis", "database", ("inference", "seaweed_database", "postificus_observability"), SKILLS["database"]),
    "remotestar": ResumeConfig("RemoteStar", "cloud", ("postificus_cloud", "seaweed_backend", "penny_agents"), SKILLS["cloud"]),
    "repello_ai": ResumeConfig("Repello AI", "security", ("murdoc_security", "swish_policy", "penny_agents"), SKILLS["security"]),
    "round_treasury": ResumeConfig("Round Treasury", "finance_workflow", ("swish_workflow", "postificus_workflow", "seaweed_backend"), SKILLS["workflow"]),
    "shellkode": ResumeConfig("Shellkode", "cloud", ("postificus_cloud", "inference", "swish_workflow"), SKILLS["cloud"]),
    "sid": ResumeConfig("SID", "ai_infra", ("inference", "murdoc_routing", "penny_agents"), SKILLS["ai_infra"]),
    "signoz": ResumeConfig("SigNoz", "observability", ("murdoc_observability", "postificus_observability", "swish_policy"), SKILLS["observability"]),
    "solidroad": ResumeConfig("Solidroad", "cx", ("swish_cx", "murdoc_security", "penny_agents"), SKILLS["workflow"]),
    "stackgen": ResumeConfig("StackGen", "cloud", ("postificus_cloud", "murdoc_security", "inference"), SKILLS["cloud"]),
    "subimage": ResumeConfig("SubImage", "security", ("murdoc_security", "postificus_cloud", "seaweed_backend"), SKILLS["security"]),
    "swif_ai": ResumeConfig("Swif.ai", "security", ("murdoc_security", "swish_policy", "postificus_cloud"), SKILLS["security"]),
    "testmu_ai": ResumeConfig("TestMu AI", "devtools", ("seaweed_eval", "postificus_browser", "murdoc_routing"), SKILLS["devtools"]),
    "tidb": ResumeConfig("TiDB", "database", ("seaweed_database", "inference", "postificus_observability"), SKILLS["database"]),
    "tsecondai": ResumeConfig("TsecondAI", "edge", ("edge_inference", "murdoc_routing", "postificus_cloud"), SKILLS["ai_infra"]),
    "upwind": ResumeConfig("Upwind", "security", ("murdoc_security", "inference", "postificus_cloud"), SKILLS["security"]),
    "work_on_grid": ResumeConfig("Work On Grid", "ops_workflow", ("postificus_workflow", "swish_workflow", "seaweed_backend"), SKILLS["workflow"]),
    "xurrent": ResumeConfig("Xurrent", "observability", ("swish_cx", "postificus_observability", "murdoc_observability"), SKILLS["observability"]),
    "yugabytedb": ResumeConfig("YugabyteDB", "database", ("seaweed_database", "inference", "postificus_observability"), SKILLS["database"]),
}


COMPANY_FOCUS: dict[str, str] = {
    "apica": "observability, telemetry pipelines, OpenTelemetry, Prometheus, health checks, agent-event traces",
    "atlas": "AI accounting workflows, finance operations, audit trails, backend workflow reliability, operational APIs",
    "atlan": "context layer, active metadata, governance, trace lineage, AI agent reliability, enterprise data",
    "auctor": "implementation automation, enterprise workflows, structured data, handoffs, services-to-software",
    "azul": "runtime/platform performance, cloud cost optimization, backend performance, production tuning",
    "browser_use": "browser agents, browser automation, retry-aware browser flows, workflow reliability, agent tooling",
    "cast_ai": "cloud platform automation, compute efficiency, service health, cloud cost, production reliability",
    "chainguard": "policy enforcement, CI/CD security, containers, open-source review, AI coding-agent guardrails",
    "clickhouse": "real-time analytics, observability data, Postgres, Redis, Prometheus, AI data infrastructure",
    "cloud_in": "managed cloud, platform support, cloud workloads, service health, production reliability",
    "cloudsek": "backend intern, cybersecurity products, NodeJS/Go, GraphQL, backend APIs, PostgreSQL, Docker, CI/CD, attack surface monitoring, cyber threat intelligence, digital risk workflows",
    "cloudthat": "cloud consulting, platform delivery, AWS, containerized services, cloud enablement",
    "cockroachdb": "distributed SQL, correctness, resilience, PostgreSQL-backed systems, storage reliability",
    "coderabbit": "AI code review, PR workflows, evaluation pipelines, review quality, developer tooling",
    "concerto_by_trianz": "cloud transformation, data platforms, workflow automation, agentic AI delivery, consulting",
    "coralogix": "AI observability, telemetry pipelines, real-time observability, cost-aware systems, incident context",
    "deccan_ai": "AI evaluation systems, coding assessments, agent workflows, browser automation, trace verification",
    "digital_paani": "operational data, external integrations, deployments, monitoring, backend data reliability",
    "dragonfly": "Redis-backed systems, in-memory data paths, cache performance, low-latency backend services",
    "grafana_labs": "open-source observability, metrics, traces, service health, AI workload observability",
    "hackerrank": "technical assessment, AI fluency, evaluation systems, developer tooling, code execution",
    "i2k2": "managed cloud, infrastructure operations, security controls, hosting, customer delivery",
    "ibm_cloudability": "cloud cost awareness, infrastructure cost reduction, service metrics, cloud spend discipline",
    "kong": "API gateway, AI gateway, MCP traffic, request governance, distributed systems",
    "manageengine": "AIOps, incident response, IT operations, observability backend, support workflows",
    "miniorange": "access governance, policy enforcement, AI agent access, RBAC, authentication-aware workflows",
    "mintlify": "developer docs, knowledge workflows, retrieval-backed support, devtools, content automation",
    "neodocs": "health data, diagnostics workflows, APIs, document data, reliable backend systems",
    "neosoft_cloud": "cloud consulting, platform delivery, DevOps, client-facing backend, cloud services",
    "novaflow": "scientific workflows, medical-image data, reproducible pipelines, research automation",
    "oceanbase": "distributed database, AI data layer, transactional workflows, backend data systems",
    "one2n": "SRE, production ownership, incident response, platform engineering, DevOps, reliability",
    "openrouter": "multi-model inference, provider routing, fallback logic, latency, token cost, developer platform",
    "pulse": "document workflows, model inference, operational APIs, traceable actions, evaluation pipelines",
    "redis": "Redis-backed systems, caching, real-time data, low-latency reads, distributed systems",
    "remotestar": "remote engineering, cloud delivery, backend ownership, distributed teams, platform delivery",
    "repello_ai": "prompt injection, MCP security, unsafe tool execution, runtime policy, guardrails, audit logs",
    "round_treasury": "finance workflow automation, operational APIs, audit trails, backend reliability, recoverable workflows",
    "shellkode": "cloud services, GenAI workflows, platform delivery, consulting, backend integration",
    "sid": "LLM systems, routing, latency, evaluation workflows, agent memory, checkpoints",
    "signoz": "OpenTelemetry, traces, metrics, Prometheus, observability backend, incident context",
    "solidroad": "support QA, conversation evaluation, agent supervision, escalation, customer-service automation",
    "stackgen": "DevOps automation, platform engineering, CI/CD, containerized services, operational reliability",
    "subimage": "security tooling, policy enforcement, open-source review, request context, backend security",
    "swif_ai": "enterprise security workflows, policy enforcement, access controls, audit logs, backend reliability",
    "testmu_ai": "agentic testing, browser automation, test infrastructure, QA automation, evaluation pipelines",
    "tidb": "database-backed systems, PostgreSQL materialized views, real-time ranking data, query performance, low-latency reads",
    "tsecondai": "edge AI, hardware-aware inference, low-latency runtime, streaming APIs, worker health",
    "upwind": "runtime security, cloud services, AI gateway security, policy enforcement, observability, backend reliability",
    "work_on_grid": "operational data workflows, backend automation, recoverable integrations, AI-assisted workflows, data platform reliability",
    "xurrent": "service management workflows, incident context, workflow automation, observability, support operations",
    "yugabytedb": "PostgreSQL-backed systems, cloud-deployed services, resilience, query performance, low-latency reads",
}


PREAMBLE = r"""% Generated full tailored resume. Source: tools/generate_tailored_resumes.py
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
\usepackage{multicol}
\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
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

\titleformat{\section}{
  \vspace{-5pt}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]

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
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.16in]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

\begin{document}
"""


PROFILE_HINTS: dict[str, dict[str, tuple[str, str, str]]] = {
    "ai_infra": {
        "bentham": (
            r"Architected a resilient \textbf{Puppeteer/Node.js automation engine} for MCA filings, reducing manual filing time by \textbf{85\%} through network-idle handling, Vision API CAPTCHA solving, retries, and API-backed state checks.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized services with \textbf{Docker}, deployed to \textbf{Google Cloud Run}, and automated releases with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions} using PyTorch/TinyGrad-compatible deep learning models and production-style preprocessing over large medical volumes.",
            r"Optimized processing time by \textbf{87\%} through asynchronous execution, parallel processing, and fewer repeated passes across high-dimensional image data.",
            r"Extended 3D reconstructed surface visualization workflows, keeping model outputs usable for interactive inspection and downstream analysis.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, adapting patches to existing architecture, maintainer review, and project conventions.",
        ),
    },
    "security": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js workflow} for MCA filings with session handling, CAPTCHA handoff, form retries, and state recovery, reducing manual filing time by \textbf{85\%}.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized backend services with \textbf{Docker}, wired \textbf{GitHub Actions} deployments to \textbf{Google Cloud Run}, and improved release velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built medical-image segmentation tooling for \textbf{95 brain subparts}, handling model inference, orientation, preprocessing, and large-volume data paths with reproducible outputs.",
            r"Reduced segmentation runtime by \textbf{87\%} using asynchronous and parallel execution while preserving inspection workflows for generated masks and 3D surfaces.",
            r"Worked in a mature open-source codebase with review constraints, compatibility concerns, and careful integration into existing user workflows.",
        ),
        "oss": (
            r"Contributed patches across Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, working inside existing maintainer security, reliability, and review expectations.",
        ),
    },
    "observability": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js automation engine} for MCA filings, reducing manual filing time by \textbf{85\%} through retries, network-idle monitoring, and recoverable browser-state handling.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized services with \textbf{Docker}, deployed to \textbf{Google Cloud Run}, and automated releases with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions} and integrated model outputs into visualization workflows that needed repeatable, inspectable processing.",
            r"Profiled volume-processing paths and reduced runtime by \textbf{87\%} with async/parallel execution and fewer repeated post-processing passes.",
            r"Improved 3D reconstructed surface visualization flows, keeping image-processing outputs usable for debugging and review.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, adapting fixes to maintainer review and existing observability/debugging practices.",
        ),
    },
    "database": {
        "bentham": (
            r"Built a \textbf{Puppeteer/Node.js automation engine} for stateful MCA filing workflows, reducing manual filing time by \textbf{85\%} through retries, session recovery, and API-backed state checks.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized services with \textbf{Docker}, deployed to \textbf{Google Cloud Run}, and automated builds/releases with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling over large volume data, producing masks for \textbf{95 brain subparts} with PyTorch/TinyGrad model support.",
            r"Reduced processing runtime by \textbf{87\%} through async/parallel execution and fewer repeated passes across large image arrays.",
            r"Improved 3D reconstructed surface visualization, keeping derived model outputs inspectable for downstream workflows.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, working with established codebases and maintainer feedback loops.",
        ),
    },
    "cloud": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js automation service} for MCA filings, reducing manual filing time by \textbf{85\%} with retries, browser-state recovery, and API-backed validation.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized backend services with \textbf{Docker}, deployed to \textbf{Google Cloud Run}, and automated CI/CD with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions}, integrating model inference, preprocessing, and visualization into an existing desktop medical-imaging application.",
            r"Reduced processing time by \textbf{87\%} using asynchronous and parallel execution across expensive image-processing workflows.",
            r"Improved 3D reconstructed surface visualization while preserving compatibility with existing VTK/wxPython user flows.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, adapting implementation details to established open-source review and release practices.",
        ),
    },
    "workflow": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js workflow engine} for MCA company-registration filings, reducing manual filing time by \textbf{85\%} through state recovery, retries, and public-site API lookups.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized services with \textbf{Docker} and automated \textbf{GitHub Actions} deployments to \textbf{Google Cloud Run}, improving release velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions}, turning model outputs into usable masks and 3D visualization artifacts inside an existing application workflow.",
            r"Reduced processing runtime by \textbf{87\%} with async/parallel execution and fewer repeated post-processing passes over large MRI volumes.",
            r"Integrated outputs into 3D reconstructed surface visualization flows so model results stayed inspectable and useful to end users.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, working with existing maintainers, code style, and review constraints.",
        ),
    },
    "devtools": {
        "bentham": (
            r"Built a resilient \textbf{Puppeteer/Node.js automation engine} for MCA filings, reducing manual filing time by \textbf{85\%} through reliable browser execution, retries, and API-backed state checks.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized services with \textbf{Docker}, deployed to \textbf{Google Cloud Run}, and automated releases through \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions} with PyTorch/TinyGrad model support and integration into an existing open-source application.",
            r"Reduced runtime by \textbf{87\%} using asynchronous and parallel processing, turning slow model workflows into a more usable developer/user experience.",
            r"Improved 3D surface visualization around model outputs, making generated artifacts easier to inspect and validate.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, adapting patches to established code review, issue context, and maintainer expectations.",
        ),
    },
    "browser": {
        "bentham": (
            r"Architected a resilient \textbf{Puppeteer/Node.js browser automation engine} for MCA filings, reducing manual filing time by \textbf{85\%} through network-idle monitoring, CAPTCHA handoff, retries, and state recovery.",
            r"Optimized an \textbf{AI-assisted company-registration pipeline} for unique company-name suggestions, descriptions, and filing-field drafts, reducing manual drafting/rework across MCA workflow preparation.",
            r"Containerized services with \textbf{Docker}, deployed to \textbf{Google Cloud Run}, and automated releases through \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built MRI segmentation tooling for \textbf{95 anatomical regions}, integrating model inference outputs into existing visualization and user-interaction paths.",
            r"Reduced processing time by \textbf{87\%} using async and parallel execution over expensive model and image-processing workflows.",
            r"Enhanced 3D surface visualization so generated masks and model outputs remained inspectable in the application.",
        ),
        "oss": (
            r"Contributed to Invesalius, IOOS, VideoLAN, CRIU, Tiled, Kyverno, and Kuadrant, working within existing codebases and maintainer review loops.",
        ),
    },
}


PROFILE_ALIASES = {
    "finance_workflow": "workflow",
    "metadata": "workflow",
    "runtime": "database",
    "ai_gateway": "ai_infra",
    "ops_workflow": "workflow",
    "cx": "workflow",
    "edge": "ai_infra",
    "security_backend": "security",
}


def profile_hint(profile: str) -> dict[str, tuple[str, ...]]:
    return PROFILE_HINTS[PROFILE_ALIASES.get(profile, profile)]


def discover_slugs() -> list[str]:
    slugs = sorted(p.name.removesuffix("_resume.tex") for p in SOURCE_DIR.glob("*_resume.tex"))
    if "atlan" not in slugs:
        slugs.append("atlan")
    return sorted(set(slugs).union(CONFIGS))


def render_project(key: str) -> str:
    project = PROJECTS[key]
    link = project.link
    return rf"""
\resumeProjectHeading
{{\textbf{{{project.title}}} $|$ \emph{{{project.tech}}}}}{{{link}}}
\resumeItemListStart
\resumeItem{{{project.bullets[0]}}}
\resumeItem{{{project.bullets[1]}}}
\resumeItemListEnd
"""


def render_resume(slug: str, config: ResumeConfig) -> str:
    hints = profile_hint(config.profile)
    bentham = hints["bentham"]
    gsoc = hints["gsoc"]
    oss = hints["oss"]
    projects = "\n".join(render_project(key) for key in config.projects)
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
\resumeItem{{{bentham[0]}}}
\resumeItem{{{bentham[1]}}}
\resumeItem{{{bentham[2]}}}
\resumeItemListEnd

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5}}{{Google Summer of Code}}}} & \textit{{May 2025 -- Sept 2025}} \\
\textit{{Mentee at Invesalius: Python, VTK, wxPython, NumPy, PyTorch, ONNX}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
\resumeItem{{{gsoc[0]}}}
\resumeItem{{{gsoc[1]}}}
\resumeItem{{{gsoc[2]}}}
\resumeItemListEnd

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{Open Source}} & \bodyhref{{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}}{{\textit{{Contributions}}}} \\
\end{{tabular*}}
\resumeItemListStart
\resumeItem{{{oss[0]}}}
\resumeItemListEnd

\resumeSubHeadingListEnd

\section{{Projects}}
\resumeSubHeadingListStart
{projects}
\resumeSubHeadingListEnd

\section{{Technical Skills}}
\begin{{itemize}}[leftmargin=0.15in, label={{}}]
  \small{{\item{{
   {config.skills}
  }}}}
\end{{itemize}}

\end{{document}}
"""


def write_resumes(slugs: list[str]) -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for slug in slugs:
        config = CONFIGS.get(slug)
        if config is None:
            config = ResumeConfig(slug.replace("_", " ").title(), "cloud", ("postificus_cloud", "seaweed_backend", "murdoc_observability"), SKILLS["cloud"])
        path = OUT_DIR / f"{slug}_resume.tex"
        path.write_text(render_resume(slug, config), encoding="utf-8")
        written.append(path)
    return written


def write_keyword_report(slugs: list[str]) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / "company_keyword_focus.md"
    rows = [
        "# Company Keyword Targets",
        "",
        "Generated by `tools/generate_tailored_resumes.py`.",
        "",
        "| Resume | Keyword targets |",
        "| --- | --- |",
    ]
    for slug in slugs:
        config = CONFIGS.get(slug)
        display = config.display if config else slug.replace("_", " ").title()
        rows.append(f"| `{slug}_resume.pdf` | {COMPANY_FOCUS.get(slug, display)} |")
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return path


def compile_resumes(paths: list[Path]) -> list[tuple[Path, int]]:
    failures: list[tuple[Path, int]] = []
    for path in paths:
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
            failures.append((path, result.returncode))
    return failures


def clean_aux() -> None:
    for ext in ("*.aux", "*.log", "*.out"):
        for path in OUT_DIR.glob(ext):
            path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compile", action="store_true", help="Compile generated TeX files to PDFs")
    parser.add_argument("--clean-aux", action="store_true", help="Remove LaTeX aux/log/out files after compilation")
    args = parser.parse_args()

    slugs = discover_slugs()
    paths = write_resumes(slugs)
    report = write_keyword_report(slugs)
    failures: list[tuple[Path, int]] = []
    if args.compile:
        failures = compile_resumes(paths)
    if args.clean_aux:
        clean_aux()

    print(f"Generated {len(paths)} full resumes in {OUT_DIR.relative_to(ROOT)}")
    print(f"Wrote keyword report to {report.relative_to(ROOT)}")
    if args.compile:
        print(f"Compiled {len(paths) - len(failures)} PDFs")
    if failures:
        print("Failures:")
        for path, code in failures:
            print(f"  {path.name}: exit {code}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
