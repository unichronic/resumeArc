# Project Inventory Gap Ideas For Company-Optimized Resumes

Research date: 2026-05-06

This is based on the company files in `tailored_resumes/`, the current project inventory under `/home/unichronic`, and product/feature research from official product pages, docs, careers pages, and the existing research files in this folder.

## Current Inventory Read

Your current projects already cover a lot of the market:

- `Murdoc`: strongest for AI security gateways, MCP/tool governance, observability, policy enforcement, and backend platform roles.
- `Tradeage / Penny Lane Capital`: strongest for multi-agent workflows, decision memory, evaluation traces, validation harnesses, and applied AI systems.
- `Swish Support System`: strongest for agentic support workflows, conversation memory, Langfuse traces, policy-grounded customer operations, and CX automation.
- `Postificus`: strongest for Go backend systems, browser automation, queues, workers, retries, observability, and publishing automation.
- `Seaweed / Recruit`: useful for backend/platform and evaluation-system signals, but less differentiated than the four above for the companies in this folder.
- `SSM`: currently not strong enough to carry a resume unless it is finished into a clear systems/security/data product.

The main missing inventory is not "more random apps". The gaps are specific proof-of-work projects around model routing, code-review evaluation, telemetry infra, Kubernetes/FinOps, metadata governance, browser-agent reliability, distributed data systems, and cloud/security graphs.

## Non-Clash Rules

These ideas should not be built or presented as clones of the target companies. They should be adjacent proof-of-work in the same technical domain.

- If an idea overlaps with an existing project, implement it as an extension to that project, not as a separate resume project.
- `Murdoc` should remain the AI security / MCP gateway project. Any routing, policy, or model-traffic work should deepen Murdoc instead of competing with it.
- `Postificus` should remain the browser automation / worker-system project. Any browser-agent reliability work should extend Postificus.
- `Swish Support System` should remain the support-agent workflow project. Any QA, memory, or eval work should deepen Swish.
- `Penny Lane Capital` should remain the multi-agent decision/evaluation project. Any agent-memory or evaluation work should either deepen Penny Lane or be clearly framed as a separate developer-tooling benchmark.
- New standalone projects should cover domains your current inventory does not cover: Kubernetes optimization, active metadata/lineage, distributed datastore benchmarking, cloud/supply-chain graph security, and edge data sync.
- Resume positioning should say "built adjacent systems in the same domain", not "rebuilt X company's product".

## Best New Projects To Add

### 1. Murdoc RouterLab: Model-Routing And MCP Policy Evaluation Extension

Do not build this as a separate project beside `Murdoc`. Build it as a `Murdoc` extension or benchmark lab that evaluates LLM/provider routing, policy enforcement, tool permissions, and observability under realistic workloads. This strengthens your existing AI gateway story without clashing with it.

Product research basis:
- OpenRouter emphasizes unified access to many AI models, fallbacks, provider routing, latency/throughput/price sorting, and model/provider selection.
- Kong is positioning around API + AI connectivity, AI Gateway, MCP registry, agent gateway, token budgets, semantic caching, cost control, and governance.
- Repello focuses on security for AI applications, agentic workflows, MCP connections, prompt injection, data exfiltration, runtime defenses, and policy controls.

Core features:
- A small routing/evaluation layer for your own AI workloads, not a commercial model marketplace clone.
- Provider fallback experiments, max-cost controls, latency/cost quality scorecards, and request replay for benchmark prompts.
- MCP server registry for local test tools with route-level allowlists, tool permission scopes, policy decisions, audit ledgers, and context-source labels.
- Prompt/tool-output risk checks, structured policy engine, rate limiting, token budgets, and per-team API keys.
- OpenTelemetry traces, Prometheus metrics, request logs with redaction, Langfuse traces for AI behavior, and dashboard-ready exports.
- CLI to run local eval suites against multiple providers and compare cost, latency, failure rate, and answer quality.

Tech stack:
- `Go` or `Python`, `FastAPI` or `Gin`, `PostgreSQL`, `Redis`, `MCP`, `OpenTelemetry`, `Prometheus`, `Docker`, `OPA/Rego-style policies`, `Langfuse`.

Resume use after implementation:
- "Extended Murdoc with a routing/evaluation lab for LLM traffic, adding provider fallback experiments, token budgets, MCP tool governance, audit logs, and OTel/Prometheus observability."
- "Added latency/cost/quality scorecards and replayable traces to compare model-provider behavior under policy-controlled AI workloads."

