# Cold Email Drafts - Batch 04

Research date: 2026-05-12

Companies covered:
1. miniOrange
2. i2k2 Networks
3. NeoDocs
4. TestMu AI
5. Kong

Cold-email rules used for this batch:
- Keep the first email short, plain text, and easy to skim.
- Open with a real company-specific reason, not generic praise.
- Lead with proof: shipped systems, metrics, project links, or open-source work.
- Make one low-friction ask.
- Use formal careers/apply paths first for larger companies.
- If only a general inbox exists, ask for routing instead of treating it like a recruiting inbox.
- Do not leave local file paths in the sent email body.

## 1. miniOrange

Recommended route: `careers@xecurify.com`

Founder route if sending only a very specific security/product note: `anirban@miniorange.com`

Suggested subject: `Backend/security engineering profile`

Use resume: `tailored_resumes/full/miniorange_resume.pdf`

Attachment note: attach the PDF above. The official careers page lists `careers@xecurify.com`, which is better than using support.

Why this angle:
miniOrange spans SSO, MFA, user lifecycle, RBAC, PAM, CASB/UEM, identity governance, and secure AI agents. The strongest fit is Murdoc's AI gateway, RBAC/runtime policy, PII redaction, allow/block rules, audit trails, and OpenTelemetry/Prometheus instrumentation, plus Swish's deterministic policy enforcement.

Email:

```text
Hi miniOrange team,

I saw miniOrange's product surface spans SSO/MFA, user lifecycle management, RBAC, PAM, CASB/UEM, and secure AI agents. The part that fits my background is access-aware backend work where policy, auditability, and product workflows have to stay tightly connected.

My strongest overlap is Murdoc, a self-hosted AI security gateway for LLM, HTTP-tool, and MCP traffic. It uses route profiles, RBAC runtime settings, PII redaction, allow/block rules, OpenTelemetry/Prometheus, health checks, and audit ledgers for policy decisions. On a 150-case attack corpus, it blocked 90%+ of prompt-injection and unsafe-tool attempts with under 5% false positives. I also built Swish, where LLM suggestions are constrained by deterministic refund, trust, and escalation rules.

Would my profile be relevant for software intern, backend, or security engineering roles at miniOrange?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi miniOrange team,

Quick bump. I think the fit is around identity-aware backend systems where access controls, policy decisions, audit logs, and AI-agent/tool behavior need to be enforced at runtime.

Happy to send a short walkthrough of Murdoc if useful.

Best,
Shuvam
```

## 2. i2k2 Networks

Send to: `hr@i2k2.com`

Suggested subject: `Cloud/platform backend profile`

Use resume: `tailored_resumes/full/i2k2_resume.pdf`

Attachment note: attach the PDF above. i2k2's careers page explicitly lists `hr@i2k2.com` for HR queries.

Why this angle:
i2k2 is a managed cloud and infrastructure services company: cloud hosting, managed support, availability, security, maintenance, and customer delivery. The strongest fit is Bentham deployment/CI, Postificus service reliability, Murdoc security observability, and Seaweed load-aware backend work.

Email:

```text
Hi i2k2 HR team,

I saw i2k2's work around managed cloud hosting, cloud-agnostic infrastructure, high availability, security, and 24x7 managed support. My background is closest to backend/platform work where services need to be deployable, observable, and reliable under operational load.

At my last internship at Bentham AI, I containerized backend services, deployed to Google Cloud Run, and automated GitHub Actions releases, improving deployment velocity by 70%. I built Postificus, a browser workflow platform, and worked on Go microservices with RabbitMQ retries, Redis state, PostgreSQL persistence, Dockerized services, health checks, and Prometheus metrics around unreliable long-running integrations. I also built Seaweed, a Go/PostgreSQL/Judge0 evaluation platform for 500+ concurrent users with sub-5s P95 verdict latency.

Would my profile be relevant for cloud, backend, DevOps, or platform engineering roles at i2k2?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi i2k2 HR team,

Quick bump. I think the fit is around managed cloud/backend work: containerized services, CI/CD, metrics, retries, failure isolation, and operating customer-facing systems reliably.

Happy to share a short walkthrough of Postificus or Seaweed if useful.

Best,
Shuvam
```

## 3. NeoDocs

Send to: `care@neodocs.in`

Suggested subject: `Health-data backend profile`

Use resume: `tailored_resumes/full/neodocs_resume.pdf`

Attachment note: attach the PDF above only if sending by email. This is a general care/contact inbox, so the email explicitly asks for routing to technical hiring.

Why this angle:
NeoDocs is focused on at-home testing, proactive health monitoring, test interpretation, WhatsApp/customer support, and accessible diagnostics. The strongest fit is health-data workflow reliability from GSoC medical imaging, Swish operational support workflows, and Bentham/Postificus recoverable backend automation.

Email:

```text
Hi NeoDocs team,

I know this is a general contact route, but I could not find a direct engineering hiring email. Could you forward this to the right person if relevant?

I saw NeoDocs is building at-home testing and health monitoring around accessible diagnostics, result interpretation, and ongoing user support. My background is backend workflow work around sensitive/structured outputs. During Google Summer of Code with Invesalius, I built MRI segmentation tooling for 95 anatomical regions, reduced processing runtime by 87%, and integrated model outputs into inspectable application workflows. I also built Swish, an AI-assisted support workflow system with operational APIs, PostgreSQL/Redis state, traceable actions, and human handoffs for high-risk decisions.

Would my profile be relevant for backend, health-data, or workflow engineering at NeoDocs?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi NeoDocs team,

Quick bump. I think the fit is around health-data workflows where model/output processing, traceability, support handoffs, and reliable backend state matter.

Happy to send a short walkthrough of the GSoC or Swish work if useful.

Best,
Shuvam
```

