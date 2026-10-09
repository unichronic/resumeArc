/**
 * Gmail draft creator for internship outreach.
 *
 * Originally assembled from cold_email_drafts_batch_01.md through cold_email_drafts_batch_11.md.
 * Primary company emails/application notes are included; follow-up drafts are intentionally omitted.
 * The draft bodies below are the current polished versions used by createDrafts().
 *
 * How to use:
 * 1. Open https://script.google.com and create a new Apps Script project.
 * 2. Upload the PDFs from tailored_resumes/full/ to Google Drive.
 * 3. Optional but recommended: put the Drive folder ID in CONFIG.resumeDriveFolderId.
 * 4. Paste this whole file into Code.gs.
 * 5. Run previewDrafts() and previewResumeAttachments() to inspect logs.
 * 6. Run createDrafts().
 * 7. Approve Gmail and Drive access once.
 *
 * Notes:
 * - This creates drafts only. It does not send emails.
 * - If `to` is blank, the draft is created to your own Gmail address and the
 *   subject is prefixed with [ADD TO]. Replace the recipient manually in Gmail.
 * - Apps Script cannot read local paths from this computer. resumePath is used
 *   only to derive a PDF filename, which is then looked up in Google Drive.
 * - If CONFIG.requireResumeAttachment is true, a draft is skipped when its
 *   matching PDF cannot be found in Drive.
 */

const CONFIG = {
  labelName: 'intern-outreach-drafts',
  dryRun: false,
  dedupe: true,
  attachResumes: true,
  requireResumeAttachment: true,
  // Paste the ID from a Drive folder URL. Leave blank to search all visible Drive files by filename.
  resumeDriveFolderId: '',
  createMissingRecipientDraftsToSelf: true,
  missingRecipientSubjectPrefix: '[ADD TO] ',
};