Best target companies:
- `openrouter`, `kong`, `repello_ai`, `atlan`, `coderabbit`, `mintlify`, `deccan_ai`, `testmu_ai`, `coralogix`, `apica`.

Priority:
- P0. This is the single highest-leverage extension because it upgrades Murdoc and helps AI infra, AI security, API gateway, and agent platform companies without creating a duplicate project.

### 2. ReviewBench: PR Review And Coding-Agent Evaluation Harness

Build a benchmark/evaluation system for AI code review and coding agents. This should not be a CodeRabbit clone or a toy GitHub bot. The useful artifact is the evaluation harness: datasets, scoring, false-positive analysis, and traceable review quality.

Product research basis:
- CodeRabbit highlights PR reviews, IDE/CLI reviews, codebase intelligence, linked issues, MCP/web context, linters/security scanners, learnings from reviewer feedback, unit test generation, docstrings, and custom checks.
- HackerRank is moving toward AI-era technical evaluation.
- TestMu AI has agentic testing, browser cloud, agent-to-agent testing, root-cause analysis, MCP server, and test insights.
- Deccan AI highlights coding evals, agentic tool-use data, RL environments, trace-level verifiers, production traces, rubrics, drift detection, and human/AI evaluation loops.

Core features:
- GitHub PR ingestion, diff parser, code graph extraction, changed-file dependency context, and issue-link context.
- Static analysis layer using `ruff`, `mypy`, `eslint`-style equivalents where relevant, `semgrep`, and custom project rules.
- LLM review layer with configurable rubrics for correctness, security, tests, maintainability, and spec adherence.
- Synthetic bug-injection suite and expected-findings dataset to measure precision, recall, severity calibration, and false positives.
- Feedback memory: accept/reject/ignore review comments and adapt future review rules.
- Output artifacts: PR summary, walkthrough, inline findings, generated tests, and evaluation report.

Tech stack:
- `Python`, `Go`, `GitHub API`, `tree-sitter`, `Semgrep`, `SQLite/PostgreSQL`, `FastAPI`, `OpenTelemetry`, `Langfuse`, `Docker`.

Resume use after implementation:
- "Built a PR-review evaluation harness that ingests GitHub diffs, combines static analysis with LLM review rubrics, and measures useful-comment precision, false positives, severity calibration, and generated-test coverage."
- "Implemented codebase-aware review context using AST/path rules, linked issue metadata, feedback memory, and replayable review traces."

Best target companies:
- `coderabbit`, `hackerrank`, `testmu_ai`, `deccan_ai`, `chainguard`, `mintlify`, `openrouter`, `browser_use`.

Non-clash positioning:
- This is a developer-tooling evaluation project, not a full AI review SaaS.
- It does not overlap with Penny Lane unless you reuse its evaluation-trace patterns; if you do, frame it as applying your eval-system experience to software engineering workflows.

Priority:
- P0 if CodeRabbit/HackerRank/TestMu/Deccan are high-priority applications.

### 3. TelemetryLake: OTel Pipeline, Trace Store, And Observability Control Plane

Build an observability lab that collects, routes, samples, stores, and replays telemetry from your own projects. This should be positioned as telemetry infrastructure, not as a SigNoz/Grafana/Coralogix clone and not just dashboards.

Product research basis:
- SigNoz is built around reducing signal/noise for developers and DevOps teams, with OpenTelemetry at the center.
- Apica is explicitly focused on agentic-ready telemetry, Flow/Lake/Observe/Fleet, high-cardinality metrics, synthetic checks, and AI-scale telemetry volumes.
- Coralogix emphasizes complete observability, index-free querying, infinite retention, APM, data shaping/governance, AI observability, evaluation, cost tracking, and guardrails.
- Grafana Labs is centered on full-stack observability for the agentic era.
- ClickHouse highlights observability, ClickStack, real-time analytics, vector search, GenAI, logs/metrics/traces, and long-term retention.

Core features:
- OTel collector receiver/processor/exporter pipeline for traces, logs, and metrics emitted by Murdoc, Postificus, Swish, and benchmark workloads.
- Sampling and routing policies by service, severity, customer, tenant, model/provider, and cost budget.
- ClickHouse-backed trace/log store with replay, service map, high-cardinality filtering, and dashboard queries.
- Prometheus remote-write path and Grafana dashboards.
- AI/agent trace schema for prompt, tool, model, policy, cost, latency, and failure reason.
- Synthetic workflow monitor for APIs, browser tasks, and agent tool calls.

