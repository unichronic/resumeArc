# Cold Email Drafts - Batch 01

Research date: 2026-05-11

Companies covered:
1. Auctor
2. Browser Use
3. SigNoz
4. Repello AI
5. StackGen

Cold-email rules used for this batch:
- Keep the first email short, plain text, and easy to skim.
- Open with a real company-specific reason, not generic praise.
- Lead with proof: shipped systems, metrics, project links, or open-source work.
- Make one low-friction ask.
- Use the company's preferred public route first. Use founder emails only when public and clearly relevant.
- For routes that explicitly ask for a resume, attach the tailored PDF. For founder-style notes, a link is often safer than a heavy attachment.

## 1. Auctor

Send to: `will@getauctor.com`

Suggested subject: `Backend workflows for Auctor`

Use resume: `tailored_resumes/full/auctor_resume.pdf`

Attachment note: attach the PDF above; do not leave a local path in the sent email.

Why this angle:
Auctor is explicitly about software implementation workflows: capturing project context, generating implementation artifacts, keeping decisions and scope in sync, and reducing messy handoff/rework. The strongest fit is Bentham automation + Swish workflow systems + Postificus recoverable external integrations.

Email:

```text
Hi William,

I saw Auctor is building the system of action for software implementations: capturing what was said, decided, and delivered, then turning that into SOWs, user stories, architecture docs, and delivery artifacts.

That maps closely to work I have been doing. At my last internship at Bentham AI, I built Puppeteer/Node automations for MCA company-registration filings that cut manual filing time by 85%, plus Go services and Cloud Run/GitHub Actions deployments that improved release velocity by 70%. I have also built Swish, a policy-grounded support workflow system, and Postificus, a Go/Rod + RabbitMQ workflow platform for brittle external integrations.

I think I could be useful on backend or forward-deployed engineering work where product needs to survive messy customer workflows.

Would it be worth a quick 15-minute chat, or should I send this to whoever owns engineering hiring?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi William,

Quick bump on this. I think the overlap is specifically around implementation workflows that need auditability, retries, customer-specific state, and clean handoffs.

If useful, I can send a short walkthrough of the Bentham/Postificus pieces instead of asking for a call upfront.

Best,
Shuvam
```

## 2. Browser Use

Send to: `apply@browser-use.com`

Suggested subject: `GitHub + browser automation work`

Use resume: `tailored_resumes/full/browser_use_resume.pdf`

Attachment note: attach the PDF above; Browser Use explicitly asks for GitHub, so keep the GitHub link visible in the body.

Why this angle:
Browser Use explicitly asks for GitHub and calls out hard problems around reliable browser agents, browser infrastructure, LLM tool-calling, deterministic reruns, and text representations of websites. The strongest fit is Bentham Puppeteer automation + Postificus Go-Rod/RabbitMQ reliability + Murdoc tool/MCP tracing.

Email:

```text
Hi Magnus and Gregor,

Your careers page says to send GitHub, and the YC role calls out browser-agent reliability, infrastructure, tool calling, and deterministic reruns. That is the exact part of browser automation I have been working around.

At my last internship at Bentham AI, I built a Puppeteer engine for MCA company-registration filings with session handling, network-idle checks, CAPTCHA handoff, retries, and state recovery; it cut manual filing time by 85%. I built Postificus, a browser workflow platform, and worked on Go-Rod automation with RabbitMQ retries/DLQs, circuit breakers, Prometheus metrics, and health checks for long-running third-party browser jobs.

I would be strongest on browser-agent reliability and infrastructure. GitHub: https://github.com/unichronic

Could you point me to the right next step if this is relevant?

I have attached my resume below.

Best,
Shuvam Pal
```

Follow-up if no reply after 5-7 days:

```text
Hi Magnus and Gregor,

Quick bump. The shortest version: I have shipped brittle browser automation with retries, session recovery, observability, and queue-backed execution, and I would like to work on that problem space at Browser Use.

GitHub again: https://github.com/unichronic

Best,
Shuvam
```

## 3. SigNoz

Recommended founder route: `pranay@signoz.io` or `ankit@signoz.io`

Safer hiring route: `hiring@signoz.io`

Suggested subject: `OTel-heavy backend work for SigNoz`

Use resume: `tailored_resumes/full/signoz_resume.pdf`

Attachment note: attach the PDF above if using `hiring@signoz.io`; for founder email, attachment is acceptable but a resume link is cleaner if you have one.

Why this angle:
SigNoz is OpenTelemetry-native and developer/open-source heavy. The strongest fit is Murdoc's OpenTelemetry/Prometheus/audit trail work, Postificus distributed job observability, and open-source contribution history.

Email:

```text
Hi Pranay,

I like that SigNoz is OpenTelemetry-native instead of asking teams to bake in vendor agents. My recent work lines up with that direction.

I built Murdoc, which is a FastAPI AI gateway where LLM, HTTP-tool, and MCP traffic has OpenTelemetry traces, Prometheus metrics, route profiles, audit logs, and replayable policy decisions. Postificus uses Prometheus health/metrics around RabbitMQ workers, DLQs, retries, circuit breakers, and browser jobs so failures are debuggable instead of silent.

I am looking for backend/platform work where telemetry, debugging context, and open-source discipline matter. I have contributed to Invesalius, IOOS, VideoLAN, CRIU, and Tiled, and I am comfortable working through maintainer review.

Would this be relevant for any backend, platform, or open-source engineering role at SigNoz?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Alternate if using `hiring@signoz.io` instead of founder email:

```text
Hi SigNoz team,