const DRAFTS = [
  {
    "company": "Auctor",
    "to": "will@getauctor.com",
    "subject": "Question about Auctor workflows",
    "resumePath": "tailored_resumes/full/auctor_resume.pdf",
    "body": "Hi William,\n\nAuctor's work on turning customer context into SOWs, user stories, architecture docs, and delivery artifacts caught my attention. I would like to be considered for backend internship work around those implementation workflows.\n\nAt my last internship at Bentham AI, I worked on Puppeteer-based browser automation for MCA filings, making repetitive filing flows more reliable and reducing manual filing time by 85%. I also built Postificus, a browser-automation content distribution platform, where queues, saved state, retries, and health checks keep long-running browser workflows recoverable instead of brittle.\n\nIf this sounds useful, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_01.md"
  },
  {
    "company": "Browser Use",
    "to": "apply@browser-use.com",
    "subject": "Browser automation internship",
    "resumePath": "tailored_resumes/full/browser_use_resume.pdf",
    "body": "Hi Browser Use team,\n\nBrowser Use stood out to me because the hard parts are the same browser automation problems I have been building around: agents, tool execution, retries, and deterministic reruns. I would like to be considered for browser automation internship work there.\n\nAt my last internship at Bentham AI, I worked on Puppeteer browser automation for MCA filings, including session handling, network-idle checks, CAPTCHA handoff, retries, and recovery when a flow broke midway. I later built Postificus, a browser-automation content distribution platform, using Go-Rod, RabbitMQ retries, DLQs, metrics, and health checks.\n\nIf this is relevant, could you point me to the right person or next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_01.md"
  },
  {
    "company": "SigNoz",
    "to": "hiring@signoz.io",
    "subject": "OpenTelemetry backend internship",
    "resumePath": "tailored_resumes/full/signoz_resume.pdf",
    "body": "Hi SigNoz team,\n\nSigNoz's OpenTelemetry-native direction caught my attention. I would be glad to intern on backend observability work that needs tracing, metrics, and reliable failure visibility.\n\nI built Murdoc, an AI/tool gateway for LLM, HTTP-tool, and MCP traffic, and Postificus, a browser-automation workflow platform. The Murdoc work made AI/tool traffic easier to inspect with OpenTelemetry traces, Prometheus metrics, route profiles, audit logs, and replayable decisions; the Postificus work applied similar observability ideas around queue workers, retries, DLQs, circuit breakers, and browser jobs.\n\nWould it make sense for me to be considered for a backend observability internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_01.md"
  },
  {
    "company": "Repello AI",
    "to": "contact@repello.ai",
    "subject": "MCP security work",
    "resumePath": "tailored_resumes/full/repello_ai_resume.pdf",
    "body": "Hi Repello AI team,\n\nRepello's work around MCP security, red teaming, and runtime monitoring is very close to the systems I have been building and testing myself. I would like to be considered for AI security internship work if there is room for an intern.\n\nI built Murdoc, a self-hosted gateway for LLM, HTTP-tool, and MCP traffic. I used it to experiment with route-level policy, RBAC-style runtime settings, PII redaction, allow/block rules, health checks, audit logs, and attack-case validation for prompt injection and unsafe tool use.\n\nIf there is an internship path around AI security work, I would be glad to be considered.\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_01.md"
  },
  {
    "company": "StackGen",
    "to": "jobs@stackgen.com",
    "subject": "Ops automation internship",
    "resumePath": "tailored_resumes/full/stackgen_resume.pdf",
    "body": "Hi StackGen team,\n\nStackGen's agentic Ops direction across infrastructure, observability, approvals, and audit trails maps well to the backend and workflow systems I have been building. I would like to be considered for a platform internship in that area.\n\nAt my last internship at Bentham AI, I worked across automation and deployment: Puppeteer workflows for MCA filings, backend services, Docker, Cloud Run, and GitHub Actions. Outside the internship, I built Postificus, a queue-backed browser workflow platform, and Murdoc, an AI/tool gateway where policy decisions and traces make AI traffic easier to inspect.\n\nCould you let me know whether this would be worth considering for a platform internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_01.md"
  },
  {
    "company": "Round Treasury",
    "to": "jobs@roundtreasury.com",
    "subject": "Backend internship - finance workflows",
    "resumePath": "tailored_resumes/full/round_treasury_resume.pdf",
    "body": "Hi Round team,\n\nRound's finance workflow angle caught my attention because it seems to need reliable approvals, integrations, audit trails, and alerts rather than generic automation. I would like to be considered for backend internship work around those systems.\n\nAt my last internship at Bentham AI, I worked on Puppeteer/Node workflows for MCA filings, turning a manual operational process into a more reliable automated flow and reducing manual filing time by 85%. I have also built Swish, an AI-assisted support workflow system, and Postificus, a queue-backed browser workflow platform, where correctness, retries, state, and auditability matter more than just calling an API.\n\nIf this background is useful for your backend work, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_02.md"
  },
  {
    "company": "Atlas",
    "to": "hello@theatlas.ai",
    "subject": "Workflow automation at Atlas",
    "resumePath": "tailored_resumes/full/atlas_resume.pdf",
    "body": "Hi Atlas team,\n\nAtlas's work around accounting-firm workflows, process judgment, and implementation-heavy automation caught my attention. I would like to be considered for backend internship work around workflow automation.\n\nAt my last internship at Bentham AI, I worked on Puppeteer/Node workflows for MCA company-registration filings, reducing manual filing time by 85%. That work made me comfortable with messy operational flows where browser automation, backend state, retries, and human handoff all have to fit together cleanly.\n\nWould it be useful to consider me for an internship around backend workflow automation?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_02.md"
  },
  {
    "company": "Pulse",
    "to": "hello@trypulse.ai",
    "subject": "Document AI infrastructure",
    "resumePath": "tailored_resumes/full/pulse_resume.pdf",
    "body": "Hi Pulse team,\n\nPulse's layout-aware document intelligence stood out to me because the product needs reliable extraction, logging, metrics, and private deployment paths, not just model calls. I would be glad to intern on backend ML infrastructure work in that space.\n\nIn Google Summer of Code with Invesalius, an open-source medical imaging application, I worked on MRI segmentation tooling where model outputs had to be fast, inspectable, and usable inside an application workflow. I also built a distributed inference engine, an ML-serving project that gave me practice with streaming APIs, worker health, retry-aware orchestration, and routing around constrained compute.\n\nIf this lines up with the kind of internship help you would consider, I would appreciate being pointed in the right direction.\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_02.md"
  },
  {
    "company": "Deccan AI",
    "to": "hey@deccan.ai",
    "subject": "Deccan evaluation systems",
    "resumePath": "tailored_resumes/full/deccan_ai_resume.pdf",
    "body": "Hi Deccan AI team,\n\nDeccan AI's work around expert data, benchmarks, agent workflows, and evaluation systems is close to the way I have been approaching my own projects. I would like to be considered for backend evaluation internship work.\n\nMy closest work is around evaluation systems. I built Seaweed, a technical assessment platform, where I handled judging, concurrency, result telemetry, and ranked shortlisting for 500+ users. I also built Penny Lane Capital, a multi-agent research workflow, with checkpoints, role separation, traces, and baseline comparisons.\n\nCould you let me know whether this would be relevant for an internship on backend evaluation systems?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_02.md"
  },
  {
    "company": "Work On Grid",
    "to": "hello@workongrid.com",
    "subject": "Operational workflow systems",
    "resumePath": "tailored_resumes/full/work_on_grid_resume.pdf",
    "body": "Hi Grid team,\n\nGrid's operational intelligence work caught my eye because it depends on dependable data collection, integrations, automation, and process visibility. I would like to be considered for backend platform internship work around that problem.\n\nA lot of my work has been around making operational workflows less fragile. At my last internship at Bentham AI, I automated MCA filing preparation and browser flows. I also built Postificus, a queue-backed browser workflow platform, and Swish, an AI-assisted support workflow system, where durable state, retries, traceable actions, and human handoff matter.\n\nIf this is useful for your backend platform work, could you point me to the right person for internships?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_02.md"
  },
  {
    "company": "Digital Paani",
    "to": "contact@digitalpaani.com",
    "subject": "Water operations workflows",
    "resumePath": "tailored_resumes/full/digital_paani_resume.pdf",
    "body": "Hi Digital Paani team,\n\nDigital Paani's wastewater operations product stood out to me because it needs dependable field workflows, external integrations, alerts, and operational state. I would like to be considered for backend platform internship work.\n\nAt my last internship at Bentham AI, I worked on Puppeteer/Node workflow automation for MCA filings, reducing manual filing time by 85% while dealing with state checks and unreliable browser steps. I also built Postificus, a browser-automation content distribution platform, with queueing, retries, Redis/PostgreSQL state, and Dockerized services.\n\nWould it make sense to consider me for a backend platform internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_03.md"
  },
  {
    "company": "OpenRouter",
    "to": "support@openrouter.ai",
    "subject": "Model routing infrastructure",
    "resumePath": "tailored_resumes/full/openrouter_resume.pdf",
    "body": "Hi OpenRouter team,\n\nOpenRouter's core problems around unified model access, provider routing, fallbacks, usage tracking, and reliable developer-facing APIs are exactly the kind of backend work I want to get deeper into. I would like to be considered for backend AI infrastructure internship work.\n\nMy closest work is around model and tool traffic. I built a distributed inference engine, an ML-serving project, to coordinate generation across heterogeneous workers with streaming APIs, worker health, retries, and KV-cache-aware routing. I also built Murdoc, an AI/tool gateway, to make LLM/tool requests more observable and policy-aware through traces, route profiles, metrics, and replayable decisions.\n\nIf this background is useful, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_03.md"
  },
  {
    "company": "CodeRabbit",
    "to": "careers@coderabbit.ai",
    "subject": "Developer tooling internship",
    "resumePath": "tailored_resumes/full/coderabbit_resume.pdf",
    "body": "Hi CodeRabbit team,\n\nCodeRabbit sits in a space I care about: code review quality, AI explanations, and engineering workflow integration. I would like to be considered for developer tooling internship work there.\n\nMy relevant work is around developer-facing evaluation and traceability. I built Seaweed, a coding-assessment platform, where automated judging, result telemetry, and ranked shortlisting have to stay reviewable. I also built Murdoc, an AI/tool gateway, where traces, metrics, route profiles, and replayable policy outcomes make AI behavior easier to inspect.\n\nWould you be open to considering me for an internship around developer tooling or backend systems?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_03.md"
  },
  {
    "company": "One2N",
    "to": "contact@one2n.in",
    "subject": "Backend reliability work",
    "resumePath": "tailored_resumes/full/one2n_resume.pdf",
    "body": "Hi One2N team,\n\nOne2N's work around reliability, maintainability, and production engineering matches the kind of systems I have been trying to build well. I would like to be considered for backend platform internship work.\n\nAt my last internship at Bentham AI, I worked on backend automation and deployment with Docker, Cloud Run, and GitHub Actions, improving deployment velocity by 70%. I also built Postificus, a queue-backed browser workflow platform, and Seaweed, a coding-assessment platform, where persistent state, retries, metrics, and concurrent workflows matter.\n\nCould you let me know whether my background fits any backend internship needs at One2N?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_03.md"
  },
  {
    "company": "Shellkode",
    "to": "hello@shellkode.com",
    "subject": "Shellkode cloud backend work",
    "resumePath": "tailored_resumes/full/shellkode_resume.pdf",
    "body": "Hi Shellkode team,\n\nShellkode's work across GenAI, cloud modernization, DevOps, AIOps, and observability connects well with my project background. I would like to be considered for cloud backend internship work.\n\nAt my last internship at Bentham AI, I worked across backend automation, browser workflows, containerization, Cloud Run deployments, and GitHub Actions. I also built Postificus, a Go-based browser workflow platform, where unreliable long-running jobs are handled with queues, retries, persistent state, health checks, and metrics.\n\nIf this is relevant for your cloud backend work, could you point me to the right internship contact?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_03.md"
  },
  {
    "company": "miniOrange",
    "to": "careers@xecurify.com",
    "subject": "Security backend internship",
    "resumePath": "tailored_resumes/full/miniorange_resume.pdf",
    "body": "Hi miniOrange team,\n\nminiOrange's product surface around SSO/MFA, lifecycle management, RBAC, PAM, and secure AI agents lines up with my backend security work. I would like to be considered for software engineering internship work.\n\nI built Murdoc, a self-hosted gateway for LLM, HTTP-tool, and MCP traffic. The goal was to make AI/tool usage safer and easier to audit with route-level policy, RBAC-style settings, PII redaction, allow/block rules, traces, metrics, health checks, and attack-case validation.\n\nWould it make sense for me to be considered for a software engineering internship at miniOrange?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_04.md"
  },
  {
    "company": "i2k2 Networks",
    "to": "hr@i2k2.com",
    "subject": "Managed cloud internship",
    "resumePath": "tailored_resumes/full/i2k2_resume.pdf",
    "body": "Hi i2k2 HR team,\n\ni2k2's managed cloud work stood out to me because it needs services that are deployable, observable, and reliable under operational load. I would like to be considered for cloud backend internship work.\n\nAt my last internship at Bentham AI, I worked on containerizing backend services, deploying them to Cloud Run, and automating releases with GitHub Actions, improving deployment velocity by 70%. I also built Postificus, a browser workflow platform, and Seaweed, a coding-assessment platform, with the same emphasis on reliable services, persistent state, health checks, and predictable behavior under load.\n\nCould you let me know whether this background is useful for a cloud backend internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_04.md"
  },
  {
    "company": "NeoDocs",
    "to": "care@neodocs.in",
    "subject": "Health-data backend work",
    "resumePath": "tailored_resumes/full/neodocs_resume.pdf",
    "body": "Hi NeoDocs team,\n\nNeoDocs caught my attention because the product sits around health monitoring, result interpretation, and structured user-support workflows. I would like to be considered for backend internship work if that background is useful.\n\nIn Google Summer of Code with Invesalius, an open-source medical imaging application, I worked on MRI segmentation tooling where model output had to be integrated into an inspectable application workflow. I also built Swish, an AI-assisted support workflow system, where backend state, traceable actions, and human handoff were important for higher-risk decisions.\n\nIf this overlaps with backend internship work at NeoDocs, I would appreciate being pointed to the right next step.\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_04.md"
  },
  {
    "company": "TestMu AI",
    "to": "hr@testmuai.com",
    "subject": "Testing infrastructure internship",
    "resumePath": "tailored_resumes/full/testmu_ai_resume.pdf",
    "body": "Hi TestMu AI team,\n\nTestMu's mix of agentic testing, browser infrastructure, test orchestration, MCP tooling, and developer workflows is close to work I have already done. I would like to be considered for backend testing infrastructure internship work.\n\nAt my last internship at Bentham AI, I worked on Puppeteer browser automation for MCA filings, including retries, API-backed state checks, and recovery paths for unreliable browser execution. I later built Postificus, a browser-automation content distribution platform, applying the same reliability ideas with Go-Rod, queue retries, DLQs, circuit breakers, metrics, and health checks.\n\nWould you be open to considering me for an internship around backend testing infrastructure?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_04.md"
  },
  {
    "company": "Kong",
    "to": "peopleoperations@konghq.com",
    "subject": "API gateway internship",
    "resumePath": "tailored_resumes/full/kong_resume.pdf",
    "body": "Hi Kong team,\n\nKong's work around API gateways, AI Gateway, MCP governance, observability, and developer infrastructure connects strongly with my project work. I would like to be considered for backend API infrastructure internship work.\n\nThe closest overlap is that I built Murdoc, a FastAPI gateway for LLM, HTTP-tool, and MCP traffic. I used it to explore route profiles, runtime policy checks, traces, metrics, audit logs, and replayable decisions before downstream execution. I also built Postificus, a browser workflow platform, where distributed Go workers handle long-running browser jobs with retries and persistent state.\n\nIf this background is useful, could you point me to the right next step for an internship at Kong?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_04.md"
  },
  {
    "company": "NeoSOFT Cloud",
    "to": "careers@neosofttech.com",
    "subject": "Cloud backend internship",
    "resumePath": "tailored_resumes/full/neosoft_cloud_resume.pdf",
    "body": "Hi NeoSOFT team,\n\nNeoSOFT's work across application development, cloud consulting, DevOps, AI, data engineering, and client-facing platform delivery maps well to my systems background. I would like to be considered for cloud backend internship work.\n\nAt my last internship at Bentham AI, I worked on backend automation and deployment with Docker, Cloud Run, and GitHub Actions, improving deployment velocity by 70%. I also built Postificus, a browser workflow platform, and Seaweed, a coding-assessment platform, with queues, persistent state, health checks, metrics, and concurrent user workflows.\n\nCould you let me know whether this would be a fit for a cloud backend internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_05.md"
  },
  {
    "company": "TsecondAI",
    "to": "careers@tsecond.ai",
    "subject": "Backend AI internship",
    "resumePath": "tailored_resumes/full/tsecondai_resume.pdf",
    "body": "Hi Tsecond team,\n\nTsecond's edge AI work stood out to me because it involves low-latency runtime coordination, worker health, local inference, data movement, and reliable operation when cloud assumptions break down. I would like to be considered for backend AI internship work.\n\nMy closest work is a distributed inference engine, an ML-serving project I built to coordinate generation across heterogeneous consumer hardware. It gave me hands-on experience with streaming APIs, worker health, request routing, retry-aware orchestration, and runtime metrics for latency, throughput, token acceptance, and memory use.\n\nIf this sounds relevant, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_05.md"
  },
  {
    "company": "RemoteStar",
    "to": "hello@remotestar.io",
    "subject": "Cloud backend matching",
    "resumePath": "tailored_resumes/full/remotestar_resume.pdf",
    "body": "Hi RemoteStar team,\n\nMy background seems better suited to cloud backend internship work than a generic resume screen might show, so RemoteStar's skills-first matching angle felt especially relevant.\n\nMy background is mostly in backend systems that need to be reliable under messy real-world conditions. At my last internship at Bentham AI, I worked on workflow automation and deployment. I also built Postificus, a queue-backed browser workflow platform, and Seaweed, a coding-assessment platform for 500+ concurrent users.\n\nIf you are matching candidates to technical internships, could you point me to the right next step?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_05.md"
  },
  {
    "company": "Coralogix",
    "to": "contact@coralogix.com",
    "subject": "Coralogix OpenTelemetry work",
    "resumePath": "tailored_resumes/full/coralogix_resume.pdf",
    "body": "Hi Coralogix team,\n\nCoralogix's work around OpenTelemetry, DevOps and SRE workflows, and AI observability is close to the telemetry-heavy backend projects I have been building. I would like to be considered for backend observability internship work.\n\nA similar theme shows up in two projects I built. I built Murdoc, an AI/tool gateway, and instrumented AI traffic with OpenTelemetry traces, Prometheus health checks, route profiles, and audit logs. I also built Postificus, a browser workflow platform, and used metrics, retries, DLQs, circuit breakers, and health checks around queue workers and long-running jobs.\n\nWould you be open to considering me for a backend observability internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_05.md"
  },
  {
    "company": "Swif.ai",
    "to": "support@swif.ai",
    "subject": "Security workflow backend",
    "resumePath": "tailored_resumes/full/swif_ai_resume.pdf",
    "body": "Hi Swif team,\n\nSwif's work around endpoint posture, Shadow IT visibility, policy enforcement, compliance evidence, identity integrations, and onboarding/offboarding automation connects well with my backend projects. I would like to be considered for backend security workflow internship work.\n\nMy relevant work is around backend systems where policy and reliability matter. I built Postificus, a queue-backed browser workflow platform, with retries, DLQs, state, health checks, and metrics. I also built Murdoc, an AI/tool gateway, where policy checks, RBAC-style settings, audit logs, and traces make LLM/tool traffic easier to govern.\n\nIf this is useful, could you point me to the right internship contact?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_05.md"
  },
  {
    "company": "CAST AI",
    "to": "hello@cast.ai",
    "subject": "Cloud optimization backend",
    "resumePath": "tailored_resumes/full/cast_ai_resume.pdf",
    "body": "Hi CAST AI team,\n\nCAST AI's work on cloud automation, workload optimization, GPU/AI infrastructure, and balancing cost, performance, and reliability is close to the infrastructure problems I have been working on. I would like to be considered for cloud platform internship work.\n\nMy closest work is cost-aware and runtime-aware backend infrastructure. I built Seaweed, a coding-assessment platform, where I moved a ranking path away from a Redis + DynamoDB style design toward PostgreSQL materialized views, reducing infrastructure cost by about 70% while keeping low-latency reads. I have also built a distributed inference engine with worker health, routing, and streaming APIs.\n\nCould you let me know whether this background would be worth considering for a cloud platform internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_06.md"
  },
  {
    "company": "Chainguard",
    "to": "support@chainguard.dev",
    "subject": "Secure OSS backend work",
    "resumePath": "tailored_resumes/full/chainguard_resume.pdf",
    "body": "Hi Chainguard team,\n\nChainguard's mission around verifiably secure open-source software and safer production delivery stood out to me because it matches the security side of my backend work. I would like to be considered for backend security platform internship work.\n\nI built Murdoc, a self-hosted AI security gateway where I experimented with prompt-injection and unsafe-tool defenses, policy checks, RBAC-style settings, PII redaction, traces, metrics, and audit logs. I have also contributed across open-source codebases in medical imaging, ocean data, media tooling, Linux checkpoint/restore, and map editing.\n\nWould it make sense to consider me for a backend security platform internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_06.md"
  },
  {
    "company": "Dragonfly",
    "to": "careers@dragonflydb.io",
    "subject": "Control-plane internship",
    "resumePath": "tailored_resumes/full/dragonfly_resume.pdf",
    "body": "Hi Dragonfly team,\n\nDragonfly's in-memory data platform stood out to me because the surrounding control-plane, cloud, and developer-facing systems have to be fast and reliable. I would like to be considered for backend infrastructure internship work.\n\nMy closest work is backend infrastructure with Redis/PostgreSQL-heavy state paths. I built Seaweed, a coding-assessment platform, where I handled workflows for 500+ concurrent users and redesigned ranking around PostgreSQL materialized views to reduce cost while preserving low-latency reads. I have also built a distributed inference engine with worker health, routing, and streaming APIs.\n\nIf this background is useful, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_06.md"
  },
  {
    "company": "Mintlify",
    "to": "support@mintlify.com",
    "subject": "Developer tooling work",
    "resumePath": "tailored_resumes/full/mintlify_resume.pdf",
    "body": "Hi Mintlify team,\n\nMintlify sits at the intersection of developer experience, docs-as-product, AI-assisted knowledge workflows, and review loops, which is a space I would like to work in. I would like to be considered for developer tooling internship work.\n\nThe relevant overlap is developer-facing tooling and traceable AI behavior. I built Murdoc, an AI/tool gateway, and worked on LLM/tool traffic with route profiles, policy checks, traces, metrics, and replayable decisions. I also built Seaweed, a coding-evaluation platform, where judging results, telemetry, and review workflows need to stay understandable.\n\nWould you be open to considering me for an internship around developer tooling?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_06.md"
  },
  {
    "company": "Novaflow",
    "to": "contact@novaflowapp.com",
    "subject": "Scientific workflow infra",
    "resumePath": "tailored_resumes/full/novaflow_resume.pdf",
    "body": "Hi Novaflow team,\n\nNovaflow's scientific workflow work caught my attention because it seems to need reliable model-backed tooling, data pipelines, and inspectable outputs. I would be glad to intern on backend ML infrastructure work in that space.\n\nIn Google Summer of Code with Invesalius, an open-source medical imaging application, I worked on MRI segmentation tooling where model output needed to be fast, inspectable, and usable inside a scientific workflow. I have also built backend infrastructure for inference and AI/tool decisions, including worker health, streaming APIs, traces, metrics, and replayable records.\n\nIf this lines up with any internship work, I would appreciate being pointed in the right direction.\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_06.md"
  },
  {
    "company": "ClickHouse",
    "to": "careers@clickhouse.com",
    "subject": "Data systems internship",
    "resumePath": "tailored_resumes/full/clickhouse_resume.pdf",
    "body": "Hi ClickHouse team,\n\nClickHouse's work on real-time analytics, high-volume observability data, cloud database infrastructure, and query-speed/reliability tradeoffs is the kind of systems work I want to learn from. I would like to be considered for backend data systems internship work.\n\nMy closest work is backend data infrastructure. I built Seaweed, a coding-assessment platform, where I used PostgreSQL materialized views and concurrent refreshes for ranking across 500+ users, reducing infrastructure cost by about 70%. I also built Postificus, a browser workflow platform, where service reliability depends on queues, retries, Redis/PostgreSQL state, metrics, and health checks.\n\nWould it make sense to consider me for a backend data systems internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_07.md"
  },
  {
    "company": "CockroachDB",
    "to": "recruiting@cockroachlabs.com",
    "subject": "Database backend internship",
    "resumePath": "tailored_resumes/full/cockroachdb_resume.pdf",
    "body": "Hi Cockroach Labs team,\n\nCockroachDB's work around distributed SQL, resilience, correctness, and operational scale matches the systems I have been building. I would like to be considered for backend database infrastructure internship work.\n\nMy closest work is database-backed backend infrastructure. I built Seaweed, a coding-assessment platform, where PostgreSQL materialized views and concurrent refreshes keep leaderboard behavior live for 500+ users. I also redesigned an earlier Redis + DynamoDB-style path into a PostgreSQL-centered architecture while preserving correctness and low-latency reads.\n\nIf this is relevant, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_07.md"
  },
  {
    "company": "Grafana Labs",
    "to": "info@grafana.com",
    "subject": "Grafana OpenTelemetry work",
    "resumePath": "tailored_resumes/full/grafana_labs_resume.pdf",
    "body": "Hi Grafana Labs team,\n\nGrafana's open-source observability work and Grafana Cloud stood out to me because they align with the infrastructure I have been building. I would like to be considered for backend observability internship work.\n\nMy closest work is observability-heavy backend work. I built Murdoc, an AI/tool gateway, and instrumented traffic with OpenTelemetry traces, Prometheus health checks, route profiles, and audit logs tied to policy outcomes. I also built Postificus, a browser workflow platform, and used metrics, retries, DLQs, circuit breakers, and health checks around queue workers and long-running jobs.\n\nWould you be open to considering me for a backend observability internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_07.md"
  },
  {
    "company": "Redis",
    "to": "recruiting@redis.com",
    "subject": "Backend infrastructure internship",
    "resumePath": "tailored_resumes/full/redis_resume.pdf",
    "body": "Hi Redis team,\n\nMy strongest project work has been around Redis-backed systems, low-latency reads, real-time state, worker coordination, and AI/data paths where fast context access matters. I would like to be considered for backend infrastructure internship work at Redis.\n\nMy strongest overlap is backend state and low-latency workflow design. I built Postificus, a browser workflow platform, where Redis state works alongside RabbitMQ retries, PostgreSQL persistence, health checks, metrics, and circuit breakers. I also built Seaweed, a coding-assessment platform, where ranking uses materialized views while preserving fast reads.\n\nIf this background is useful for internship work at Redis, could you point me to the right next step?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_07.md"
  },
  {
    "company": "YugabyteDB",
    "to": "info@yugabyte.com",
    "subject": "PostgreSQL backend work",
    "resumePath": "tailored_resumes/full/yugabytedb_resume.pdf",
    "body": "Hi Yugabyte team,\n\nYugabyte's PostgreSQL-compatible distributed database work is close to the backend data systems I have been building. I would like to be considered for backend database internship work.\n\nMy closest work is PostgreSQL-backed backend infrastructure. I built Seaweed, a coding-assessment platform, where materialized views and concurrent refreshes keep ranking behavior live for 500+ users. I also redesigned a Redis + DynamoDB-style path into a PostgreSQL-centered architecture while keeping ranking correctness and low-latency reads.\n\nWould it make sense to consider me for a backend database internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_07.md"
  },
  {
    "company": "Apica",
    "to": "support@apica.io",
    "subject": "Telemetry backend work",
    "resumePath": "tailored_resumes/full/apica_resume.pdf",
    "body": "Hi Apica team,\n\nApica's platform work around telemetry pipelines, observability data, AI and LLM observability, and cost-aware monitoring maps closely to my projects. I would like to be considered for backend telemetry internship work.\n\nMy closest work is telemetry-heavy backend work. I built Murdoc, an AI/tool gateway, and instrumented traffic with OpenTelemetry traces, Prometheus health checks, route profiles, and audit logs. I also built Postificus, a browser workflow platform, and used metrics, retries, DLQs, circuit breakers, and health checks around distributed Go workers and long-running jobs.\n\nIf this is relevant, could you point me to the right person for internship opportunities?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_08.md"
  },
  {
    "company": "Atlan",
    "to": "work@atlan.com",
    "subject": "AI context infrastructure",
    "resumePath": "tailored_resumes/full/atlan_resume.pdf",
    "body": "Hi Atlan team,\n\nAtlan's context layer for enterprise AI stood out to me because it is close to my work around preserving context, traces, metadata, and replayable agent decisions. I would like to be considered for backend AI infrastructure internship work.\n\nI built Murdoc, an AI gateway that preserves context around prompts, tools, retrieved data, policy decisions, and outputs through structured traces and audit logs. I also built Penny Lane, a multi-agent research workflow, where roles, debate, risk review, memory, JSONL traces, and baseline comparisons make decisions easier to inspect.\n\nWould it make sense to consider me for a backend AI infrastructure internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_08.md"
  },
  {
    "company": "Azul",
    "to": "support@azul.com",
    "subject": "Runtime cost systems",
    "resumePath": "tailored_resumes/full/azul_resume.pdf",
    "body": "Hi Azul team,\n\nAzul's work around runtime performance, cloud cost optimization, production reliability, and runtime intelligence matches the infrastructure problems I want to learn from. I would like to be considered for backend platform internship work.\n\nMy closest work is backend infrastructure where cost and runtime behavior matter. I built Seaweed, a coding-assessment platform, where PostgreSQL materialized views reduced infrastructure cost by about 70% while preserving low-latency reads. I also built Postificus, a browser workflow platform, where queues, retries, state, metrics, and health checks keep jobs reliable.\n\nIf this background is useful, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_08.md"
  },
  {
    "company": "Cloud.in",
    "to": "careers@cloud.in",
    "subject": "AWS cloud internship",
    "resumePath": "tailored_resumes/full/cloud_in_resume.pdf",
    "body": "Hi Cloud.in team,\n\nCloud.in's work across managed cloud, automation, DevOps, AWS workloads, security and compliance, disaster recovery, and production support lines up with my project experience. I would like to be considered for cloud backend internship work.\n\nAt my last internship at Bentham AI, I worked on containerizing backend services, deploying them to Cloud Run, and automating CI/CD with GitHub Actions, improving deployment velocity by 70%. I have also built cloud-style backend projects like Seaweed, a coding-assessment platform, using Go, PostgreSQL, Redis, Judge0, AWS, Docker, queues, health checks, and service metrics.\n\nWould you be open to considering me for a cloud backend internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_08.md"
  },
  {
    "company": "CloudThat",
    "to": "sales@cloudthat.com",
    "subject": "CloudThat backend delivery",
    "resumePath": "tailored_resumes/full/cloudthat_resume.pdf",
    "body": "Hi CloudThat team,\n\nCloudThat's consulting work maps to my project experience in CI and CD, containerized services, observability, platform reliability, AI/ML workloads, and production support. I would like to be considered for cloud backend internship work.\n\nAt my last internship at Bentham AI, I worked on backend deployment with Docker, Cloud Run, and GitHub Actions, improving deployment velocity by 70%. I have also built Seaweed, a coding-assessment platform, and Murdoc, an AI/tool gateway, where deployment, observability, persistent state, and predictable service behavior matter.\n\nIf this is useful for internship work at CloudThat, could you point me to the right next step?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_08.md"
  },
  {
    "company": "Concierto by Trianz",
    "to": "careers@trianz.com",
    "subject": "Concierto backend internship",
    "resumePath": "tailored_resumes/full/concerto_by_trianz_resume.pdf",
    "body": "Hi Trianz team,\n\nConcierto's platform spans cloud transformation, application modernization, managed services, data platforms, and agentic AI workflows, which connects well with my backend work. I would like to be considered for cloud backend internship work around the platform.\n\nAt my last internship at Bentham AI, I worked on Puppeteer/Node automation for MCA filings and deployment work with Docker, Cloud Run, and GitHub Actions. The work was a mix of making operational workflows less manual and making backend services easier to ship and maintain.\n\nWould it make sense to consider me for a cloud backend internship around Concierto?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_09.md"
  },
  {
    "company": "HackerRank",
    "to": "hello@hackerrank.com",
    "subject": "HackerRank evaluation systems",
    "resumePath": "tailored_resumes/full/hackerrank_resume.pdf",
    "body": "Hi HackerRank team,\n\nHackerRank's skills-assessment work maps directly to Seaweed, a technical assessment platform I built. I would like to be considered for backend evaluation internship work.\n\nI built Seaweed, a technical assessment platform where I handled judging, concurrency, result telemetry, ranked shortlisting, and live feedback for coding workflows. I also built Murdoc, an AI/tool gateway, and Penny Lane, a multi-agent research workflow, which gave me practice with evaluation, traceability, policy decisions, and validation around AI-heavy systems.\n\nIf this background is relevant, could you point me to the right internship contact?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_09.md"
  },
  {
    "company": "IBM Cloudability",
    "to": "support@apptio.com",
    "subject": "Cloudability cost systems",
    "resumePath": "tailored_resumes/full/ibm_cloudability_resume.pdf",
    "body": "Hi Cloudability team,\n\nIBM Cloudability sits at the intersection of cloud cost visibility, infrastructure ownership, service metrics, and engineering workflows, which is close to my cost-aware backend work. I would like to be considered for cloud backend internship work.\n\nMy closest work is cost-aware backend infrastructure. I built Seaweed, a coding-assessment platform, where PostgreSQL materialized views reduced infrastructure cost by about 70% while preserving low-latency reads. I also built Postificus, a browser workflow platform, where service reliability depends on retries, Redis/PostgreSQL state, health checks, and metrics for long-running jobs.\n\nWould you be open to considering me for a cloud backend internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_09.md"
  },
  {
    "company": "ManageEngine",
    "to": "resume-us@manageengine.com",
    "subject": "AIOps workflow internship",
    "resumePath": "tailored_resumes/full/manageengine_resume.pdf",
    "body": "Hi ManageEngine team,\n\nManageEngine's work around IT operations, AIOps, observability, support workflows, security, and incident response maps closely to my systems work. I would like to be considered for backend internship work if that background is useful.\n\nMy closest work is operational backend automation. I built Swish, an AI-assisted support workflow system, where conversation context, evidence, deterministic policy handling, and traceable decisions matter. I also built Murdoc, an AI/tool gateway, where OpenTelemetry traces, Prometheus health checks, route profiles, and audit logs tie traffic to policy outcomes.\n\nIf this background fits any backend internship work, I would appreciate being pointed in the right direction.\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_09.md"
  },
  {
    "company": "OceanBase",
    "to": "contact-us@oceanbase.com",
    "subject": "Distributed SQL backend",
    "resumePath": "tailored_resumes/full/oceanbase_resume.pdf",
    "body": "Hi OceanBase team,\n\nOceanBase's work on distributed SQL, transactional workloads, AI data layers, high availability, and production reliability is the kind of backend data work I want to learn from. I would like to be considered for backend database internship work.\n\nMy closest work is backend data infrastructure. I built Seaweed, a PostgreSQL-backed coding-assessment platform, where materialized views and concurrent refreshes keep leaderboards live for 500+ users. I also worked on a distributed inference engine, an ML-serving project that gave me practice with streaming APIs, worker health, and retry-aware orchestration.\n\nCould you let me know whether this would be useful for a backend database internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_09.md"
  },
  {
    "company": "SID",
    "to": "info@sid.ai",
    "subject": "Retrieval systems intern",
    "resumePath": "tailored_resumes/full/sid_resume.pdf",
    "body": "Hi SID team,\n\nSID's Research Intern opportunity caught my attention because the work on agentic retrieval lines up with my projects around LLM routing, retrieval-aware context, latency-sensitive inference, checkpoints, and evaluation workflows.\n\nMy closest work is a distributed inference engine, an ML-serving project I built to run larger models across heterogeneous consumer hardware. The main problems were coordination and reliability: streaming APIs, worker heartbeats, retry-aware orchestration, KV-cache-aware routing, and balancing latency, throughput, and availability.\n\nIf my background fits the Research Intern role, I would be glad to be considered.\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_10.md"
  },
  {
    "company": "Solidroad",
    "to": "support@solidroad.com",
    "subject": "AI support QA systems",
    "resumePath": "tailored_resumes/full/solidroad_resume.pdf",
    "body": "Hi Solidroad team,\n\nSolidroad's AI support QA and customer conversation work is close to systems I have already built. I would like to be considered for product backend internship work.\n\nI built Swish, an AI-assisted support workflow system where conversation context, evidence, deterministic policy handling, and human handoff mattered. I also worked on Murdoc, an AI/tool gateway, which gave me practice making AI decisions inspectable through policy records, traces, metrics, and audit logs.\n\nWould you be open to considering me for a product backend internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_10.md"
  },
  {
    "company": "SubImage",
    "to": "alex@subimage.io,kunaal@subimage.io",
    "subject": "SubImage security work",
    "resumePath": "tailored_resumes/full/subimage_resume.pdf",
    "body": "Hi Alex and Kunaal,\n\nSubImage's work around attack paths, vulnerability management, CSPM, AI asset inventory, and infrastructure mapping lines up with my security and observability projects. I would like to be considered for backend security internship work.\n\nThe strongest overlap for me is AI/security tooling. I built Murdoc, a self-hosted AI security gateway, and experimented with prompt-injection and unsafe-tool defenses, policy checks, RBAC-style settings, PII redaction, traces, metrics, and audit logs. I have also contributed to open-source projects, so I am used to working inside existing codebases with review constraints.\n\nIf this seems useful, could you let me know whether an internship conversation would make sense?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_10.md"
  },
  {
    "company": "PingCAP",
    "to": "careers@pingcap.com",
    "subject": "TiDB backend internship",
    "resumePath": "tailored_resumes/full/tidb_resume.pdf",
    "body": "Hi PingCAP team,\n\nTiDB sits in the space I want to learn from: distributed SQL, open-source database internals, transactional workloads, AI data infrastructure, horizontal scaling, and query performance. I would like to be considered for backend database internship work at PingCAP.\n\nThe strongest overlap is PostgreSQL-backed backend work. I built Seaweed, a coding-assessment platform, where materialized views and concurrent refreshes keep ranking behavior live for 500+ users. I also redesigned a Redis + DynamoDB-style path into a PostgreSQL-centered architecture while keeping ranking correctness and low-latency reads.\n\nWould it make sense to consider me for a backend database internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_10.md"
  },
  {
    "company": "Upwind",
    "to": "support@upwind.io",
    "subject": "Runtime security backend",
    "resumePath": "tailored_resumes/full/upwind_resume.pdf",
    "body": "Hi Upwind team,\n\nUpwind's work across runtime visibility, cloud security posture, attack paths, vulnerability management, AI security, API security, and incident response is close to my backend security projects. I would like to be considered for backend cloud security internship work.\n\nThe closest overlap is that I built Murdoc, a self-hosted AI security gateway where I experimented with prompt-injection and unsafe-tool defenses, policy checks, RBAC-style settings, PII redaction, traces, metrics, and audit logs. I have also built Postificus, a browser workflow platform, where backend reliability depends on retries, persistent state, metrics, health checks, and failure isolation.\n\nIf this background is relevant, could you point me to the right next step for an internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_10.md"
  },
  {
    "company": "Xurrent",
    "to": "info@xurrent.com",
    "subject": "Service workflow backend",
    "resumePath": "tailored_resumes/full/xurrent_resume.pdf",
    "body": "Hi Xurrent team,\n\nXurrent's service workflow, incident context, automation, integrations, and operational analytics match the kind of systems I have been building. I would like to be considered for backend internship work if that background is useful.\n\nMy closest work is operational workflow automation. I built Swish, an AI-assisted support workflow system, where conversation context, evidence, deterministic policy handling, and human handoff matter. I also built Postificus, a browser workflow platform, where queues, retries, Redis/PostgreSQL state, metrics, health checks, and circuit breakers keep long-running jobs reliable.\n\nCould you let me know whether this would be worth considering for a backend internship?\n\nI have attached my resume below.\n\nBest,\nShuvam Pal\nGitHub: https://github.com/unichronic",
    "source": "cold_email_drafts_batch_11.md"
  }
];

