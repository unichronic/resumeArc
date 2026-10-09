# Cold Email Drafts - Batch 03

Research date: 2026-05-12

Companies covered:
1. Digital Paani
2. OpenRouter
3. CodeRabbit
4. One2N
5. Shellkode

Cold-email rules used for this batch:
- Keep the first email short, plain text, and easy to skim.
- Open with a real company-specific reason, not generic praise.
- Lead with proof: shipped systems, metrics, project links, or open-source work.
- Make one low-friction ask.
- Prefer a hiring/careers route over a support inbox when one exists.
- Do not leave local file paths in the sent email body.

## 1. Digital Paani

Recommended route: `contact@digitalpaani.com`

Founder route if sending a mission-specific note: `mansi.jain@digitalpaani.com`

Suggested subject: `Backend workflows for water operations`

Use resume: `tailored_resumes/full/digital_paani_resume.pdf`

Attachment note: attach the PDF above. Digital Paani's site explicitly asks candidates to send a resume plus a brief 1-2 minute pitch, so this can be a resume-forward note.

Why this angle:
Digital Paani is building lifecycle management software for wastewater treatment and water operations, with a need for operational data, monitoring, workflows, and reliable deployment across real facilities. The strongest fit is backend workflow reliability from Bentham, Postificus, Swish, and Seaweed.

Email:

```text
Hi Mansi and Digital Paani team,

I saw Digital Paani is fixing wastewater treatment by turning plant operations into monitored, software-driven workflows. The part that stood out to me is that this is not just a dashboard problem: deployments across buildings and factories need reliable operational data, external integrations, alerts, and workflows that keep working in the field.

My background is backend workflow automation. At my last internship at Bentham AI, I built Puppeteer/Node workflows for MCA company-registration filings that reduced manual filing time by 85%, plus Go services and Cloud Run/GitHub Actions deployments that improved release velocity by 70%. I also built Postificus, a Go/RabbitMQ workflow system with retries, durable job state, Redis/PostgreSQL, and Dockerized services, and Swish, an AI-assisted workflow system with traceable actions and human handoffs.

Would my profile be relevant for backend/platform engineering at Digital Paani?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Mansi and Digital Paani team,

Quick bump. The specific overlap I see is backend reliability for operational workflows: data ingestion, retries, alerts, durable state, and making field processes visible enough to act on.

Happy to send a short walkthrough of Postificus or Swish if useful.

Best,
Shuvam
```

## 2. OpenRouter

Best route: OpenRouter careers/open positions page

Cold-routing fallback: support ticket or `support@openrouter.ai`, asking to forward to engineering hiring

Suggested subject: `LLM routing + backend infra work`

Use resume: `tailored_resumes/full/openrouter_resume.pdf`

Attachment note: if using a form, attach the PDF above. If using support as a routing fallback, include GitHub and ask for forwarding rather than treating support like a hiring inbox.

Why this angle:
OpenRouter is a unified API for model access with routing, fallback, billing, usage analytics, provider abstraction, and developer-platform concerns. The strongest fit is the distributed inference engine, Murdoc AI gateway, and backend provider-abstraction work at Bentham.

Email:

```text
Hi OpenRouter team,

I am reaching out because OpenRouter's core problem is exactly the kind of backend/AI-infra work I want to do: unified model access, provider routing, fallbacks, usage tracking, and developer-facing APIs where reliability and latency matter.

My strongest overlap is infrastructure around model/tool traffic. I built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing across heterogeneous workers. I also built Murdoc, a FastAPI AI gateway for LLM, HTTP-tool, and MCP traffic with route profiles, policy checks, OpenTelemetry traces, Prometheus metrics, and replayable decisions. At my last internship at Bentham AI, I built a Go notification service with provider abstraction and strict validation.

Would my profile be relevant for backend, infra, or developer-platform engineering work at OpenRouter?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Support-route version if there is no direct hiring email:

```text
Hi OpenRouter support team,

I know this may not be the ideal hiring route, but I could not find a direct engineering recruiting email. Could you forward this to the right person if relevant?

I am interested in backend/AI-infra work around model routing, provider fallback, usage tracking, and developer-facing APIs. I have built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing, plus Murdoc, a FastAPI AI gateway with OpenTelemetry traces, Prometheus metrics, route profiles, policy checks, and replayable decisions.

GitHub: https://github.com/unichronic

Best,
Shuvam Pal
```

Follow-up if no reply after 5-7 days:

```text
Hi OpenRouter team,

Quick bump. The specific overlap is routing/fallback infrastructure for model traffic: provider abstraction, streaming APIs, retries, latency/throughput tradeoffs, and traceable request behavior.

Happy to send a short technical walkthrough if useful.

Best,
Shuvam
```

## 3. CodeRabbit

Recommended route: `careers@coderabbit.ai`

Backup route: CodeRabbit careers/open roles page

Suggested subject: `AI code review + evaluation systems`

Use resume: `tailored_resumes/full/coderabbit_resume.pdf`

Attachment note: attach the PDF above. `careers@coderabbit.ai` appears in CodeRabbit's own Series A hiring post, which is cleaner than using support.

Why this angle:
CodeRabbit is building AI-powered code reviews and quality gates across PR, IDE, CLI, OSS, and developer workflows. The strongest fit is Seaweed's coding evaluation system, Murdoc's traceable AI/tool behavior, Penny Lane's multi-agent evaluation, and open-source review experience.

Email:

```text
Hi CodeRabbit team,

