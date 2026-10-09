# Cold Email Drafts - Batch 07

Research date: 2026-05-12

Companies covered:
1. ClickHouse
2. CockroachDB
3. Grafana Labs
4. Redis
5. YugabyteDB

Cold-email rules used for this batch:
- Use formal careers/application routes first for mature companies with structured hiring funnels.
- Do not use support, sales, press, security, or generic company inboxes for jobs.
- Keep the note technical and proof-heavy: product reason, matching shipped work, one low-friction ask.
- Do not leave local file paths in the sent email/application body.
- Avoid founder outreach here unless a current, public recruiting route is explicitly visible.

## 1. ClickHouse

Best route: ClickHouse careers page / relevant role application

Suggested subject: `Backend/data systems profile - real-time analytics`

Use resume: `tailored_resumes/full/clickhouse_resume.pdf`

Attachment note: attach the PDF above in the formal application. I did not verify a current recruiting email, so do not send this to a generic company inbox.

Why this angle:
ClickHouse is centered on high-performance real-time analytics, ClickHouse Cloud, Postgres-adjacent data workflows, observability through ClickStack, and AI/data infrastructure. The strongest fit is Seaweed's PostgreSQL materialized-view ranking system, Postificus metrics/retry architecture, Murdoc observability, and the distributed inference engine.

Application note:

```text
Hi ClickHouse team,

I am interested in backend/data systems roles at ClickHouse because the product direction sits exactly where I want to work: real-time analytics, high-volume observability data, cloud database infrastructure, and systems where query speed and operational reliability both matter.

My closest overlap is backend infrastructure around data-heavy services. I built Seaweed, a coding-assessment platform, and worked on a Go/PostgreSQL ranking backend for 500+ concurrent users using materialized views and concurrent refreshes, replacing a Redis + DynamoDB design and reducing infrastructure cost by about 70% while preserving low-latency leaderboard reads. I built Postificus, a browser workflow platform, and worked on Go services with RabbitMQ retries/DLQs, Redis autosave, PostgreSQL persistence, Prometheus metrics, health checks, and circuit breakers around long-running browser jobs. I also built Murdoc, an AI gateway instrumented with OpenTelemetry/Prometheus traces, metrics, and replayable audit records.

Would my profile be relevant for backend, cloud database, observability data, or infrastructure engineering roles at ClickHouse?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi ClickHouse team,

Quick bump. I think the fit is around backend systems for real-time analytics and observability: PostgreSQL-heavy data paths, materialized views, Prometheus/OpenTelemetry instrumentation, retryable workers, and cloud-deployed services.

Happy to send a short walkthrough of Seaweed, Postificus, or Murdoc if useful.

Best,
Shuvam
```

## 2. CockroachDB

Best route: Cockroach Labs careers page / relevant role application

Suggested subject: `Distributed backend systems profile`

Use resume: `tailored_resumes/full/cockroachdb_resume.pdf`

Attachment note: attach the PDF above in the formal application. Do not use `info@cockroachlabs.com` or `press@cockroachlabs.com` for hiring unless only asking for routing after applying.

Why this angle:
CockroachDB is a mature distributed SQL/database company focused on helping teams build and scale applications. The strongest fit is Seaweed's PostgreSQL-centered architecture, distributed inference orchestration, Postificus reliability patterns, and backend work around correctness, retries, and operational resilience.

Application note:

```text
Hi Cockroach Labs team,

I am interested in backend/database engineering roles at Cockroach Labs because CockroachDB's core problem space - distributed SQL, application scale, resilience, and correctness under operational pressure - maps closely to the backend systems work I have been building.

My strongest overlap is PostgreSQL-backed and distributed service reliability work. I built Seaweed, a coding-assessment platform, and worked on a Go/PostgreSQL ranking backend for 500+ concurrent users, using materialized views and concurrent refreshes to preserve live leaderboard behavior. I also replaced a Redis + DynamoDB design with a PostgreSQL-centered architecture, reducing infrastructure cost by about 70% while keeping ranking correctness and low-latency reads. I built Postificus, a browser workflow platform, and worked on Go services with RabbitMQ retries/DLQs, Redis state, PostgreSQL persistence, health checks, Prometheus metrics, and circuit breakers. I also built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing.

Would my profile be relevant for backend, database infrastructure, distributed systems, or reliability-focused engineering roles at Cockroach Labs?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Cockroach Labs team,

Quick bump. I think the fit is around distributed backend systems where correctness, retries, low-latency reads, PostgreSQL data modeling, and operational resilience are central to the product.

Happy to send a short walkthrough of Seaweed, Postificus, or the distributed inference engine if useful.

Best,
Shuvam
```

## 3. Grafana Labs

Best route: Grafana Labs careers page / Greenhouse application

Suggested subject: `OpenTelemetry/backend observability profile`

Use resume: `tailored_resumes/full/grafana_labs_resume.pdf`

Attachment note: attach the PDF above in the formal application. Grafana is a large remote-first company with structured hiring; keep this as application text rather than cold-emailing general inboxes.

Why this angle:
Grafana Labs is focused on observability, open-source infrastructure, Grafana Cloud, and remote-first engineering. The strongest fit is Murdoc's OpenTelemetry/Prometheus traces, metrics, audit logs, and AI workload observability; Postificus service metrics and health checks; Swish traceability; and open-source contribution history.

Application note:

```text
Hi Grafana Labs team,

I am interested in backend/observability engineering roles at Grafana Labs because your work around open-source observability, Grafana Cloud, and systems that make production behavior inspectable is very close to the infrastructure I have been building.

My strongest overlap is instrumentation-heavy backend work. I built Murdoc, an AI gateway for LLM, HTTP-tool, and MCP traffic with OpenTelemetry metrics/traces, Prometheus health checks, route profiles, and replayable audit records tying model/tool requests to policy outcomes. I built Postificus, a browser workflow platform, and worked on distributed Go services with RabbitMQ workers, DLQs, retries, Redis autosave, PostgreSQL persistence, Prometheus metrics, health checks, and circuit breakers around long-running jobs. I built Swish, an AI-assisted support workflow system, and traced high-risk support-agent decisions with Langfuse/local logs so actions stayed inspectable rather than prompt-only.

I have also contributed to Invesalius, IOOS, VideoLAN, CRIU, and Tiled, so I am comfortable working in open-source codebases with maintainer review.

Would my profile be relevant for backend, observability, OpenTelemetry, Prometheus, or AI workload observability roles at Grafana Labs?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Grafana Labs team,

Quick bump. I think the fit is around observability-heavy backend systems: OpenTelemetry traces, Prometheus metrics, service health, replayable audit records, and instrumentation for AI/tool workflows.

Happy to send a short walkthrough of Murdoc or Postificus if useful.

Best,
Shuvam
```

## 4. Redis

Best route: Redis careers page / relevant role application

Suggested subject: `Redis-backed backend systems profile`

Use resume: `tailored_resumes/full/redis_resume.pdf`

Attachment note: attach the PDF above in the formal application. I did not verify a current recruiting email, so use the role application route.

Why this angle:
Redis is focused on Redis Cloud, Redis Software, Redis Open Source for caching/streaming, and AI-oriented data products such as LangCache and context/semantic-cache workflows. The strongest fit is Redis-heavy backend work across Postificus, Seaweed, Swish, and the distributed inference engine.

Application note:

```text
Hi Redis team,

I am interested in backend/infrastructure roles at Redis because my strongest project work has been around Redis-backed systems, low-latency reads, real-time state, worker coordination, and AI/data paths where fast context access matters.

I built Postificus, a browser workflow platform, and worked on Go services with Redis autosave, RabbitMQ retries/DLQs, PostgreSQL persistence, Prometheus metrics, health checks, and circuit breakers around long-running browser jobs. I built Seaweed, a coding-assessment platform, and worked on a backend-heavy ranking system for 500+ concurrent users and replaced a Redis + DynamoDB design with PostgreSQL materialized views, reducing infrastructure cost by about 70% while preserving low-latency reads. I also built a distributed inference engine with Redis, streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing to balance latency, throughput, and worker availability.

Would my profile be relevant for backend, Redis Cloud, AI/context infrastructure, caching, or distributed systems engineering roles at Redis?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Redis team,

Quick bump. I think the fit is around Redis-backed backend systems: caching, durable job state, low-latency reads, worker coordination, service health, and AI/context infrastructure.

Happy to send a short walkthrough of Postificus, Seaweed, or the distributed inference engine if useful.

Best,
Shuvam
```

## 5. YugabyteDB

Best route: Yugabyte careers page / Greenhouse application

Suggested subject: `Distributed database/backend profile`

Use resume: `tailored_resumes/full/yugabytedb_resume.pdf`

Attachment note: attach the PDF above in the formal application. I did not verify a current recruiting email, so keep this to the application flow.

Why this angle:
YugabyteDB is a cloud-native distributed database company with PostgreSQL-compatible infrastructure, global/distributed teams, and India offices in Bangalore and Pune. The strongest fit is Seaweed's PostgreSQL-centered backend, materialized views and ranking correctness, Postificus reliability patterns, and the distributed inference engine's coordination work.

Application note:

```text
Hi Yugabyte team,

I am interested in backend/database engineering roles at Yugabyte because the product is exactly the kind of infrastructure work I want to grow into: PostgreSQL-compatible distributed databases, cloud-native reliability, low-latency reads, and systems that need to stay correct under real production load.

My closest overlap is PostgreSQL-backed backend and distributed service work. I built Seaweed, a coding-assessment platform, and worked on a Go/PostgreSQL ranking backend for 500+ concurrent users using materialized views and concurrent refreshes to preserve live leaderboard behavior. I also replaced a Redis + DynamoDB design with a PostgreSQL-centered architecture, reducing infrastructure cost by about 70% while keeping ranking correctness and low-latency reads. I built Postificus, a browser workflow platform, and worked on Go services with RabbitMQ retries/DLQs, Redis state, PostgreSQL persistence, health checks, Prometheus metrics, and failure isolation. I also built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing.

Would my profile be relevant for backend, distributed database, cloud infrastructure, or PostgreSQL-adjacent engineering roles at Yugabyte?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Yugabyte team,

Quick bump. I think the fit is around PostgreSQL-backed and distributed backend systems: ranking correctness, low-latency reads, retries, service health, and cloud-deployed infrastructure.

Happy to send a short walkthrough of Seaweed, Postificus, or the distributed inference engine if useful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance reused from prior batches:
- Concise body, specific company-aware opening, proof-heavy middle, and one low-friction ask.
- For structured companies, use formal applications first. Use email only as a routing note when the route is clearly appropriate.

Company context checked:
- ClickHouse: official careers page and current product/careers context: https://clickhouse.com/company/careers
- CockroachDB: official careers page and product/company context: https://www.cockroachlabs.com/careers/
- Grafana Labs: official careers page, remote-first hiring process, and observability positioning: https://grafana.com/careers/
- Redis: official careers page and current product areas including Redis Cloud, Redis Open Source, Redis for AI, LangCache, and context/semantic-cache roles: https://redis.io/company/careers/
- YugabyteDB: official careers page, distributed database positioning, open jobs route, and Bangalore/Pune presence: https://www.yugabyte.com/careers/