Tech stack:
- `Go`, `OpenTelemetry Collector`, `ClickHouse`, `Prometheus`, `Grafana`, `Docker`, `PostgreSQL`, `RabbitMQ` or `Kafka-compatible queue`.

Resume use after implementation:
- "Built an OpenTelemetry control plane that routes, samples, stores, and replays service and AI-agent traces using ClickHouse, Prometheus, and Grafana dashboards."
- "Implemented high-cardinality telemetry controls, synthetic checks, and cost-aware routing for logs, metrics, traces, and agent events."

Best target companies:
- `signoz`, `grafana_labs`, `coralogix`, `apica`, `clickhouse`, `manageengine`, `ibm_cloudability`, `one2n`, `cast_ai`, `kong`.

Non-clash positioning:
- This does not replace the observability inside Murdoc or Postificus; it becomes the shared telemetry backend that ingests those projects.
- On resumes, use it when applying to observability companies; for non-observability companies, keep Murdoc/Postificus and mention OTel briefly inside those bullets.

Priority:
- P0 for infra/observability companies.

### 4. KubePilot: Kubernetes FinOps And Runtime Optimization Lab

Build a Kubernetes optimization lab that recommends and safely applies resource changes for your own services. This should show cloud/platform engineering skill without copying CAST AI or Cloudability.

Product research basis:
- CAST AI emphasizes application performance automation, SLO signals, latency/error/OOM monitoring, workload rightsizing, node scaling, spot management, GPU optimization, and autonomous remediation.
- IBM Cloudability is a cloud-cost/FinOps product.
- StackGen focuses on autonomous operations and infrastructure-from-code.
- One2N emphasizes reliability engineering and production systems.
- CloudThat, Cloud.in, NeoSOFT Cloud, i2k2, Shellkode, RemoteStar, and Concerto are cloud/platform/services targets where hands-on cloud optimization proof is useful.

Core features:
- Collect pod CPU/memory/network metrics and infer requests/limits recommendations.
- Detect OOM, throttling, noisy-neighbor patterns, underutilization, and SLO-risk changes.
- Generate Kubernetes patches, Helm values diffs, and Terraform variable suggestions.
- Safe rollout mode with dry-run, diff, approval, and rollback.
- Simulated spot interruption and node-pool rebalancing.
- Cost dashboard: estimated monthly waste, savings, risk score, and utilization.

Tech stack:
- `Go`, `Kubernetes API`, `Prometheus`, `OpenTelemetry`, `Helm`, `Terraform`, `Docker`, `kind/k3d`, `PostgreSQL`.

Resume use after implementation:
- "Built a Kubernetes FinOps controller that analyzes workload utilization, recommends CPU/memory rightsizing, detects SLO risk, and generates safe rollout patches with rollback support."
- "Implemented Prometheus-backed cost and reliability dashboards for throttling, OOMs, underutilization, and node-pool optimization."

Best target companies:
- `cast_ai`, `ibm_cloudability`, `stackgen`, `one2n`, `cloudthat`, `cloud_in`, `neosoft_cloud`, `i2k2`, `shellkode`, `remotestar`, `concerto_by_trianz`, `upwind`.

Non-clash positioning:
- This is a new standalone infra project because your current inventory does not strongly show Kubernetes, scheduling, or FinOps.
- Keep the scope to local/lab clusters and explain it as optimization tooling for your own services, not a commercial cloud optimization platform.

Priority:
- P0 if infra/platform roles are the focus.

### 5. MetaLineage: Active Metadata, Lineage, And Data Governance Graph

Build a metadata and lineage graph for your own project data, APIs, docs, traces, schemas, and agent outputs. This should demonstrate active metadata thinking without copying Atlan.

Product research basis:
- Atlan is an active metadata platform with governance, catalog, lineage, AI readiness, metadata automation, and integrations across the modern data stack.
- Pulse focuses on enterprise document intelligence and self-hosted document processing.
- Mintlify is positioning as an intelligent knowledge/docs platform where AI agents consume docs.
- Auctor focuses on implementation lifecycle context, project memory, handoffs, deliverables, scope creep, and connected systems.
- Work On Grid, Digital Paani, NeoDocs, Novaflow, Atlas, and Round Treasury all benefit from reliable operational data, workflow state, document extraction, and auditability.

