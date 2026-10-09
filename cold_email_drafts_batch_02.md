# Cold Email Drafts - Batch 02

Research date: 2026-05-12

Companies covered:
1. Round Treasury
2. Atlas
3. Pulse
4. Deccan AI
5. Work On Grid

Cold-email rules used for this batch:
- Keep the first email short, plain text, and easy to skim.
- Open with a real company-specific reason, not generic praise.
- Lead with proof: shipped systems, metrics, project links, or open-source work.
- Make one low-friction ask.
- Use the strongest public route first. Use founder-route emails only when public and when the note is meaningfully technical.
- For routes that explicitly ask for a resume, attach the tailored PDF. Do not leave local file paths in the email body.

## 1. Round Treasury

Send to: `jobs@roundtreasury.com`

Suggested subject: `Backend workflows for Round`

Use resume: `tailored_resumes/full/round_treasury_resume.pdf`

Attachment note: attach the PDF above; Round's public site routes hiring through the Join Us/jobs path, so the resume is appropriate here.

Why this angle:
Round is automating treasury, accounts payable, payroll, approvals, account visibility, and ERP/payment workflows for finance teams. The strongest fit is finance workflow automation, recoverable operational APIs, auditability, and backend reliability from Bentham, Swish, and Postificus.

Email:

```text
Hi Round team,

I saw Round is building an AI-powered finance system across treasury, AP, payroll, approvals, and connected banking. The part that stood out to me is the workflow depth: money movement, approvals, ERP sync, audit trails, and alerts all have to be reliable, not just automated.

My recent work has been in similar operational backends. At my last internship at Bentham AI, I built Puppeteer/Node workflows for MCA company-registration filings that cut manual filing time by 85%, plus Go services and Cloud Run/GitHub Actions deployments that improved release velocity by 70%. I also built Swish, a policy-grounded support workflow system, and Postificus, a Go/RabbitMQ workflow platform with retries, durable job state, and audit-friendly execution.

Would my profile be relevant for backend or product engineering work at Round?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Round team,

Quick bump. I think the fit is specifically around finance workflows where retries, approvals, audit trails, and external integrations need to work reliably under real operational constraints.

Happy to send a short walkthrough of the Bentham or Postificus systems if useful.

Best,
Shuvam
```

## 2. Atlas

Send to: `hello@theatlas.ai`

Suggested subject: `Backend workflows for Atlas`

Use resume: `tailored_resumes/full/atlas_resume.pdf`

Attachment note: attach the PDF above if sending by email. If using the contact form instead, paste the email body and include GitHub.

Why this angle:
Atlas partners with accounting firms to implement AI systems that scale firm capacity without scaling headcount. The strongest fit is AI-assisted accounting/finance operations, operational APIs, workflow reliability, and systems that preserve human judgment rather than replacing it blindly.

Email:

```text
Hi Arpit and Jagmal,

Atlas stood out because you are not just selling generic AI to accounting firms; you are implementing systems around each firm's processes, judgment, and operating model.

That matches the kind of backend workflow work I have been doing. At my last internship at Bentham AI, I built Puppeteer/Node workflows for MCA company-registration filings that reduced manual filing time by 85%, and I paired that with Go services, Docker, Cloud Run, and GitHub Actions. I also built Swish, an AI-assisted support workflow system where tool calls propose actions but deterministic services enforce refund, trust, and escalation rules.

I think I could help on backend systems for accounting workflows, operational APIs, traceable AI actions, or implementation-heavy customer deployments.

Would it be worth a short chat, or should I send this to whoever handles engineering hiring?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Arpit and Jagmal,

Quick bump. The specific fit I see is around workflow automation for accounting operations where AI suggestions still need deterministic checks, auditability, and clean handoffs.

I can share a short technical walkthrough if that is more useful than a resume-first note.

Best,
Shuvam
```

## 3. Pulse

Recommended route: `hello@trypulse.ai`

Founder route if sending a very technical note: `sid@trypulse.ai`; `ritvik@trypulse.ai` is also public, but use it sparingly.

Suggested subject: `Document workflow + model infra work`

Use resume: `tailored_resumes/full/pulse_resume.pdf`

Attachment note: attach the PDF above for `hello@trypulse.ai`. For founder email, a GitHub/resume link is cleaner if you have one.

Why this angle:
Pulse is building document intelligence across OCR, layout, vision models, complex extraction, regulated deployments, private VPC/on-prem options, Docker/Kubernetes, logging, metrics, and high-accuracy document workflows. The strongest fit is GSoC model/output integration, distributed inference, document/workflow backends, and evaluation systems.

Email:

```text
Hi Sid and Ritvik,

Pulse stood out because the product is not just OCR; it is layout-aware document intelligence that has to work in regulated enterprise environments, with private deployments, logging, metrics, and reliable extraction across messy real-world files.

My strongest overlap is model/workflow infrastructure. During Google Summer of Code with Invesalius, I built MRI segmentation tooling for 95 anatomical regions and reduced processing runtime by 87% with async/parallel execution while keeping outputs inspectable in a real application. I also built a distributed inference engine with streaming APIs, worker heartbeats, retry-aware orchestration, and KV-cache-aware routing. On the workflow side, Swish uses operational APIs, traceable actions, and human handoff paths for high-risk decisions.

Would my profile be relevant for backend, infra, or document-processing engineering work at Pulse?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Sid and Ritvik,

Quick bump. I think the overlap is model-output reliability: turning complex inputs into structured, inspectable outputs while keeping latency, deployment, and failure modes under control.

Happy to send a compact walkthrough of the GSoC or inference-engine work.

Best,
Shuvam
```

## 4. Deccan AI

Send to: `hey@deccan.ai`

Suggested subject: `Backend/eval systems for Deccan AI`

Use resume: `tailored_resumes/full/deccan_ai_resume.pdf`

Attachment note: attach the PDF above. Deccan's careers page asks for a resume, portfolio, and brief note; their open roles include Backend Engineer and ML Researcher - Benchmarks & Evaluation.

Why this angle:
Deccan AI is focused on high-quality human-curated data, model evaluation, agentic workflows, RL environments, Text2SQL, coding, multimodal data, and accuracy at scale. The strongest fit is evaluation infrastructure from Seaweed, agent/eval workflow design from Penny Lane, model integration from GSoC, and backend automation from Postificus.

Email:

```text
Hi Deccan AI team,

I saw your open roles for Backend Engineer and ML Researcher - Benchmarks & Evaluation, and the broader focus on accurate AI through expert data, model evaluation, agentic workflows, and RL environments.

My work lines up best with backend and evaluation systems. I built Seaweed, a Go/PostgreSQL/Judge0 evaluation platform for 500+ concurrent users with sub-5s P95 verdict latency and per-test runtime/memory telemetry. I also built Penny Lane Capital, a multi-agent research workflow with analyst roles, risk review, checkpoints, JSONL traces, and 5 baselines for evaluation. During Google Summer of Code with Invesalius, I integrated model outputs into an existing medical-imaging application and reduced runtime by 87%.

Would my profile be relevant for backend, benchmarks/evaluation, or agent-workflow engineering roles?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Deccan AI team,

Quick bump. The specific fit I see is around building evaluation systems where outputs need telemetry, repeatability, baselines, and human-reviewable traces.

Happy to send a short walkthrough of Seaweed or Penny Lane if helpful.

Best,
Shuvam
```

## 5. Work On Grid

Send to: `hello@workongrid.com`

Suggested subject: `Operational data workflows for Grid`

Use resume: `tailored_resumes/full/work_on_grid_resume.pdf`

Attachment note: attach the PDF above; this is a general company route, so keep the note short and ask for routing to engineering/hiring.

Why this angle:
Work On Grid is building operational intelligence for utilities and industrial operations, with integrations across existing enterprise systems and a need for reliable structured data collection, workflow visibility, and process automation. The strongest fit is operational data workflows from Postificus, Swish, Seaweed, and Bentham.

Email:

```text
Hi Grid team,

I saw Grid is focused on operational intelligence for utilities and industrial workflows: structured data collection, process visibility, integrations, automation, and measurable time savings across operations.

That maps well to the backend systems I have been building. Postificus coordinates long-running external integrations with Go services, PostgreSQL, Redis, RabbitMQ retries/DLQs, durable job state, and Dockerized deployment. Swish uses operational APIs, PostgreSQL/Redis state, traceable actions, and human handoff paths for high-risk workflow decisions. At my last internship at Bentham AI, I built Puppeteer/Node workflow automation that cut manual filing time by 85% and improved release velocity by 70% through Docker, Cloud Run, and GitHub Actions.

Would my profile be relevant for backend, platform, or operational workflow engineering at Grid?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Grid team,

Quick bump. I think the fit is around operational workflows that need integrations, durable state, retries, visibility, and backend reliability rather than one-off automation.

Happy to send a short walkthrough of Postificus or Swish if useful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance reused from Batch 01:
- Concise body, specific company-aware opening, proof-heavy middle, and one low-friction ask.
- Keep first-touch emails plain text and avoid overexplaining the full resume.

Company context checked:
- Round Treasury: official site/about page and Join Us route.
- Atlas: official site and Stellaris portfolio/news page.
- Pulse: official site, careers page, privacy page, and recent document-intelligence posts.
- Deccan AI: official about/careers/open-roles pages and March 2026 funding/news context.
- Work On Grid: official about page and April 2026 funding/news context.
