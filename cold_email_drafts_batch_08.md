# Cold Email Drafts - Batch 08

Research date: 2026-05-12

Companies covered:
1. Apica
2. Atlan
3. Azul
4. Cloud.in
5. CloudThat

Cold-email rules used for this batch:
- Use formal application portals first for structured or services-led companies.
- Do not use sales, demo, support, or generic contact forms as recruiting channels unless only asking for routing after applying.
- Open with a current product/workflow reason, then back it with shipped systems and numbers.
- Be honest about fit gaps. Do not overclaim Java/JVM depth for Azul.
- Do not leave local file paths in the sent email/application body.

## 1. Apica

Best route: Apica careers page / current Bangalore engineering role application

Suggested subject: `Golang backend profile - telemetry pipeline systems`

Use resume: `tailored_resumes/full/apica_resume.pdf`

Attachment note: attach the PDF above in the formal application. Current role fit is strongest for Apica's Bangalore `Full Stack Engineer (Backend focused - Golang)` or `Senior Full Stack Engineer` roles.

Why this angle:
Apica's current careers page lists engineering work around telemetry pipeline services that ingest, mutate, enrich, route, and query large datasets, plus backend-focused Golang systems, distributed services, data pipelines, access control, observability, AI/LLM observability, high-cardinality metrics, and cost-aware telemetry. The strongest fit is Murdoc's OpenTelemetry/Prometheus gateway, Postificus's Go worker services, Swish traceability, and Bentham's production automation.

Application note:

```text
Hi Apica team,

I am interested in the backend-focused Golang engineering roles in Bangalore because Apica's current platform work around telemetry pipelines, observability data, AI/LLM observability, high-cardinality metrics, and cost-aware monitoring maps closely to the systems I have been building.

My strongest overlap is observability-heavy backend work. I built Murdoc, an AI/tool gateway, and instrumented AI/tool traffic with OpenTelemetry metrics/traces, Prometheus health checks, route profiles, and audit logs tying model/tool requests to policy outcomes. I built Postificus, a browser workflow platform, and worked on distributed Go services with RabbitMQ workers, DLQs, retries, Redis autosave, PostgreSQL persistence, Prometheus metrics, health checks, and circuit breakers around long-running browser jobs. I built Swish, an AI-assisted support workflow system, and worked on AI-assisted backend workflows with PostgreSQL/Redis state, retrieval-backed responses, confidence thresholds, human handoff paths, and traceable action records.

At my last internship at Bentham AI, I also containerized services, deployed to Google Cloud Run, and automated GitHub Actions releases, improving deployment velocity by 70%.

Would my profile be relevant for Apica's backend-focused Golang, telemetry pipeline, observability, or AI/LLM observability engineering work?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Apica team,

Quick bump. I think the fit is around backend services for telemetry data: OpenTelemetry traces, Prometheus metrics, route/audit records, retryable workers, service health, and Go/Python production systems.

Happy to send a short walkthrough of Murdoc or Postificus if useful.

Best,
Shuvam
```

## 2. Atlan

Best route: Atlan careers page / open role application

Suggested subject: `Backend/AI context layer profile`

Use resume: `tailored_resumes/full/atlan_resume.pdf`

Attachment note: attach the PDF above in the formal application. Atlan does not have a useful public founder/recruiting email in the dossier, so use the application route.

Why this angle:
Atlan's current positioning is explicitly around the enterprise context layer for AI: Enterprise Data Graph, Data Lineage, Data Marketplace, Context Agents, Context Engineering Studio, and Context Lakehouse. The strongest fit is Murdoc's context-preserving AI gateway, Penny Lane's checkpointed multi-agent workflow, Swish's traceable agent actions, and Bentham's workflow automation.

Application note:

```text
Hi Atlan team,

I am interested in backend / AI infrastructure roles at Atlan because your current direction around the context layer for enterprise AI is very close to the systems I have been building: preserving context, making agent actions inspectable, and turning workflow state into structured metadata that can be governed and replayed.

My strongest overlap is Murdoc, an AI gateway for LLM, HTTP-tool, and MCP traffic. It preserves context around prompts, tools, retrieved data, policy decisions, and outputs using structured traces and audit ledgers. I modeled runtime settings, route profiles, RBAC decisions, and attack-lab outcomes as explicit metadata so agent behavior could be governed, replayed, and debugged. I also built Penny Lane, a checkpointed multi-agent research workflow with analyst roles, debate, trader/risk review, memory, JSONL traces, validation harnesses, and 5 market baselines.

At my last internship at Bentham AI, I built a Puppeteer/Node.js workflow engine for MCA company-registration filings, reducing manual filing time by 85%, and separated workflow logic from delivery vendors through a concurrent Go notification service.

Would my profile be relevant for backend, AI context, metadata, governance, or agent-workflow infrastructure roles at Atlan?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Atlan team,

Quick bump. I think the fit is around AI context infrastructure: traceable agent actions, metadata-rich workflow state, auditability, checkpointing, governance rules, and backend systems that make context usable rather than hidden in prompts.

Happy to send a short walkthrough of Murdoc, Penny Lane, or Swish if useful.

Best,
Shuvam
```

## 3. Azul

Best route: Azul careers page / relevant role application

Suggested subject: `Platform/backend performance profile`

Use resume: `tailored_resumes/full/azul_resume.pdf`

Attachment note: attach the PDF above in the formal application. Use a platform/backend or tooling role if available; do not pitch yourself as a JVM specialist.

Why this angle:
Azul is a mature Java platform company focused on Azul Core, Azul Prime, Payara, Azul Intelligence Cloud, runtime performance, enterprise Java, cloud cost optimization, compliance, and production reliability. The strongest honest angle is backend/platform performance, cloud cost reduction, production service reliability, metrics, and distributed systems. The resume includes C++ as a language, but the proof is mainly Go/Python/backend infrastructure rather than deep Java/JVM internals.

Application note:

```text
Hi Azul team,

I am interested in platform/backend engineering roles at Azul because your work around Java runtime performance, cloud cost optimization, production reliability, and runtime intelligence matches the kind of infrastructure problems I want to work on.

My strongest experience is not deep JVM internals yet, so I am positioning myself for backend/platform, tooling, observability, or cloud-infrastructure roles rather than compiler/runtime-core roles. I built Seaweed, a coding-assessment platform, and worked on a Go/PostgreSQL backend for 500+ concurrent users and replaced a Redis + DynamoDB design with PostgreSQL materialized views, reducing infrastructure cost by about 70% while preserving low-latency reads. I built Postificus, a browser workflow platform, and worked on distributed Go services with RabbitMQ retries/DLQs, Redis state, PostgreSQL persistence, Prometheus metrics, health checks, and circuit breakers around long-running jobs. I also built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing to balance latency, throughput, and worker availability.

Would my profile be relevant for backend, platform tooling, cloud-cost, observability, or production reliability engineering roles at Azul?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Azul team,

Quick bump. I think the fit is around platform/backend systems where performance, service reliability, cloud cost, telemetry, and production operations matter.

Happy to send a short walkthrough of Seaweed, Postificus, or the distributed inference engine if useful.

Best,
Shuvam
```

## 4. Cloud.in

Best route: Cloud.in careers page / GreytHR `Apply Online`

Suggested subject: `Cloud/platform backend profile`

Use resume: `tailored_resumes/full/cloud_in_resume.pdf`

Attachment note: attach the PDF above in the formal application. Do not use `sales@cloud.in` for a job note; it is a sales/contact route.

Why this angle:
Cloud.in is a cloud services and managed-services company with offerings across security/compliance, consulting, migration, managed services, billing, automation/DevOps, content delivery/edge, disaster recovery, backup, big data/analytics, and AI/ML. Their expertise pages mention AWS services including CloudFront, Config, Systems Manager, RDS, WAF, DynamoDB, EKS, Kinesis, CloudFormation, Lambda, API Gateway, OpenSearch, Glue, and managed services. The strongest fit is managed cloud, platform support, backend services, CI/CD, service health, and AWS-adjacent reliability work.

Application note:

```text
Hi Cloud.in team,

I am interested in cloud/platform engineering roles at Cloud.in because your work spans the exact operational surface I want to grow in: managed cloud, automation and DevOps, AWS workloads, security/compliance, disaster recovery, big data/analytics, AI/ML, and production support for customer systems.

My strongest overlap is backend and platform delivery work. At my last internship at Bentham AI, I containerized backend services with Docker, deployed to Google Cloud Run, and automated CI/CD with GitHub Actions, improving deployment velocity by 70%. I built Postificus, a browser workflow platform, and worked on containerized Go microservices with asynchronous workers, RabbitMQ retries, Redis state, PostgreSQL persistence, health checks, and Prometheus-ready service metrics. I built Seaweed, a coding-assessment platform, and worked on backend services for registration, submissions, sandboxed execution, scoring, and ranked candidate shortlisting across 500+ concurrent users, using Go, PostgreSQL, Redis, Judge0, AWS, and Docker.

Would my profile be relevant for cloud engineering, DevOps, backend platform, managed services, or production reliability roles at Cloud.in?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Cloud.in team,

Quick bump. I think the fit is around cloud/platform delivery: containerized services, CI/CD, AWS-adjacent backend workloads, Prometheus metrics, service health, queue retries, and production support.

Happy to send a short walkthrough of Postificus, Seaweed, or my Bentham deployment work if useful.

Best,
Shuvam
```

## 5. CloudThat

Best route: CloudThat careers page / Keka role application

Suggested subject: `Cloud DevOps/backend platform profile`

Use resume: `tailored_resumes/full/cloudthat_resume.pdf`

Attachment note: attach the PDF above in the Keka application. Current closest fits are DevOps Engineer, Cloud Solution Architect, cloud security, or platform delivery roles depending on level.

Why this angle:
CloudThat is a cloud training and consulting company with work across cloud migration, DevOps/DevSecOps, data analytics, managed services, app modernization, AI/ML, cloud native, containerization, AWS, Microsoft, GCP, NVIDIA, and role listings around CI/CD, cloud architecture, Kubernetes, observability, GitOps, Terraform, AWS production systems, IAM/security, and monitoring/logging. The strongest fit is cloud consulting/platform delivery, containerized backend services, CI/CD, service health, observability, and AWS-oriented backend work.

Application note:

```text
Hi CloudThat team,

I am interested in cloud DevOps / platform engineering roles at CloudThat because your current consulting and hiring focus maps closely to my project work: cloud infrastructure, CI/CD, containerized services, observability, platform reliability, AI/ML workloads, and production support.

My strongest overlap is backend systems that are built to operate cleanly. At my last internship at Bentham AI, I containerized backend services with Docker, deployed to Google Cloud Run, and automated CI/CD with GitHub Actions, improving deployment velocity by 70%. I built Postificus, a browser workflow platform, and worked on Go microservices with asynchronous workers, RabbitMQ retries, Redis state, PostgreSQL persistence, health checks, and Prometheus-ready service metrics. I built Seaweed, a coding-assessment platform, and worked on backend services for registration, submissions, sandboxed execution, scoring, and ranked candidate shortlisting across 500+ concurrent users using Go, PostgreSQL, Redis, Judge0, AWS, and Docker. I also built Murdoc with OpenTelemetry metrics/traces, Prometheus health checks, route profiles, and replayable audit records.

Would my profile be relevant for cloud DevOps, backend platform, cloud consulting, observability, or production reliability roles at CloudThat?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi CloudThat team,

Quick bump. I think the fit is around cloud/platform delivery: CI/CD, Dockerized services, AWS-adjacent backend systems, observability, health checks, queue retries, and production support.

Happy to send a short walkthrough of Postificus, Seaweed, Murdoc, or my Bentham deployment work if useful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance reused from prior batches:
- Concise body, specific company-aware opening, proof-heavy middle, and one low-friction ask.
- For structured companies, use formal applications first. Use email only as a routing note when the route is clearly appropriate.

Company context checked:
- Apica: official careers page, current Bangalore engineering roles, telemetry pipeline / observability product context: https://www.apica.io/careers/
- Atlan: official careers page and current product positioning around Enterprise Data Graph, Context Agents, Context Engineering Studio, and Context Lakehouse: https://atlan.com/careers/
- Azul: official careers/about pages for Java platform, Azul Core, Azul Prime, Payara, Azul Intelligence Cloud, runtime performance, and cloud cost optimization: https://www.azul.com/careers/ and https://www.azul.com/about/
- Cloud.in: official careers page, GreytHR application route, offerings, AWS expertise, and sales/contact route classification: https://www.cloud.in/careers and https://www.cloud.in/expertise
- CloudThat: official careers page and Keka role pages for DevOps Engineer, Cloud Solution Architect, and Senior Cloud Security Engineer: https://www.cloudthat.com/careers/ and https://cloudthat.keka.com/careers/