Core features:
- Connectors for PostgreSQL, ClickHouse, CSV/Parquet, local docs, OpenAPI specs, and dbt-like lineage files.
- Metadata graph with assets, owners, schemas, upstream/downstream lineage, tags, policies, quality checks, and freshness.
- PII/sensitive-tag propagation, schema-drift detection, Slack/email-style notifications, and approval workflows.
- Search API and natural-language metadata assistant using retrieval over the graph.
- Document ingestion pipeline for PDFs/forms/invoices/lab reports/specs with structured extraction and provenance.
- Agent context API that returns trusted metadata, lineage, definitions, and quality warnings before an agent answers.

Tech stack:
- `Python`, `FastAPI`, `PostgreSQL`, `SQLite`, `ClickHouse`, `OpenAPI`, `Pydantic`, `SQLGlot`, `OpenTelemetry`, `Docker`, vector search via `pgvector` or `sqlite-vss`.

Resume use after implementation:
- "Built an active metadata control plane with dataset/API/doc connectors, lineage graph, schema-drift detection, policy-tag propagation, and retrieval APIs for AI agents."
- "Implemented document-to-structured-data extraction with provenance, quality checks, and audit-ready metadata for regulated workflows."

Best target companies:
- `atlan`, `pulse`, `mintlify`, `auctor`, `round_treasury`, `atlas`, `neodocs`, `novaflow`, `digital_paani`, `work_on_grid`, `sid`, `xurrent`.

Non-clash positioning:
- This is a new standalone data-platform project because your current inventory does not show lineage, metadata propagation, or governance deeply.
- It should use your own repos and generated datasets as the asset graph, not imitate Atlan's product UI or enterprise catalog.

Priority:
- P1 overall, but P0 if Atlan/data/document/workflow companies are your next applications.

### 6. BrowserFlow Bench: Browser Agent Reliability And Test Harness

Build a benchmark harness for browser automation reliability. This should extend `Postificus` rather than become a separate Browser Use clone or a new toy browser bot.

Product research basis:
- Browser Use explicitly focuses on web agents, browser automation at scale, stealth browsers, proxies, skill APIs, custom models, cloud browser APIs, and infrastructure/browser engineers.
- TestMu AI has browser cloud, Kane CLI, AI-native E2E testing, agentic testing cloud, visual testing, accessibility testing, and test insights.
- Deccan AI highlights agentic tool-use, browser/computer-use data, containerized RL environments, and trace-level verification.

Core features:
- Task suite for login, search, publish, form-fill, checkout, content extraction, and multi-tab workflows.
- Browser adapters for Go-Rod and Playwright/Puppeteer-compatible execution.
- Screenshot/video/DOM snapshots, retry traces, action timelines, and failure classifications.
- Flake detector and deterministic replay of failed browser steps.
- Synthetic "site variants" to test resilience against layout drift.
- Scorecards: success rate, time-to-completion, action count, retry count, DOM mismatch, and failure reason.

Tech stack:
- `Go`, `Python`, `Go-Rod`, `Playwright` or `Puppeteer`, `Docker`, `PostgreSQL`, `Redis`, `OpenTelemetry`, `Prometheus`.

Resume use after implementation:
- "Built a browser-agent reliability harness with deterministic task replay, screenshot/DOM traces, flake detection, layout-drift scenarios, and success-rate scorecards across browser automation backends."
- "Extended a Go-based publishing automation platform with queue-backed browser workers, retry traces, and Prometheus metrics for failed browser actions."

Best target companies:
- `browser_use`, `testmu_ai`, `deccan_ai`, `solidroad`, `coderabbit`, `openrouter`.

Non-clash positioning:
- This is a Postificus extension. Do not list it separately from Postificus unless it becomes large enough to stand alone.
- The domain is reliability/testing of browser automation, not "we built Browser Use."

Priority:
- P1, or P0 if Browser Use is the immediate target.

### 7. DataStore Lab: Distributed SQL, Cache, And Real-Time Analytics Benchmark Suite

Build a serious benchmark lab for databases and caches. It should show systems thinking: workload design, tail latency, failover, consistency tradeoffs, and operational observability. This is not a database product clone; it is a reproducible evaluation suite.

Product research basis:
- ClickHouse focuses on fast OLAP, real-time analytics, observability, ML/GenAI, vector search, and efficient compression/vectorized execution.
- CockroachDB emphasizes PostgreSQL compatibility, scale, resilience, strong consistency, regional failure survival, and compliance.
- Dragonfly and Redis are in-memory data/cache systems, with Redis also leaning into real-time data and AI memory/context.
- TiDB, YugabyteDB, and OceanBase are distributed SQL/database companies with AI-era positioning.
- Azul is Java runtime/performance focused, so a JVM workload driver is useful for that target.