function previewDrafts() {
  DRAFTS.forEach((draft, index) => {
    const to = clean_(draft.to) || '[ADD TO]';
    Logger.log(`${index + 1}. ${draft.company} -> ${to} | ${draft.subject} | resume: ${draft.resumePath || '[none]'}`);
  });
  Logger.log(`Total drafts: ${DRAFTS.length}`);
}

function previewResumeAttachments() {
  let found = 0;
  let missing = 0;

  DRAFTS.forEach((draft, index) => {
    const fileName = getFileNameFromPath_(draft.resumePath);
    const file = fileName ? findResumeFile_(fileName) : null;

    if (file) {
      found += 1;
      Logger.log(`${index + 1}. FOUND ${draft.company}: ${fileName}`);
    } else {
      missing += 1;
      Logger.log(`${index + 1}. MISSING ${draft.company}: ${fileName || '[no resumePath]'}`);
    }
  });

  Logger.log(`Resume attachments found: ${found}; missing: ${missing}.`);
}

function createDrafts() {
  const label = getOrCreateLabel_(CONFIG.labelName);
  const activeEmail = getSessionEmail_('active');
  const effectiveEmail = getSessionEmail_('effective');
  const selfEmail = activeEmail || effectiveEmail;
  const props = PropertiesService.getUserProperties();

  let created = 0;
  let skipped = 0;

  Logger.log(`Active user email: ${activeEmail || '[blank]'}`);
  Logger.log(`Effective user email: ${effectiveEmail || '[blank]'}`);
  Logger.log(`Draft label: ${CONFIG.labelName}`);

  DRAFTS.forEach((draft, index) => {
    const company = clean_(draft.company) || `Draft ${index + 1}`;
    const originalTo = clean_(draft.to);
    let to = originalTo;
    let subject = clean_(draft.subject) || company;
    let body = String(draft.body || '').trim();

    if (!body) {
      Logger.log(`Skipped ${company}: missing body`);
      skipped += 1;
      return;
    }

    if (!to) {
      if (!CONFIG.createMissingRecipientDraftsToSelf || !selfEmail) {
        Logger.log(`Skipped ${company}: missing recipient`);
        skipped += 1;
        return;
      }
      to = selfEmail;
      subject = `${CONFIG.missingRecipientSubjectPrefix}${subject}`;
      body = `TO FILL: ${company}

${body}`;
    }

    const resumeFileName = getFileNameFromPath_(draft.resumePath);
    const attachments = [];

    if (CONFIG.attachResumes && resumeFileName) {
      const resumeFile = findResumeFile_(resumeFileName);

      if (!resumeFile) {
        Logger.log(`Missing resume attachment for ${company}: ${resumeFileName}`);

        if (CONFIG.requireResumeAttachment) {
          skipped += 1;
          return;
        }
      } else {
        attachments.push(resumeFile.getBlob().setName(resumeFileName));
      }
    }

    const attachmentNames = attachments.map((attachment) => attachment.getName()).join(',');
    const dedupeKey = buildDedupeKey_(company, to, subject, body, attachmentNames);
    if (CONFIG.dedupe && props.getProperty(dedupeKey)) {
      Logger.log(`Skipped duplicate: ${company}`);
      skipped += 1;
      return;
    }

    if (CONFIG.dryRun) {
      Logger.log(`[DRY RUN] ${company} -> ${to} | ${subject} | attachment: ${attachmentNames || '[none]'} | resume: ${draft.resumePath || '[none]'}`);
      created += 1;
      return;
    }

    const options = attachments.length ? { attachments } : {};
    const gmailDraft = GmailApp.createDraft(to, subject, body, options);
    label.addToThread(gmailDraft.getMessage().getThread());
    props.setProperty(dedupeKey, new Date().toISOString());
    Logger.log(`Created draft: ${company} -> ${to} | attachment: ${attachmentNames || '[none]'} | resume: ${draft.resumePath || '[none]'}`);
    created += 1;
  });

  Logger.log(`Done. Created ${created}; skipped ${skipped}.`);
  Logger.log(`Verify in Gmail with: in:drafts label:${CONFIG.labelName}`);
}