I am reaching out because CodeRabbit's product sits at the intersection of developer tooling, code review quality, and AI systems that need to explain themselves inside existing workflows.

My strongest overlap is evaluation and review tooling. I built Seaweed, a Go/PostgreSQL/Judge0 coding-evaluation platform for 500+ concurrent users with sub-5s P95 verdict latency and per-test runtime/memory telemetry. I also built Murdoc, an AI gateway that records route profiles, policy decisions, OpenTelemetry traces, Prometheus metrics, and replayable decisions for LLM/tool traffic. On the open-source side, I have contributed to Invesalius, IOOS, VideoLAN, CRIU, and Tiled, so I am used to maintainer review constraints.

Would my profile be relevant for backend, evaluation, or developer-tooling engineering roles at CodeRabbit?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi CodeRabbit team,

Quick bump. I think the fit is around code-review systems where AI output needs evaluation, telemetry, policy/context awareness, and useful developer-facing feedback rather than generic comments.

Happy to send a short walkthrough of Seaweed or Murdoc if useful.

Best,
Shuvam
```

## 4. One2N

Best route: apply through the One2N careers page for matching SRE/backend roles

Email fallback from official site terms: `contact@one2n.in`

Suggested subject: `SRE/platform engineering profile`

Use resume: `tailored_resumes/full/one2n_resume.pdf`

Attachment note: attach the PDF above if emailing. For active roles, use the careers apply link first, then send the email as a short parallel note.

Why this angle:
One2N's current hiring and services are strongly SRE/platform/backend oriented: reliability engineering, production ownership, CI/CD, DevSecOps, backend engineering, and AI-enabled SRE/SDLC. The strongest fit is Postificus reliability patterns, Seaweed production-style evaluation systems, Murdoc observability, and Bentham deployment work.

Email:

```text
Hi One2N team,

I saw your current roles around SRE and your emphasis on pragmatic engineering, production reliability, and solving the real scaling/maintainability work after a proof of concept exists. That matches the kind of systems work I have been doing.

At my last internship at Bentham AI, I containerized backend services, deployed to Google Cloud Run, and automated GitHub Actions releases, improving deployment velocity by 70%. I built Postificus, a browser workflow platform, and worked on Go microservices with RabbitMQ retries, Redis state, PostgreSQL persistence, Dockerized services, health checks, and Prometheus metrics around unreliable long-running integrations. I built Seaweed, a coding-assessment platform, and worked on a Go/PostgreSQL/Judge0 evaluation platform for 500+ concurrent users with sub-5s P95 verdict latency.

Would my profile be relevant for SRE, platform, or backend engineering roles at One2N?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi One2N team,

Quick bump. I think the fit is around production-minded backend/platform work: retries, metrics, failure isolation, CI/CD, and making systems operable after the first version ships.

Happy to send a short walkthrough of Postificus or Seaweed if useful.

Best,
Shuvam
```

## 5. Shellkode

Send to: `hello@shellkode.com`

Suggested subject: `Cloud + GenAI backend profile`

Use resume: `tailored_resumes/full/shellkode_resume.pdf`

Attachment note: attach the PDF above. This is a general company inbox, so keep the note direct and ask for routing to the cloud/GenAI hiring owner.

Why this angle:
Shellkode is positioned around GenAI agents, data engineering, cloud migration/modernization, NextGen AIOps, DevOps, observability, and AWS modernization. The strongest fit is cloud/platform delivery from Bentham, Postificus, distributed inference, and Swish.

Email:

```text
Hi Shellkode team,

I saw Shellkode's current focus on GenAI agents, data engineering, cloud modernization, DevOps, AIOps, and observability. The mix of enterprise delivery and hands-on platform work is the part that fits my background best.

At my last internship at Bentham AI, I built backend automation with Node/Puppeteer and Go, then containerized services with Docker, deployed to Google Cloud Run, and automated GitHub Actions releases, improving deployment velocity by 70%. I built Postificus, a browser workflow platform, and worked on Go services with RabbitMQ retries, Redis state, PostgreSQL persistence, Dockerized deployment, health checks, and Prometheus metrics. I also built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing.

Would my profile be relevant for cloud, GenAI backend, platform, or DevOps engineering work at Shellkode?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Shellkode team,

Quick bump. I think the fit is around cloud/backend implementation for GenAI and DevOps workflows: containerized services, CI/CD, observability, retry-aware integrations, and operational reliability.

Happy to send a short walkthrough of Postificus or the inference-engine work if useful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance reused from prior batches:
- Concise body, specific company-aware opening, proof-heavy middle, and one low-friction ask.
- Avoid support inboxes when a careers/hiring email exists; if support is the only public route, ask for routing rather than pretending it is recruiting.

Company context checked:
- Digital Paani: official about page and ADB Water Resilience Hub listing.
- OpenRouter: official careers and support pages.
- CodeRabbit: official about/careers/contact pages and CodeRabbit Series A hiring post.
- One2N: official careers, AI engineering, contact, and terms pages.
- Shellkode: official home, about, and DevOps pages.