Core features:
- Go workload generator for OLTP, OLAP, cache, queue-like access, time-series events, and vector/metadata lookup patterns.
- Database adapters for PostgreSQL, CockroachDB, YugabyteDB, TiDB, OceanBase-compatible SQL, ClickHouse, Redis, and Dragonfly.
- Measurements for p50/p95/p99 latency, throughput, failover time, consistency anomalies, memory usage, CPU, storage, and compression.
- Jepsen-lite failure scenarios: node kill, network delay, failover, replica lag, hot key, write skew.
- Dashboards and reproducible Docker Compose profiles.
- Optional Java workload driver for JVM/runtime optimization comparison.

Tech stack:
- `Go`, `Docker Compose`, `PostgreSQL`, `ClickHouse`, `Redis`, `Dragonfly`, `Prometheus`, `Grafana`, optional `Java`.

Resume use after implementation:
- "Built a reproducible distributed datastore benchmark suite covering SQL, OLAP, and cache workloads with p99 latency, failover, consistency, and resource-usage analysis."
- "Implemented fault-injection scenarios and dashboards to compare CockroachDB/Yugabyte/TiDB-style distributed SQL behavior with Redis/Dragonfly caching and ClickHouse analytics paths."

Best target companies:
- `clickhouse`, `cockroachdb`, `dragonfly`, `redis`, `tidb`, `yugabytedb`, `oceanbase`, `azul`.

Non-clash positioning:
- This is a new standalone systems project because your current inventory does not deeply show databases, caches, distributed SQL, or benchmark methodology.
- Keep it benchmark/evaluation focused; do not claim you built a replacement for Redis, ClickHouse, or CockroachDB.

Priority:
- P1. Excellent for database/systems targets, but narrower than the P0 projects.

### 8. SecureOps Graph: Cloud Asset, Supply Chain, IAM, And Runtime Security Graph

Build a cloud/security graph that ties together repos, builds, containers, runtime services, identities, devices, and exposed APIs. This can reuse Murdoc policy ideas, but it must be broader than AI traffic so it does not clash with Murdoc.

Product research basis:
- Chainguard focuses on trusted open source, secure software supply chain, images, CI/CD, and developer/AI coding agent security.
- Upwind focuses on cloud security for the AI and realtime era, runtime context, cloud assets, and risk.
- SubImage positions around cloud/security graph tooling and open-core security.
- miniOrange is IAM/security; Swif.ai is MDM/device compliance and shadow IT.
- Kong and Repello overlap through API/AI gateway security and runtime controls.

Core features:
- Ingest GitHub repos, container images, SBOMs, Kubernetes workloads, cloud-like asset JSON, IAM policies, and device posture records.
- Build graph of repo -> build -> image -> deployment -> service -> API/tool -> identity/device.
- Detect policy violations: unsigned image, stale dependency, public service, overbroad identity, risky tool permission, missing owner.
- Generate OPA/Rego-style policy results and remediation PRs.
- Produce dashboards for security posture, blast radius, owner mapping, and change history.

Tech stack:
- `Go`, `Python`, `PostgreSQL`, graph tables or `Neo4j` if desired, `Syft/Grype` or equivalent SBOM scanners, `OPA`, `Docker`, `Kubernetes`, `OpenTelemetry`.

Resume use after implementation:
- "Built a cloud/security graph linking repositories, SBOMs, container images, Kubernetes workloads, identities, APIs, and device posture to detect policy violations and generate remediation plans."
- "Implemented OPA-style controls for supply-chain, IAM, runtime exposure, and AI-tool permissions with audit trails and owner-aware risk reports."

Best target companies:
- `chainguard`, `upwind`, `subimage`, `miniorange`, `swif_ai`, `kong`, `repello_ai`, `stackgen`.

Non-clash positioning:
- Murdoc protects AI/tool/MCP traffic. SecureOps Graph maps software supply chain, cloud assets, IAM, devices, and runtime exposure.
- This should be framed as graph-based security analysis, not a clone of Chainguard, Upwind, SubImage, miniOrange, or Swif.ai.

Priority:
- P1, or P0 if cloud/security companies are the next push.

### 9. CX EvalOps: Support-Agent QA, Memory, And Policy Evaluation Platform

Build a realistic evaluation and observability layer for customer-support agents. This should extend `Swish Support System`; do not build it as a separate Solidroad clone.