I am reaching out because SigNoz's OpenTelemetry-native direction matches the backend/observability work I have been building.

I built Murdoc, which is a FastAPI AI gateway where LLM, HTTP-tool, and MCP traffic has OpenTelemetry traces, Prometheus metrics, route profiles, audit logs, and replayable policy decisions. Postificus uses Prometheus health/metrics around RabbitMQ workers, DLQs, retries, circuit breakers, and browser jobs so failures are debuggable instead of silent.

I have also contributed to Invesalius, IOOS, VideoLAN, CRIU, and Tiled, so I am comfortable working in open-source codebases with maintainer review.

Could you let me know if my profile is relevant for backend, platform, or open-source engineering roles?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Pranay,

Quick bump. I think the specific overlap is OpenTelemetry instrumentation, replayable debugging context, and backend systems where traces/metrics need to explain product behavior rather than just report uptime.

Happy to send a short technical walkthrough of Murdoc if useful.

Best,
Shuvam
```

## 4. Repello AI

Send to: `contact@repello.ai`

Suggested subject: `MCP security + runtime policy work`

Use resume: `tailored_resumes/full/repello_ai_resume.pdf`

Attachment note: attach the PDF above; if the contact form strips attachments, include GitHub and offer to send the resume.

Why this angle:
Repello is focused on AI security, red teaming, prompt injection, MCP risks, runtime monitoring, and enterprise AI deployments. Murdoc is the strongest company-specific hook here and should lead the email.

Email:

```text
Hi Aryaman and Naman,

Repello's recent MCP security writing stood out because it treats tool responses and agent autonomy as runtime attack surfaces, not just prompt-filtering problems. I have been building in that exact direction.

I built Murdoc, which is a self-hosted AI security gateway for LLM, HTTP-tool, and MCP traffic. It uses route profiles, RBAC runtime settings, PII redaction, allow/block rules, OpenTelemetry/Prometheus, health checks, and audit ledgers for policy decisions. On a 150-case attack corpus, it blocked 90%+ of prompt-injection and unsafe-tool attempts with under 5% false positives.

I would be useful on agentic-AI security engineering, eval harnesses, runtime policy, or backend systems around red-teaming workflows.

Is there someone I should send a fuller note or resume to?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi Aryaman and Naman,

Quick bump. The short version is that I have already built a small MCP/tool-traffic security gateway with evals, policy logs, and OpenTelemetry/Prometheus instrumentation.

If relevant, I can send a compact technical walkthrough instead of a general resume note.

Best,
Shuvam
```

## 5. StackGen

Send to: `jobs@stackgen.com`

Suggested subject: `Platform automation + observability resume`

Use resume: `tailored_resumes/full/stackgen_resume.pdf`

Attachment note: attach the PDF above; StackGen's careers page asks for resume + note at the jobs address.

Why this angle:
StackGen's current positioning is agentic/autonomous DevOps across infrastructure, SRE, observability, policy, approvals, audit trails, and cloud tooling. The strongest fit is Bentham CI/CD + Postificus platform reliability + Murdoc policy/audit/observability.

Email:

```text
Hi StackGen team,

I am reaching out because StackGen's agentic Ops direction across infrastructure, SRE, observability, approvals, and audit trails maps well to the platform work I have been doing.

At my last internship at Bentham AI, I containerized backend services, deployed to Google Cloud Run, and automated GitHub Actions releases, improving deployment velocity by 70%. I built Postificus, a browser workflow platform, and worked on Go microservices with RabbitMQ retries/DLQs, Redis state, PostgreSQL persistence, health checks, and Prometheus metrics around unreliable long-running jobs. I built Murdoc, an AI/tool gateway, and added policy decisions, RBAC, OpenTelemetry traces, Prometheus metrics, and audit ledgers to AI/tool traffic.

I am strongest where backend engineering, DevOps automation, and observability meet.

Would my profile be relevant for platform engineering, cloud security/compliance, or agentic DevOps engineering roles?

I have attached my resume below.

Best,
Shuvam Pal
GitHub: https://github.com/unichronic
```

Follow-up if no reply after 5-7 days:

```text
Hi StackGen team,

Quick bump. I think the fit is around backend/platform work that turns infrastructure automation into something observable, recoverable, and auditable.

Happy to share a short technical walkthrough of the Postificus or Murdoc systems if helpful.

Best,
Shuvam
```

## Source Notes

Cold-email guidance checked:
- Stripe Atlas startup sales guide: concise, action-oriented cold emails with a specific ask.
- Grammarly cold email guide: clear subject, personalized opening, value-driven body, one CTA, professional close.
- Outreachly cold outreach guide: short subject, 4-5 sentence body, plain text, one low-ask CTA.

Company context checked:
- Auctor: official site/careers and YC company page.
- Browser Use: careers page and YC role page.
- SigNoz: official site, about page, careers redirect, docs/GitHub.
- Repello AI: official site, about page, and current MCP/prompt-injection security posts.
- StackGen: official site, about/careers pages, Infrastructure from Code material.