## 4. TestMu AI

Best route: TestMu AI careers page, open roles, or "Apply Here" / Talent Community

Suggested subject: `Agentic testing + browser automation profile`

Use resume: `tailored_resumes/full/testmu_ai_resume.pdf`

Attachment note: attach the PDF above in the application form. I did not find a stronger current official recruiting email than the careers/apply route.

Why this angle:
TestMu AI is positioning around agentic quality engineering: KaneAI, Browser Cloud, HyperExecute, real device cloud, MCP server, test orchestration, visual testing, test insights, Playwright/Puppeteer/Selenium/Cypress ecosystems, and AI-native testing. The strongest fit is Seaweed's evaluation platform, Postificus browser automation, Murdoc MCP/tool traffic, and Bentham Puppeteer automation.

Email/application note:

```text
Hi TestMu AI team,

I am interested in TestMu AI because the product direction combines agentic testing, browser infrastructure, test orchestration, MCP tooling, and developer workflows. That overlaps strongly with the systems I have been building.

At my last internship at Bentham AI, I built a Puppeteer/Node automation engine for MCA filings with reliable browser execution, retries, and API-backed state checks, reducing manual filing time by 85%. I built Postificus, a browser workflow platform, and worked on Go-Rod browser automation with RabbitMQ retries/DLQs, circuit breakers, Prometheus metrics, and health checks for long-running third-party browser jobs. I also built Seaweed, a Go/PostgreSQL/Judge0 evaluation platform for 500+ concurrent users with sub-5s P95 verdict latency, and Murdoc, an AI gateway for LLM/tool/MCP traffic with OpenTelemetry traces and replayable decisions.

Would my profile be relevant for backend, agentic testing, browser infrastructure, or evaluation-platform engineering roles?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi TestMu AI team,

Quick bump. The specific fit is around test infrastructure where browser automation, queue-backed execution, telemetry, evaluation loops, and AI/tool behavior need to be reliable and inspectable.

Happy to share a short walkthrough of Postificus, Seaweed, or Murdoc if useful.

Best,
Shuvam
```

## 5. Kong

Best route: apply through Kong's Ashby careers page

Email fallback: none verified on Kong's current careers/contact pages in this pass. Use the parallel note only if you later find a current recruiting contact.

Suggested subject: `AI/API gateway backend profile`

Use resume: `tailored_resumes/full/kong_resume.pdf`

Attachment note: attach the PDF above in the formal application. For a parallel note, mention that you already applied and ask for routing.

Why this angle:
Kong's current platform messaging heavily emphasizes unified API and AI connectivity: API Gateway, AI Gateway, MCP client/registry/traffic gateway, service catalog, API observability, APIOps, metering, and agentic infrastructure. The strongest fit is Murdoc's AI gateway/MCP policy and telemetry, Postificus's distributed services, and the distributed inference engine.

Email/application note:

```text
Hi Kong team,

I am interested in Kong because the platform is moving directly into the API + AI traffic layer: AI Gateway, MCP production and governance, API observability, service catalog, APIOps, and agentic infrastructure.

My strongest overlap is Murdoc, a FastAPI AI gateway for LLM, HTTP-tool, and MCP traffic with route profiles, runtime policy checks, request scoring, OpenTelemetry traces, Prometheus metrics, audit ledgers, and replayable decisions before downstream execution. I also built Postificus, a browser workflow platform with distributed Go services with RabbitMQ workers, DLQs, Redis/PostgreSQL state, Prometheus metrics, and health checks around long-running browser jobs. Separately, I built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing.

Would my profile be relevant for backend, gateway, AI infrastructure, or developer-platform engineering roles at Kong?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Parallel note after applying, if you find a current recruiting contact:

```text
Hi Kong People Ops team,

I applied through the careers page and wanted to send a short routing note in case there is a backend/API-platform team reviewing AI Gateway or MCP-related profiles.

My strongest overlap is Murdoc, a FastAPI AI gateway for LLM, HTTP-tool, and MCP traffic with route profiles, runtime policy checks, OpenTelemetry traces, Prometheus metrics, audit ledgers, and replayable decisions. I have also built distributed Go services with RabbitMQ, Redis/PostgreSQL, health checks, and Prometheus metrics, plus a distributed inference engine with streaming APIs and retry-aware orchestration.

Could this be routed to the right hiring team if relevant?

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Kong team,

Quick bump. The specific overlap is AI/API gateway work: MCP/tool traffic, policy enforcement, request telemetry, replayable decisions, and infrastructure that stays observable under real production traffic.

Happy to send a short walkthrough of Murdoc if useful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance reused from prior batches:
- Concise body, specific company-aware opening, proof-heavy middle, and one low-friction ask.
- For larger companies, use the formal apply route first and treat any email as a routing note.

Company context checked:
- miniOrange: official about and careers pages.
- i2k2 Networks: official careers page and managed cloud hosting page.
- NeoDocs: official about and contact pages.
- TestMu AI: official about and careers pages.
- Kong: official careers page and current API/AI platform navigation.