Product research basis:
- Solidroad focuses on QA and training for human and AI agents, reviewing 100% of interactions, generating custom trainings, and improving support quality.
- Xurrent is AI-powered service and incident management.
- ManageEngine has IT operations/service management and AIOps surfaces.
- Auctor cares about context that survives handoffs and repeatable delivery.

Core features:
- Conversation simulator with refund/remake/escalation/safety/incident scenarios.
- Vector memory for previous customer interactions, order history, policy docs, and agent decisions.
- Rubric-based QA scoring: policy compliance, hallucination, resolution quality, escalation correctness, tone, evidence quality.
- Langfuse traces and local evaluation reports.
- Training scenario generation from failed conversations.
- Human-review workflow with issue tags and improvement suggestions.

Tech stack:
- `Python`, `Go`, `FastAPI`, `Gin`, `PostgreSQL`, `Redis`, `Langfuse`, `OpenTelemetry`, `pgvector`, `Docker`.

Resume use after implementation:
- "Built a support-agent QA platform with vector memory, rubric-based evaluation, policy compliance checks, Langfuse traces, and scenario generation from failed conversations."
- "Implemented multi-turn context management for support workflows, linking customer/order state, evidence artifacts, and deterministic policy outcomes."

Best target companies:
- `solidroad`, `xurrent`, `manageengine`, `auctor`, `testmu_ai`, `deccan_ai`.

Non-clash positioning:
- This is a Swish extension. It should strengthen the existing conversation-memory, policy, and Langfuse story.
- The domain is support-agent QA and evals on your own support simulator, not "we built Solidroad."

Priority:
- P1. Very strong for Solidroad/Xurrent, less useful for infra/database companies.

### 10. EdgeTrace: Edge Inference And Operational Data Sync

Build an edge-oriented telemetry and inference harness for data collected from simulated devices or field operations. This is lower priority unless you are targeting deeptech/IoT/utility companies, but it does not clash with your current inventory.

Product research basis:
- TsecondAI is edge/deeptech and mission-critical intelligence oriented.
- Digital Paani works around industrial water/wastewater deployments and operational data.
- Work On Grid focuses on AI-driven operational intelligence for utilities.

Core features:
- Local edge agent that buffers sensor/event data, runs lightweight model inference, and syncs when connectivity returns.
- Backpressure, deduplication, compression, and replay.
- OTel metrics for device/edge health, drift, queue depth, sync lag, and inference latency.
- Operational dashboard for anomaly alerts and audit logs.

Tech stack:
- `Go`, `Python`, `SQLite`, `MQTT` or `NATS`, `OpenTelemetry`, `Prometheus`, `Docker`, optional `ONNX Runtime`.

Resume use after implementation:
- "Built an edge data-sync and inference harness with offline buffering, replay, deduplication, OTel metrics, and operational dashboards for field-device workflows."

Best target companies:
- `tsecondai`, `digital_paani`, `work_on_grid`, `cloud_in`, `i2k2`, `shellkode`.

Non-clash positioning:
- This is a new standalone edge/IoT systems project because your current projects do not show offline sync, field telemetry, or edge inference.
- Use simulated sensors/events and your own operational dataset; do not copy a water, utility, or hardware company's product.

Priority:
- P2. Useful, but build only if those domain-specific roles become active.

## Company-To-Project Mapping

