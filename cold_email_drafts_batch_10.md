# Cold Email Drafts - Batch 10

Research date: 2026-05-12

Companies covered:
1. SID
2. Solidroad
3. SubImage
4. TiDB / PingCAP
5. Upwind

Cold-email rules used for this batch:
- Use official careers/application routes first.
- If no current role or reliable recruiting route is visible, hold the draft until a route opens.
- Do not use sales/demo/support/security/press inboxes for jobs.
- Keep each note tied to current product context and the matching tailored resume.
- Do not leave local file paths in the sent email/application body.

## 1. SID

Best route: YC jobs page / current Research Intern application

Suggested subject: `AI retrieval systems / research intern profile`

Use resume: `tailored_resumes/full/sid_resume.pdf`

Attachment note: attach the PDF above in the YC application. I did not verify a public recruiting email, so treat this as application text.

Why this angle:
SID is an AI research lab for retrieval. Current public context says SID trains models that retrieve and reason over any data source, with SID-1 positioned as an agentic retrieval model that searches, reads, and refines queries, and is available through API, AWS Bedrock, and self-hosted deployment. The current YC route lists a Research Intern role for Summer 2026. The strongest fit is the distributed inference engine, Murdoc's LLM/tool gateway and tracing, Penny Lane's multi-agent evaluation workflow, and GSoC model/inference work.

Application note:

```text
Hi SID team,

I am interested in the Research Intern role because SID's work on agentic retrieval is close to the systems I have been building: LLM routing, retrieval-aware context, latency-sensitive inference, checkpoints, and evaluation workflows where model behavior has to be inspected rather than treated as a black box.

My strongest overlap is the distributed inference engine I built to run models larger than a single consumer GPU by coordinating token generation across heterogeneous nodes. I designed streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing to balance latency, throughput, and worker availability. I also built Murdoc, an AI gateway for LLM, HTTP-tool, and MCP traffic with route profiles, runtime policy checks, request scoring, replayable decisions, OpenTelemetry traces, Prometheus metrics, audit ledgers, and attack-lab validation. I built Penny Lane, a checkpointed multi-agent research workflow with analyst roles, debate, memory, JSONL traces, validation harnesses, and 5 baselines.

At GSoC, I also built model-backed MRI segmentation tooling for 95 anatomical regions and reduced runtime by 87% through async/parallel execution over large medical volumes.

Would my profile be relevant for retrieval systems, model-serving infrastructure, evaluation workflows, or research engineering work at SID?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi SID team,

Quick bump. I think the fit is around retrieval and model-systems work: streaming inference, routing, checkpoints, agent traces, evaluation harnesses, and latency-aware orchestration.

Happy to send a short walkthrough of the distributed inference engine, Murdoc, or Penny Lane if useful.

Best,
Shuvam
```

## 2. Solidroad

Best route: Solidroad careers page / Ashby role application

Suggested subject: `AI support evaluation/backend profile`

Use resume: `tailored_resumes/full/solidroad_resume.pdf`

Attachment note: attach the PDF above in the formal application. Current engineering roles are San Francisco or Dublin on-site, so check location fit before applying.

Why this angle:
Solidroad is building AI for customer experience, customer conversation analysis, coaching/training, quality assurance, real-time simulations, and support performance improvement. Current engineering roles mention prompt/retrieval pipelines, customer conversations, integrations like Zendesk/Intercom/Salesforce, real-time multimodal simulations, and fast product iteration. The strongest fit is Swish's AI support workflow with policy-correct resolution metrics, Murdoc's AI security/traceability, and Penny Lane's evaluation harnesses.

Application note:

```text
Hi Solidroad team,

I am interested in product/backend engineering roles at Solidroad because the product is very close to work I have already built: AI-assisted support workflows, conversation evaluation, policy-aware decisions, traceability, and improving customer outcomes without blindly handing everything to a model.

My strongest overlap is Swish, an AI support system with per-conversation context for active item, issue type, requested resolution, pending confirmations, and evidence artifacts. It achieved 85%+ policy-correct resolutions on a 50-case evaluation set and reduced compensation leakage by 25% versus a naive refund baseline by separating semantic understanding from deterministic policy. I also traced high-risk cases with Langfuse so decisions could be inspected and improved. I built Murdoc, an AI/tool gateway, and worked on LLM/tool security, blocking 90%+ of prompt-injection and unsafe-tool attempts across a 150-case attack corpus with false positives under 5%, while logging policy decisions through OpenTelemetry, Prometheus, and audit ledgers.

I think the fit is around AI QA, conversation scoring, support workflow simulation, product instrumentation, and backend systems that turn customer interactions into reliable coaching signals.

Would my profile be relevant for product engineering, AI support tooling, conversation evaluation, or backend systems roles at Solidroad?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Solidroad team,

Quick bump. I think the fit is around AI support quality systems: conversation state, policy-correct decisions, eval sets, traceability, support simulation, and product feedback loops.

Happy to send a short walkthrough of Swish, Murdoc, or Penny Lane if useful.

Best,
Shuvam
```

## 3. SubImage

Best route: monitor SubImage careers / YC jobs page; no current YC-posted job found

Suggested subject: `Security backend / open-source profile`

Use resume: `tailored_resumes/full/subimage_resume.pdf`

Attachment note: hold this until a role or reliable recruiting route appears. The YC jobs page currently shows no posted roles, and I did not verify a company-approved recruiting email.

Why this angle:
SubImage is an open-core alternative to Wiz built around the Cartography open-source project, with attack path analysis, vulnerability management, CSPM, AI asset inventory, and cloud/security graph context. The strongest fit is Murdoc's AI security gateway, policy enforcement, RBAC, PII redaction, OpenTelemetry/Prometheus auditability, Postificus backend reliability, and open-source contribution history.

Hold-until-route-opens note:

```text
Hi SubImage team,

I am interested in security/backend engineering roles at SubImage because your work around attack path analysis, vulnerability management, CSPM, AI asset inventory, and Cartography-style infrastructure mapping lines up with the security and observability systems I have been building.

My strongest overlap is Murdoc, a self-hosted AI security gateway for LLM, HTTP-tool, and MCP traffic. It blocks 90%+ of prompt-injection and unsafe-tool attempts across a 150-case attack corpus with false positives under 5%. I added route profiles, RBAC runtime settings, PII redaction, allow/block rules, OpenTelemetry metrics/traces, health checks, and audit ledgers for 100% of policy decisions. I built Postificus, a browser workflow platform, and worked on containerized Go services with asynchronous workers, RabbitMQ retries, Redis state, PostgreSQL persistence, health checks, and Prometheus-ready metrics around unreliable external integrations. I have also contributed to Invesalius, IOOS, VideoLAN, CRIU, and Tiled, so I am comfortable working in established open-source codebases with maintainer review.

Would my profile be relevant if you open backend, security tooling, infrastructure graph, or open-source engineering roles?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up only if a real contact replies:

```text
Hi SubImage team,

Quick bump. I think the fit is around security backend systems: infrastructure context, policy enforcement, audit logs, RBAC, OpenTelemetry, and reliable Go/Python services around security workflows.

Happy to send a short walkthrough of Murdoc or Postificus if useful.

Best,
Shuvam
```

## 4. TiDB / PingCAP

Best route: TiDB careers page / official role application when positions reopen

Suggested subject: `Distributed database/backend systems profile`

Use resume: `tailored_resumes/full/tidb_resume.pdf`

Attachment note: hold this until a matching role appears. The global careers page currently shows no jobs for the selected filters, so do not send this to support/sales/contact routes.

Why this angle:
TiDB is an open-source distributed SQL database for transactional, AI, and modern applications, with TiDB Cloud, TiDB Self-Managed, TiKV, agentic AI memory, vector search/RAG, lower infrastructure costs, operational intelligence, horizontal scaling, and open-source distributed database internals. The strongest fit is Seaweed's PostgreSQL materialized-view work and 70% infra cost reduction, the distributed inference engine, and Postificus service reliability.

Hold-until-role-opens note:

```text
Hi TiDB / PingCAP team,

I am interested in backend / database engineering roles at TiDB because the product sits directly in the space I want to grow in: distributed SQL, open-source database internals, transactional workloads, AI data infrastructure, horizontal scaling, query performance, and lower-cost operational systems.

