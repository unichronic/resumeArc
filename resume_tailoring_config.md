# Resume Tailoring Config

Use this file as the working checklist before creating or editing any tailored resume.

## Operating Rules

- Create a separate tailored `.tex` and `.pdf` for each company unless explicitly asked to modify an existing resume.
- Keep the existing LaTeX formatting intact. Prefer changing only project bullets, experience bullets, project tech stacks, and skills.
- Compile every final resume with `pdflatex` and verify the output is 1 page with `pdfinfo`.
- After compiling, inspect the PDF text with `pdftotext -layout` for ordering, wording, line breaks, and missing terms.
- If a live JD or company page is provided, verify it from the web before tailoring.
- Keep resumes genuine, grounded, and not over-bloated. Use strong phrasing, but avoid claims that look fake or too broad.
- Maintain reverse chronological order in Experience.
- Avoid writing bullets in the pattern `Built X: did Y`. Prefer natural sentences without colon-led explanations.
- Use bold highlights sparingly for key JD matches, metrics, or project anchors.
- Use JavaScript, TypeScript, React, Next.js, and Node.js first for full-stack roles unless the JD is clearly backend/infra/ML-heavy.
- For AI/full-stack roles, show both product engineering and AI systems work instead of making the resume look like a pure ML resume.

## Global Avoid List

- Do not mention Mistral or Presidio.
- Do not mention autonomous red-team or red-teaming projects unless the user explicitly reintroduces a real project.
- Do not add LangChain/LlamaIndex unless the project actually uses them or the user asks to include them after implementation.
- Do not over-pack the skills section with tools just because a JD mentions them.

## Preferred Skills Format

Use three rows only:

- `Languages`
- `Frameworks`
- `Tools`

For full-stack AI roles, preferred ordering:

- `Languages`: JavaScript, TypeScript, Python, Go
- `Frameworks`: React, Next.js, Node.js, GraphQL, Vite, FastAPI, Gin, Echo, PyTorch
- `Tools`: PostgreSQL/pgvector, Redis, SQLite, Vector Memory, Firebase Auth, Judge0, Docker, GCP, GitHub Actions, Langfuse, Prometheus

Adjust per JD. Remove irrelevant tools rather than listing everything.

## Project Inventory And Best Use

### Swish Support System

- Best for AI + product, RAG/context grounding, hybrid AI + rule-based workflows, support automation, observability/evals.
- Strongest framing: hybrid AI + rule-based logic system.
- Safe claims: LLM assessments classify messy complaint semantics; deterministic policy code controls refunds/replacements/escalations; context is grounded in order, item, evidence, customer, and policy data; agent memory/state survives clarifications and follow-ups; Langfuse traces and regression checks exist.
- Full-stack AI stack: JavaScript, React, Python, PostgreSQL/pgvector, Redis, Langfuse.
- Avoid making it sound like only a generic AI agent. Emphasize rules, context, auditability, regression tests, and product workflow.

### Penny Lane Capital

- Best for vector memory, multi-agent orchestration, semantic retrieval, RAG-style memory, evaluation loops, typed workflow state.
- Safe claims: Agno workflow, analyst/debate/trader/risk/portfolio roles, Pydantic state, SQLite checkpoints, JSONL traces, vector memory, semantic lesson retrieval, validation harnesses, reward-loop style evaluation.
- Preferred stack: Python, Agno, Pydantic, SQLite, Vector Memory, JSONL.
- Do not show `Local Embeddings` in the visible tech stack unless needed; `Vector Memory` is cleaner.

### Hyoka

- Best for AI-agent reliability, evaluation/replay infrastructure, self-improving agent loops, release gates, trace ingestion, operational dashboards, and framework-neutral AI observability.
- Safe claims: FastAPI API server; trace/event ingestion; OTLP/JSON ingestion for GenAI/OpenInference-style spans; OpenAI-compatible proxy; Python SDK; Typer CLI; SQLAlchemy/Alembic metadata model; SQLite local and Postgres production paths; worker-owned replay/eval execution with database leases; evaluator registry; failure mining; evidence-hashed candidate proposals; validation runs; gate decisions; promotions; content-addressed artifacts; signed manifests; API keys; audit logs; Next.js dashboard.
- Strongest framing: reliability control plane for AI agents that observes traces, evaluates behavior, replays candidates, and promotes safer configurations through explicit gates.
- Preferred stack: Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL, OpenTelemetry/OTLP, Typer, Next.js, TypeScript, Docker.
- Do not frame it as a model-training project. Emphasize infrastructure, evaluation, reproducibility, traceability, and safe promotion.