| Company file | Product angle from research | Best new project to add |
| --- | --- | --- |
| `apica_resume.tex` | Agentic-ready telemetry, routing, lake, observe, high-cardinality metrics, synthetic checks | `TelemetryLake`, optional `BrowserFlow Bench` |
| `atlas_resume.tex` / `Atlan.md` | Active metadata, catalog, governance, lineage, AI-ready data, connector framework | `MetaLineage` |
| `auctor_resume.tex` | Implementation lifecycle, context handoffs, deliverables, scope creep, connected systems | `MetaLineage`, `CX EvalOps` |
| `azul_resume.tex` | Java runtime performance, cloud cost optimization, JVM platform | `DataStore Lab` with Java workload driver |
| `browser_use_resume.tex` | Web agents, browser automation, cloud browsers, stealth/proxy/browser infra | `BrowserFlow Bench` |
| `cast_ai_resume.tex` | Kubernetes performance automation, rightsizing, SLO signals, node/GPU optimization | `KubePilot` |
| `chainguard_resume.tex` | Trusted OSS, supply chain, secure CI/CD, developer/AI coding security | `SecureOps Graph`, `ReviewBench` |
| `clickhouse_resume.tex` | Real-time analytics, observability, ClickStack, GenAI/vector search, efficient OLAP | `TelemetryLake`, `DataStore Lab` |
| `cloud_in_resume.tex` | Cloud services, managed workloads, NOC/platform operations | `KubePilot`, `EdgeTrace` |
| `cloudthat_resume.tex` | Cloud consulting, training, platform delivery | `KubePilot` |
| `cockroachdb_resume.tex` | Distributed SQL, PostgreSQL compatibility, resilience, scale, compliance | `DataStore Lab` |
| `coderabbit_resume.tex` | AI code review, PR/IDE/CLI reviews, codebase intelligence, linters, learnings | `ReviewBench` |
| `concerto_by_trianz_resume.tex` | Cloud/data/app transformation, enterprise platform delivery | `KubePilot`, `MetaLineage` |
| `coralogix_resume.tex` | Observability, index-free querying, AI observability, cost tracking, guardrails | `TelemetryLake` |
| `deccan_ai_resume.tex` | Training/eval data, RL environments, coding/browser/agentic evals, trace verifiers | `ReviewBench`, `BrowserFlow Bench` |
| `digital_paani_resume.tex` | Industrial/IoT operational data, deployments, monitoring | `EdgeTrace`, `MetaLineage` |
| `dragonfly_resume.tex` | In-memory datastore/cache, Redis-compatible performance | `DataStore Lab` |
| `grafana_labs_resume.tex` | Full-stack observability, dashboards, metrics/logs/traces, open source | `TelemetryLake` |
| `hackerrank_resume.tex` | Technical evaluation, AI-era assessment, developer tooling | `ReviewBench` |
| `i2k2_resume.tex` | Managed cloud, hosting, infrastructure and security services | `KubePilot`, `SecureOps Graph` |
| `ibm_cloudability_resume.tex` | Cloud cost management and FinOps | `KubePilot` |
| `kong_resume.tex` | API + AI connectivity, AI Gateway, MCP registry, context, token/cost governance | `Murdoc RouterLab` |
| `manageengine_resume.tex` | ITOps, service management, observability/AIOps, enterprise infra software | `TelemetryLake`, `CX EvalOps` |
| `miniorange_resume.tex` | IAM, identity security, access governance | `SecureOps Graph` |
| `mintlify_resume.tex` | Intelligent knowledge/docs platform, docs for AI agents, developer tooling | `MetaLineage`, `ReviewBench` |
| `neodocs_resume.tex` | Health data, diagnostics, document/data product | `MetaLineage` |
| `neosoft_cloud_resume.tex` | Cloud consulting/platform delivery | `KubePilot` |
| `novaflow_resume.tex` | Bioinformatics workflows, scientific data analysis | `MetaLineage` |
| `oceanbase_resume.tex` | Distributed database, AI-era unified database | `DataStore Lab` |
| `one2n_resume.tex` | SRE, DevOps, production reliability, platform engineering | `KubePilot`, `TelemetryLake` |
| `openrouter_resume.tex` | Unified AI model API, model/provider routing, fallbacks, latency/cost controls | `Murdoc RouterLab` |
| `pulse_resume.tex` | Enterprise document intelligence, self-hosted processing, evals/workflows | `MetaLineage` |
| `redis_resume.tex` | Real-time data, cache/database, AI memory/context | `DataStore Lab` |
| `remotestar_resume.tex` | Remote engineering/AI hiring platform, broad backend/cloud delivery | `KubePilot`, `ReviewBench` |
| `repello_ai_resume.tex` | AI app security, MCP/agent workflow protection, runtime policy controls | `Murdoc RouterLab`, `SecureOps Graph` |
| `round_treasury_resume.tex` | Finance automation, treasury, AP, payroll, workflow builder, approvals | `MetaLineage` |
| `shellkode_resume.tex` | Cloud/data/AI services and delivery | `KubePilot`, `EdgeTrace` |
| `sid_resume.tex` | Retrieval and AI infrastructure | `MetaLineage`, `Murdoc RouterLab` |
| `signoz_resume.tex` | OpenTelemetry, logs/metrics/traces, signal/noise, observability backend | `TelemetryLake` |
| `solidroad_resume.tex` | QA/training for human and AI support agents, interaction review, simulations | `CX EvalOps` |
| `stackgen_resume.tex` | Autonomous operations, infrastructure-from-code, platform/DevOps | `KubePilot`, `SecureOps Graph` |
| `subimage_resume.tex` | Cloud/security graph, open-core security tooling | `SecureOps Graph` |
| `swif_ai_resume.tex` | Device compliance, MDM, shadow IT, endpoint/security workflows | `SecureOps Graph` |
| `testmu_ai_resume.tex` | Agentic testing cloud, browser cloud, agent-to-agent testing, MCP, test insights | `BrowserFlow Bench`, `ReviewBench` |
| `tidb_resume.tex` | Distributed SQL, real-time/AI-native data platform | `DataStore Lab` |
| `tsecondai_resume.tex` | Edge/deeptech AI systems and mission-critical intelligence | `EdgeTrace` |
| `upwind_resume.tex` | Runtime cloud security, AI/realtime cloud security posture | `SecureOps Graph`, `KubePilot` |
| `work_on_grid_resume.tex` | Utility operational intelligence, data platform, AI-native workflows | `EdgeTrace`, `MetaLineage` |
| `xurrent_resume.tex` | AI-powered service/incident management and workflow automation | `CX EvalOps`, `TelemetryLake` |
| `yugabytedb_resume.tex` | AI-ready distributed PostgreSQL, cloud-native database | `DataStore Lab` |