My strongest overlap is backend data systems work. I built Seaweed, a coding-assessment platform, and worked on a Go/PostgreSQL ranking backend for 500+ concurrent users using materialized views and concurrent refreshes to preserve live leaderboard behavior. I also replaced a Redis + DynamoDB design with a PostgreSQL-centered architecture, reducing infrastructure cost by about 70% while keeping ranking correctness and low-latency reads. I built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing to balance latency, throughput, and worker availability. I built Postificus, a browser workflow platform, and worked on Go services with RabbitMQ retries/DLQs, Redis state, PostgreSQL persistence, Prometheus metrics, health checks, and circuit breakers around long-running jobs.

Would my profile be relevant for backend, distributed database, AI data infrastructure, query performance, or cloud database engineering roles when a matching opening is available?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up only if a recruiter/hiring contact replies:

```text
Hi TiDB / PingCAP team,

Quick bump. I think the fit is around database-backed systems: PostgreSQL-heavy data paths, materialized views, query-performance tradeoffs, infrastructure cost reduction, low-latency reads, and service reliability.

Happy to send a short walkthrough of Seaweed, Postificus, or the distributed inference engine if useful.

Best,
Shuvam
```

## 5. Upwind

Best route: Upwind careers page / relevant engineering or security role application

Suggested subject: `Runtime security/backend profile`

Use resume: `tailored_resumes/full/upwind_resume.pdf`

Attachment note: attach the PDF above in the formal application. Current strongest route is the careers page; relevant roles include backend engineering, AI engineering, security research, and Senior Cloud Security Validation Engineer in India.

Why this angle:
Upwind is a CNAPP/cloud security company covering build/run/protect: IaC security, supply chain security, containers admission control, CSPM, attack path and exposure management, CIEM, vulnerability management, DSPM, container/Kubernetes security, AI-SPM, serverless security, AI security, CDR, API security, DAST, and incident response. The strongest fit is Murdoc's AI security gateway and policy enforcement, distributed inference/runtime orchestration, and Postificus service reliability.

Application note:

```text
Hi Upwind team,

I am interested in backend / cloud security engineering roles at Upwind because your platform spans the exact security surface I want to work on: runtime visibility, cloud security posture, attack paths, vulnerability management, AI security, API security, incident response, and policy-aware protection for modern infrastructure.

My strongest overlap is Murdoc, a self-hosted AI security gateway for LLM, HTTP-tool, and MCP traffic. It blocks 90%+ of prompt-injection and unsafe-tool attempts across a 150-case attack corpus with false positives under 5%. I added route profiles, RBAC runtime settings, PII redaction, allow/block rules, OpenTelemetry metrics/traces, health checks, and audit ledgers for 100% of policy decisions. I also built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing, and Postificus, containerized Go services with retries, Redis/PostgreSQL state, Prometheus metrics, health checks, and failure isolation.

Would my profile be relevant for backend, runtime security, AI security, cloud security validation, or observability-heavy engineering roles at Upwind?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if a recruiter/hiring contact replies but goes quiet:

```text
Hi Upwind team,

Quick bump. I think the fit is around runtime security and backend systems: policy enforcement, attack validation, RBAC, audit logs, OpenTelemetry, service health, and reliable cloud-deployed services.

Happy to send a short walkthrough of Murdoc, the distributed inference engine, or Postificus if useful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance reused from prior batches:
- Concise body, specific company-aware opening, proof-heavy middle, and one low-friction ask.
- For structured companies, use formal applications first. Use email only as a routing note when the route is clearly appropriate.
- For companies with no current route, save the note until a reliable role or contact route appears.

Company context checked:
- SID: YC company page, current Research Intern role, SID-1 launch context, and docs: https://www.ycombinator.com/companies/sid and https://docs.sid.ai/start/landing
- Solidroad: official careers page and current Ashby engineering roles: https://www.solidroad.com/careers
- SubImage: official about/careers link and YC jobs page showing no current YC-posted roles: https://www.subimage.io/about/ and https://www.ycombinator.com/companies/subimage/jobs
- TiDB / PingCAP: official careers page, product context, and no current global open positions shown: https://www.pingcap.com/careers/
- Upwind: official careers page and current engineering/security roles: https://www.upwind.io/careers