### Seaweed Contest Platform

- Best for full-stack product, React/Next.js UI, assessment platforms, coding/evaluation products, auth, admin dashboards, leaderboards.
- Safe claims: React/Next.js assessment UI, auth-gated problem pages, code editor, submissions, admin review/shortlisting, ranked leaderboards, Judge0 judging APIs, PostgreSQL rankings/materialized views.
- Metrics already used: 500+ concurrent users, sub-5s P95 verdict latency.
- Preferred stack: TypeScript, React, Next.js, Go, PostgreSQL, Judge0, Firebase.

### GSoC / Invesalius

- Best for ML pipelines, model inference, performance optimization, open-source engineering, mature-codebase debugging.
- Safe claims: Python medical-image segmentation tooling for 95 brain subparts, preprocessing, orientation correction, model inference, generated masks, large MRI data paths, PyTorch/ONNX-style inference, binary mask generation.
- Metrics already used: 87% runtime reduction through async/parallel execution.
- Keep as Experience, not Projects, unless the resume needs ML-heavy emphasis.

### Open Source Contributions

- Do not leave Open Source as only a generic project list when the role has a clear angle.
- For AI/ML/search roles: emphasize Invesalius model-output reliability, PyTorch/ONNX-style debugging, parsing robustness, security fixes, and maintainer-reviewed integration changes.
- For scientific/research roles: emphasize Invesalius, IOOS, and Tiled as scientific/data/visualization-adjacent systems; mention medical-imaging workflows, data/tooling robustness, compatibility, and security validation.
- For AI-agent/RAG/platform roles: emphasize Kuadrant MCP Gateway backend-outage grace handling, agent/tool reliability, Kyverno policy/infrastructure context, and maintainer-reviewed reliability/security code paths.
- For full-stack/customer engineering roles: emphasize UI/compatibility fixes, parsing robustness, Zip Slip path validation, backend integration behavior, and working across mature codebases under maintainer review.
- Keep this section to one strong bullet unless the resume has space; it should support the role without displacing stronger projects.

### Bentham AI

- Best for product engineering internship, AI-assisted workflow automation, backend orchestration, async workflows, deployment.
- Stronger AI framing: AI orchestration workflow for company-registration drafts with structured prompt outputs, operator validation, public-site API lookups, and automation handoff.
- Safe claims: retries, session recovery, browser automation, state validation, Docker, Google Cloud Run, GitHub Actions.
- Metrics already used: 85% manual filing time reduction, 70% deployment velocity improvement.

### Omni-SSM / SSM

- Best for speech/AI/ML roles, not general full-stack unless voice AI is relevant.
- Safe claims: Moonshine Hindi ASR tuning, STT/TTS research loop, SSAMBA streaming CTC, PyTorch, ONNX/runtime constraints, TTS evaluation, latency reports.
- Use only when the JD asks for speech, on-device ML, multilingual AI, inference, or AI/ML research.

### Postificus

- Best for full-stack/backend/product workflows, rich editor, async workers, publishing automation, queueing, reliability.
- Safe claims: React/Vite editor dashboard, Go/Echo backend, PostgreSQL, Redis, RabbitMQ, retries, DLQs, browser fallback, health checks, Prometheus.
- Use for full-stack/product roles when AI projects would make the resume too AI-heavy.

## Company / JD Matching Heuristics

- AI full-stack / RAG / vector DB roles: Hyoka, Swish, Penny Lane, Seaweed; lead with Hyoka for agent reliability/eval roles and Swish for product/RAG roles.
- Assessment / education / grading products: Swish, Seaweed, GSoC; include Penny Lane if RAG/vector DB is in the JD.
- Backend / infrastructure roles: Seaweed, Postificus, Bentham, Murdoc if observability/MCP is relevant.
- AI/ML research roles: GSoC, Hyoka, Penny Lane, Swish, Omni-SSM.
- Harness/testing roles: Playo-style resume should emphasize Seaweed, Swish regression/evals, GitHub Actions, Playwright/Cypress/Postman only if actually present or user confirms.
- Generic full-stack startup roles: Seaweed, Postificus, Swish; keep React/Next/TypeScript high and avoid making it too AI-heavy.

## Verification Commands

```bash
pdflatex -interaction=nonstopmode -halt-on-error <resume>.tex
pdfinfo <resume>.pdf | rg "Pages|File size"
pdftotext -layout <resume>.pdf - | sed -n '1,220p'
rg -n "Mistral|Presidio|red.?team|LangChain|LlamaIndex" <resume>.tex
rg -n "resumeItem\\{.*:" <resume>.tex
```