## Recommended Build Order

If the goal is maximum resume leverage across the whole folder, build or extend in this order:

1. `Murdoc RouterLab`: upgrades Murdoc and targets OpenRouter, Kong, Repello, Atlan-adjacent AI governance, and AI infra companies.
2. `TelemetryLake`: shared telemetry lab for your existing services; targets SigNoz, Grafana, Coralogix, Apica, ClickHouse, ManageEngine, and infra roles.
3. `ReviewBench`: targets CodeRabbit, HackerRank, TestMu AI, Deccan AI, and AI-eval/devtool roles.
4. `KubePilot`: targets CAST AI, Cloudability, StackGen, One2N, cloud/platform/services companies.
5. `MetaLineage`: targets Atlan, Pulse, Mintlify, Auctor, Round Treasury, NeoDocs, Novaflow, Work On Grid, and document/data workflow companies.
6. `BrowserFlow Bench`: Postificus extension; targets Browser Use and TestMu AI, and improves browser-automation credibility.
7. `DataStore Lab`: targets database companies.
8. `SecureOps Graph`: targets Chainguard, Upwind, SubImage, miniOrange, Swif.ai.
9. `CX EvalOps`: Swish extension; targets Solidroad, Xurrent, ManageEngine, and agent-support roles.
10. `EdgeTrace`: targets TsecondAI, Digital Paani, Work On Grid, and IoT/edge roles.

If you only have time for three, build:

- `Murdoc RouterLab`
- `TelemetryLake`
- `ReviewBench`

Those three cover the highest-value AI/backend/infra/devtool companies in the folder and can reuse your existing Murdoc, Swish, Postificus, and Penny Lane code.

## Source Notes

Primary research sources used:

- Existing local research: `backend_infra_ai_deep_research.md`, `backend_infra_ai_rankings.md`, `startup_backend_infra_ai_tiers.md`, `startup_research.md`.
- OpenRouter docs: https://openrouter.ai/docs/quickstart and https://openrouter.ai/docs/guides/routing/provider-selection
- CodeRabbit product/docs: https://www.coderabbit.ai/ and https://docs.coderabbit.ai/
- Browser Use careers/product surface: https://browser-use.com/careers
- Solidroad product: https://www.solidroad.com/
- SigNoz about/product: https://signoz.io/about-us/ and https://signoz.io/
- Repello product: https://repello.ai/
- CAST AI product: https://cast.ai/
- Apica product: https://www.apica.io/
- Coralogix product: https://coralogix.com/
- ClickHouse product: https://clickhouse.com/
- Kong product: https://konghq.com/
- Auctor product: https://www.getauctor.com/
- Round Treasury product: https://www.roundtreasury.com/
- Deccan AI product: https://www.deccan.ai/
- TestMu AI product: https://www.testmuai.com/
- Atlan product research via official search results: https://atlan.com/active-data-governance/ and https://atlan.com/active-metadata-101/
- Database/security/cloud company pages checked: CockroachDB, Dragonfly, Redis, TiDB/PingCAP, YugabyteDB, OceanBase, Chainguard, Upwind, SubImage, miniOrange, Swif.ai, Azul, CloudThat, Cloud.in, NeoSOFT Cloud, i2k2, Shellkode, RemoteStar, Work On Grid, Digital Paani, Novaflow, Xurrent.