function resetDraftDedupe() {
  PropertiesService.getUserProperties().deleteAllProperties();
  Logger.log('Cleared draft dedupe keys.');
}

function verifyCreatedDrafts() {
  const activeEmail = getSessionEmail_('active');
  const effectiveEmail = getSessionEmail_('effective');
  const query = `in:drafts label:${CONFIG.labelName}`;
  const allDrafts = GmailApp.getDrafts();
  const threads = GmailApp.search(query, 0, 100);

  Logger.log(`Active user email: ${activeEmail || '[blank]'}`);
  Logger.log(`Effective user email: ${effectiveEmail || '[blank]'}`);
  Logger.log(`Total drafts visible to this script: ${allDrafts.length}`);
  Logger.log(`Draft search query: ${query}`);
  Logger.log(`Matching draft threads found: ${threads.length}`);
}

function getOrCreateLabel_(name) {
  const existing = GmailApp.getUserLabelByName(name);
  return existing || GmailApp.createLabel(name);
}

function clean_(value) {
  return String(value || '').trim();
}

function buildDedupeKey_(company, to, subject, body, attachmentNames) {
  const raw = [company, to, subject, body, attachmentNames || ''].join('\n');
  const digest = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, raw);
  return `draft:${Utilities.base64EncodeWebSafe(digest)}`;
}

function getFileNameFromPath_(path) {
  const parts = String(path || '').split('/');
  return clean_(parts[parts.length - 1]);
}

function findResumeFile_(fileName) {
  if (!fileName) {
    return null;
  }

  const folderId = clean_(CONFIG.resumeDriveFolderId);
  const files = folderId
    ? DriveApp.getFolderById(folderId).getFilesByName(fileName)
    : DriveApp.getFilesByName(fileName);

  return files.hasNext() ? files.next() : null;
}

function getSessionEmail_(kind) {
  try {
    const user = kind === 'effective' ? Session.getEffectiveUser() : Session.getActiveUser();
    return user && user.getEmail ? String(user.getEmail() || '').trim() : '';
  } catch (error) {
    return '';
  }
}
