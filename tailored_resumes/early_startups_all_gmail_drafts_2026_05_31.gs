/**
 * Gmail draft creator for all early-startup spreadsheet outreach.
 *
 * How to use:
 * 1. Open https://script.google.com and create a new Apps Script project.
 * 2. Upload or sync the PDFs from early_startup_all_email_attachments_2026_05_31/ to one Google Drive folder.
 * 3. Paste the folder ID from the Drive URL in CONFIG.resumeDriveFolderId.
 * 4. Paste this whole file into Code.gs.
 * 5. Run previewDrafts() and previewResumeAttachments() to inspect logs.
 * 6. Run createDrafts().
 * 7. Approve Gmail and Drive access once.
 *
 * Notes:
 * - This creates Gmail drafts only. It does not send emails.
 * - If `to` is blank, the draft is created to your own Gmail address and the
 *   subject is prefixed with [ADD TO]. Replace the recipient manually in Gmail.
 * - Apps Script cannot read local paths or local/Colab Drive mounts directly.
 *   resumePath is only used to derive the PDF filename, which is looked up in
 *   Google Drive.
 * - If CONFIG.requireResumeAttachment is true, a draft is skipped when its
 *   matching PDF cannot be found in Drive.
 */

const CONFIG = {
  labelName: 'early-startup-spreadsheet-drafts',
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
    "company": "Atlas",
    "to": "",
    "subject": "Internship inquiry - AI backend / workflow reliability",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/atlas_intern_resume.pdf",
    "body": "Hi Atlas team,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. I was reading about Atlas and the idea of helping accounting firms scale with AI felt very close to the kind of systems work I enjoy: messy workflows, reliable execution, and making AI outputs inspectable enough for real use.\n\nThe closest overlap is my work at Bentham AI (https://www.bentham.legal/). I built backend automation for legal/compliance filing workflows with browser execution, public-site API lookups, retries, session recovery, and operator checkpoints, reducing manual filing time by 85%. I also worked on AI-assisted draft generation for company-name suggestions, object descriptions, and filing fields where the generated output had to stay inspectable before final execution.\n\nI know legal filings and accounting workflows are not the same thing, but the engineering shape feels similar: professional-service workflows, generated drafts, external systems, validation checkpoints, and a need for reliability more than flashy demos. I\u2019ve also built Hyoka, an AI reliability control plane with traces, eval/replay workers, gates, API keys, audit logs, and a dashboard.\n\nIf you are open to interns, I\u2019d be interested in helping with backend, integrations, AI workflow reliability, or internal product tooling. I\u2019ve attached a resume tailored to that kind of work.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Bhindi AI",
    "to": "",
    "subject": "Internship inquiry - AI agents / backend reliability",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/bhindi_ai_intern_resume.pdf",
    "body": "Hi Bhindi team,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. Bhindi\u2019s focus on reducing repetitive work with AI caught my attention because I\u2019ve been building around the less glamorous but important parts of AI systems: traces, evals, replay, tool calls, and making agent behavior easier to trust.\n\nThe backend reliability side is where I think I can be most useful. At Bentham AI (https://www.bentham.legal/), I built backend automation for compliance-sensitive filing workflows with browser execution, public-site API lookups, retries, session recovery, and operator checkpoints. It reduced manual filing time by 85%, and the main lesson was that AI-assisted workflows only work well when the surrounding backend is recoverable and inspectable.\n\nI\u2019ve also built Hyoka, an AI workflow reliability layer with trace ingestion, eval/replay workers, validation runs, gates, API keys, audit logs, and Dockerized services. Separately, Postificus gave me hands-on backend reliability work with RabbitMQ workers, Redis/PostgreSQL state, DLQs, retries, circuit breakers, health checks, and Prometheus metrics.\n\nI\u2019d be glad to contribute as an intern on backend reliability, AI workflow infrastructure, integrations, or eval tooling if there is room on the team. I\u2019ve attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Cent",
    "to": "",
    "subject": "Internship inquiry - ML / healthtech backend",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/cent_intern_resume.pdf",
    "body": "Hi Cent team,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. Cent stood out to me because your product sits at a very practical intersection of diagnostics, imaging, biomarkers, and software workflows.\n\nThe main reason I\u2019m reaching out is my Google Summer of Code work with Invesalius. I worked on a medical-imaging segmentation pipeline for 95 anatomical brain regions, including FastSurfer-style CNN inference, PyTorch/TorchScript and ONNX/TinyGrad paths, NIfTI/MGZ preprocessing, voxel conformation, label remapping, binary masks, QC/debugging, and 3D inspection flows. I also reduced runtime by 87% through async/parallel execution.\n\nThat project made me interested in health software where model outputs and data pipelines have to be correct, inspectable, and useful to real workflows. Alongside that, I\u2019ve built Hyoka for traceable AI evaluation/replay workflows and Swish for policy-grounded operational workflows.\n\nIf Cent is open to interns, I\u2019d be interested in ML/data pipeline, healthtech backend, or internal tooling work. I\u2019ve attached a resume tailored to this direction.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Maieutic Semiconductor",
    "to": "",
    "subject": "Internship inquiry - AI engineering / AI infrastructure",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/maieutic_semiconductor_intern_resume.pdf",
    "body": "Hi Maieutic team,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering. I came across Maieutic\u2019s work on a GenAI copilot for analog IC design, and what stood out to me was the engineering shape of the problem: specs, design context, model outputs, automated reviews, and optimization suggestions all need to be reliable enough for engineers to actually trust.\n\nI don\u2019t come from an analog IC background yet, but I have been building the AI infrastructure side that feels relevant here:\n\n- Hyoka: trace ingestion, eval/replay workers, validation gates, artifacts, audit logs, and a dashboard for inspecting AI workflow behavior.\n- Murdoc: an AI gateway around LLM/tool traffic with route profiles, policy checks, OpenTelemetry traces, Prometheus metrics, and replayable decisions.\n- GSoC with Invesalius: model-inference and preprocessing work for medical-image segmentation, including PyTorch/TorchScript, ONNX-style paths, large data handling, and debugging generated model outputs.\n\nIf there is scope for an intern on AI engineering, AI infrastructure, evaluation/replay systems, Python backend work, or internal tooling around the copilot, I\u2019d be very interested. I\u2019ve attached my resume.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Pulse",
    "to": "info@pulseio.in",
    "subject": "Backend engineering at Pulse",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/pulse_intern_resume.pdf",
    "body": "tl;dr;\n\nI really like what Pulse is building: a full-stack medical equipment platform from India, with serious work around critical care, renal/cardiac categories, manufacturing, quality/compliance, and service support. I want to work on backend systems where the work is practical, operationally important, and has to be correct because people depend on it.\n\nHi,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering, reaching out to ask if there is room for a backend engineering intern at Pulse.\n\nThe part that genuinely interested me is that Pulse is not just selling devices; the company seems to be building the operating backbone around medical equipment: product lifecycle, manufacturing coordination, regulatory/QA, customer support, training, and service workflows. That needs strong backend/internal tooling, not just a nice website.\n\nMy strongest relevant work:\n\n- At Bentham AI (https://www.bentham.legal/), I built backend automation for compliance-sensitive workflows with API lookups, browser execution, retries, session recovery, validation checkpoints, Docker, Cloud Run, and GitHub Actions.\n- In Postificus, I built queue-backed workflow infrastructure with REST APIs, PostgreSQL, Redis, RabbitMQ, retries, DLQs, circuit breakers, health checks, and Prometheus metrics.\n- In Swish, I built support-workflow backend logic around order/item/customer context, escalation paths, evidence strength, policy decisions, PostgreSQL/Redis state, and traceable actions.\n- Through GSoC with Invesalius, I also have healthcare-adjacent engineering exposure from medical-imaging segmentation work, large MRI data handling, generated masks, QC/debugging, and runtime optimization.\n\nIf useful, I\u2019d be glad to work on backend/internal tools for service workflows, inventory/order systems, QA/compliance tooling, customer support operations, or dashboards. I\u2019ve attached my resume.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Trupeer Ai",
    "to": "",
    "subject": "Backend engineering at Trupeer",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/trupeer_ai_intern_resume.pdf",
    "body": "tl;dr;\n\nI like that Trupeer turns a rough screen recording into useful product videos and documentation: action detection, screenshots, scripts, voiceovers, translations, exports, and embeds. I want to work on the backend systems behind that kind of product, where ingestion, job orchestration, retries, generated artifacts, and reliability matter as much as the AI layer.\n\nHi,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering, reaching out to ask if there is room for a backend engineering intern at Trupeer.\n\nThe part that stood out to me is that Trupeer\u2019s product is not just \u201cgenerate a video.\u201d It has to handle screen-recording upload/recording, step detection, editing, brand rules, translations, sharing, exports, and integrations with tools like Notion, Zendesk, and Intercom. That looks like a backend-heavy product with long-running AI/media jobs and a lot of operational edge cases.\n\nMy strongest relevant work:\n\n- Postificus: built queue-backed Go services for content/workflow automation with REST APIs, PostgreSQL, Redis, RabbitMQ, retries, DLQs, circuit breakers, browser-fallback execution, health checks, and Prometheus metrics.\n- Hyoka: built an AI eval/replay control plane with trace ingestion, validation runs, replay workers, release gates, API keys, audit logs, generated artifacts, and a dashboard.\n- Bentham AI (https://www.bentham.legal/): built browser/API automation for compliance workflows with session recovery, retries, validation checkpoints, generated drafts, Docker, Cloud Run, and GitHub Actions.\n- Seaweed: built a backend-heavy contest platform with Go/Echo APIs, PostgreSQL result schemas, Firebase Auth, S3-backed submissions, Judge0 judging, admin controls, and live leaderboards for 500+ concurrent users.\n\nIf useful, I\u2019d be glad to work on backend APIs, generation/job orchestration, integrations, browser automation, AI workflow reliability, or internal tooling around Trupeer\u2019s video/documentation pipeline. I\u2019ve attached my resume.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Enerzolve Smart Technologies",
    "to": "contact@enerzolve.com",
    "subject": "Interested in backend/reliability work at Enerzolve",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/enerzolve_smart_technologies_intern_resume.pdf",
    "body": "Hi Enerzolve team,\n\nI\u2019m Shuvam Pal, a B.E. AIML student at Dayananda Sagar College of Engineering, reaching out to ask if there is room for a backend/reliability engineering intern at Enerzolve.\n\nI came across Enerzolve\u2019s work around smart-grid automation, energy storage, EMS/BMS, metering, testing, and validation. What I genuinely liked is that this is software close to real infrastructure, where reliability and clear failure handling matter a lot. That is the kind of backend work I want to get better at.\n\nI should be upfront that I don\u2019t come from an embedded or power-electronics background yet, so I would not pretend to be useful on firmware from day one. The area where I think I can contribute is the backend/platform layer around engineering operations: internal tools, telemetry/data workflows, validation records, dashboards, deployment automation, and making failures easier to inspect and recover from.\n\nSome relevant work from my side:\n\n- Postificus: built queue-backed Go services with REST APIs, PostgreSQL, Redis, RabbitMQ, retries, DLQs, circuit breakers, health checks, and Prometheus metrics for unreliable long-running workflows.\n- Bentham AI (https://www.bentham.legal/): built recoverable browser/API automation with session recovery, validation checkpoints, inspectable failure records, Docker, Cloud Run, and GitHub Actions.\n- Hyoka: built trace/evaluation/replay infrastructure with worker leases, signed manifests, audit logs, generated artifacts, and Postgres-backed metadata.\n\nIf there is any backend, platform tooling, Python automation, telemetry/data workflow, or reliability work where an intern can help, I\u2019d be grateful to be considered. I\u2019ve attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Sedna Horeca",
    "to": "mahad@sedna.in",
    "subject": "Sedna frontend is Doomed",
    "resumePath": "tailored_resumes/early_startups_first8_2026_05_28/sedna_horeca_intern_resume.pdf",
    "body": "Hi Sedna team,\n\nI found this when I tried to open sedna.in -\n\n[inline screenshot]\n\nSlightly dramatic subject line aside, I\u2019m not sending this just to point out a broken page. I came across Sedna while looking into early startups building real operations software, and the work around food operations, procurement, inventory planning, warehousing/cold-chain visibility, and supply-chain workflows looked genuinely interesting to me.\n\nThis feels like backend/platform ops work more than just a dashboard problem. Vendor state, stock movement, order status, background jobs, failures, and operational visibility all have to stay understandable for the teams using the system every day.\n\nMy strongest fit is on that backend/platform side:\n\n- At Bentham AI (https://www.bentham.legal/), I built recoverable browser/API automation for legal/compliance workflows with retries, session recovery, validation checkpoints, inspectable failure records, Docker, Cloud Run, and GitHub Actions.\n- In Swish, I built an operational support backend around order, kitchen, fleet, customer, policy, trust, and evidence context, with workflow state stored in PostgreSQL/Redis.\n- In Postificus, I built a Go workflow backend with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, circuit breakers, health checks, and Prometheus metrics.\n\nI\u2019m looking for an internship where I can work on backend APIs, platform/internal tools, ops workflows, job reliability, dashboards, or data workflow tooling. If there\u2019s a useful way for an intern to help at Sedna, I\u2019d be happy to start with something practical, including reproducing/fixing issues like this if that helps.\n\nI\u2019ve attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "myjobb AI Backend Engineer",
    "to": "support@myjobb.ai",
    "subject": "Backend engineering internship inquiry - myjobb AI",
    "resumePath": "tailored_resumes/myjobb_ai_backend_2026_05_29/myjobb_backend_engineer_resume.pdf",
    "body": "Hi myjobb team,\n\nI went through myjobb and the Backend Gen AI / Full-Stack Intern postings, and wanted to reach out for backend engineering internship opportunities.\n\nWhat stood out to me is that myjobb is not just a job-board UI problem. The hard part seems to be the backend layer behind it: scanning multiple job boards, parsing resumes and job descriptions, removing noisy or duplicate listings, computing useful match scores, managing multiple resumes and application status, and keeping all of that fast enough for jobseekers to actually trust it.\n\nThe closest work I have done:\n\n- At Bentham AI (https://www.bentham.legal/), I built backend automation for compliance workflows with browser execution, public-site API lookups, retries, session recovery, validation checkpoints, generated drafts, Docker, Cloud Run, and GitHub Actions.\n- I have worked on Careers.pointblank.club, a student-developer recruiting surface, including AI-assisted resume analysis to extract skills, project signals, and role-fit summaries from student profiles.\n- In Hyoka, I built an AI evaluation/replay backend with trace ingestion, validation runs, worker leases, release gates, audit logs, an OpenAI-compatible proxy, and PostgreSQL-backed metadata.\n- In Postificus, I worked on queue-backed publishing workflows with REST APIs, PostgreSQL, Redis, RabbitMQ, retries, DLQs, health checks, Prometheus metrics, and recoverable long-running jobs.\n- In Seaweed, I built contest-platform backend flows with Go/Echo, PostgreSQL, Firebase Auth, S3-backed submissions, Judge0 judging, admin controls, and live leaderboards.\n\nI also noticed myjobb 2.0 is currently being prepared for launch, so I imagine reliability, backend velocity, and matching quality matter a lot right now. If there is room for an intern on backend APIs, job/resume parsing workflows, matching infrastructure, application automation, internal tooling, or AI-backed profile analysis, I would be grateful to be considered.\n\nI have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Vibrium",
    "to": "hr@vibrium.ai",
    "subject": "Backend/AI reliability internship inquiry - Vibrium",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/vibrium_ai_backend_intern_resume.pdf",
    "body": "Hi Vibrium team,\n\nI spent time reading about Vibrium's enterprise agentic AI work and wanted to reach out for backend or AI reliability internship opportunities. What stood out to me is that enterprise agents only become useful when the backend around them is reliable: tool execution, integrations, traces, evals, workflow state, and customer-specific guardrails.\n\nThat is the kind of engineering I have been gravitating toward.\n\n- Hyoka is the closest match: I built trace ingestion, validation runs, replay workers, release gates, audit logs, and worker leases for AI workflows.\n- Swish maps to enterprise agent grounding: operational context, deterministic policy, PostgreSQL/Redis state, evidence strength, and escalation paths.\n- Postificus gave me backend reliability experience around queues, retries, DLQs, health checks, Prometheus metrics, and unreliable external integrations.\n\nIf there is room for an intern who can help with agents, integrations, backend workflow reliability, eval tooling, or observability, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Ateli",
    "to": "deepesh@ateli.co.in",
    "subject": "Backend internship inquiry - Ateli",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/ateli_backend_intern_resume.pdf",
    "body": "Hi Ateli team,\n\nI looked into Ateli and liked that the product is solving a very operational problem: reducing chaos between design, vendors, materials, and site execution. That kind of product usually depends on solid backend systems more than flashy UI alone.\n\nThe areas that seemed most interesting to me were vendor onboarding, material/order state, project handovers, inventory visibility, dashboards, and internal tools for urgent site workflows.\n\n- Postificus is my closest match because it handles fragmented external publishing workflows with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, and status tracking.\n- Swish is relevant for operational state modeling: issue type, evidence, desired resolution, trust/context, and escalation paths.\n- Seaweed shows I can build user-facing backend platforms with Go, PostgreSQL, Firebase Auth, S3-backed submissions, Judge0 integration, and live leaderboards.\n\nIf you are open to interns, I would be interested in helping with backend APIs, marketplace operations, vendor/internal tools, or workflow automation. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Kluisz.ai",
    "to": "abhinav@kluisz.ai",
    "subject": "Backend/platform internship inquiry - Kluisz.ai",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/kluisz_ai_platform_intern_resume.pdf",
    "body": "Hi Kluisz.ai team,\n\nI looked into Kluisz.ai/NAVA and the AI-native cloud platform direction stood out to me. The interesting part, from my side, is not just AI usage but the platform layer underneath it: workload control, observability, reliability, developer tooling, and clean operational workflows.\n\nThat is close to the kind of backend/platform work I have been building.\n\n- At Bentham AI (https://www.bentham.legal/), I shipped Dockerized backend services on Cloud Run with GitHub Actions and improved deployment velocity by 70%.\n- Postificus uses workers, queues, retries, health checks, Prometheus metrics, PostgreSQL, Redis, and RabbitMQ around long-running jobs.\n- Hyoka has a control-plane shape: trace ingestion, worker leases, API keys, audit logs, validation runs, and release gates for AI workflows.\n\nIf there is scope for an intern on backend services, platform tooling, workload reliability, observability, or internal developer tools, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "STCH",
    "to": "enquiry@stch.ai",
    "subject": "Backend/product engineering internship inquiry - STCH",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/stch_backend_product_intern_resume.pdf",
    "body": "Hi STCH team,\n\nI looked into STCH and liked that the product is applying AI to fabric R&D and manufacturing workflows, where the hard part is not only model output but turning experiments, data, and production context into reliable software.\n\nThe backend work that stood out to me was structured experiment data, workflow states, dashboards, search/recommendation, and integrations with production systems.\n\n- Hyoka fits this kind of work because it treats generated outputs as things to evaluate, replay, gate, audit, and promote rather than accept blindly.\n- Postificus is relevant for backend workflow reliability: REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, and Prometheus metrics.\n- My GSoC work with Invesalius gave me experience debugging data correctness and generated artifacts inside a mature technical application.\n\nIf there is room for an intern on backend APIs, AI workflow tooling, data capture, internal dashboards, or product engineering, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Grevoro",
    "to": "info@grevoro.com",
    "subject": "Backend/data internship inquiry - Grevoro",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/grevoro_backend_data_intern_resume.pdf",
    "body": "Hi Grevoro team,\n\nI looked into Grevoro and liked that the work is tied to low-carbon industrial operations rather than being a purely software-only product. That usually makes the software problems more practical: data coming from real processes, messy operational state, and reporting that has to be trusted.\n\nIf Grevoro builds internal software, the useful areas seem to be operational data workflows, process metrics, reporting, monitoring, and tools around manufacturing execution.\n\n- Postificus shows my backend reliability experience: REST APIs, queues, Redis/PostgreSQL state, retries, DLQs, health checks, and metrics around long-running workflows.\n- At Bentham AI (https://www.bentham.legal/), I built automation around messy external systems with API lookups, session recovery, validation checks, and operator checkpoints.\n- My GSoC work involved heavy Python data-processing paths, generated artifacts, correctness checks, and runtime optimization in a mature application.\n\nIf there is room for an intern on Python/data workflows, internal tools, monitoring, operational dashboards, or backend automation, I would be interested in helping. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "PRED",
    "to": "amit@pred.app",
    "subject": "Backend systems internship inquiry - PRED",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/pred_backend_systems_intern_resume.pdf",
    "body": "Hi PRED team,\n\nI looked into PRED and the sports prediction exchange angle stood out because the backend has to be correct, live, and observable. Prediction products cannot afford vague state handling; data feeds, user/account state, market state, settlement, and monitoring all have to line up.\n\nThat is the part I would be most useful around.\n\n- Postificus gives the queue/reliability piece: RabbitMQ workers, retries, DLQs, Redis/PostgreSQL state, health checks, and metrics.\n- Seaweed maps to live user-facing state: Go/Echo services, PostgreSQL, Firebase Auth, S3-backed submissions, Judge0 judging, and live leaderboards for 500+ concurrent users.\n- Penny Lane is relevant to the decision/risk side: market research workflows, typed state, backtests, scorecards, and replayable traces.\n\nIf you are open to interns, I would be interested in backend work around APIs, data feeds, real-time state, risk/settlement workflows, or observability. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Aamra Seniors Club",
    "to": "info@aamra.life",
    "subject": "Backend/internal tools internship inquiry - Aamra",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/aamra_seniors_club_backend_ops_intern_resume.pdf",
    "body": "Hi Aamra team,\n\nI looked into Aamra and liked that it is a real care/service operation, not just a generic health app. For a senior-care day club, good internal software can quietly remove a lot of friction for staff and families.\n\nThe areas that seemed most useful were member records, scheduling, check-ins, family communication, follow-ups, and internal operations tooling.\n\n- Swish is my closest project because it models support/care-like operational state: case context, evidence strength, desired resolution, trust/context, and escalation paths.\n- At Bentham AI (https://www.bentham.legal/), I built backend automation around multi-step workflows, API lookups, validation checks, and operator checkpoints.\n- Seaweed shows I can ship user-facing backend flows with Go, PostgreSQL, Firebase Auth, S3-backed submissions, Judge0 integration, and stable live views.\n\nIf there is room for an intern on internal tools, member/scheduling systems, backend APIs, dashboards, or care-ops workflow automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Puresta",
    "to": "ashish@puresta.in",
    "subject": "ML/backend internship inquiry - Puresta",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/puresta_ml_backend_intern_resume.pdf",
    "body": "Hi Puresta team,\n\nI looked into Puresta and the health plus beauty direction, especially AI-assisted skin analysis and dermatology workflows, felt close to work I have already done. The interesting part to me is making model outputs useful in a real product: image/data pipelines, reviewable outputs, consultation flows, and reliable backend state.\n\nMy closest relevant work:\n\n- My GSoC work with Invesalius is directly relevant: I integrated segmentation workflows for 95 anatomical regions, generated masks, correctness checks, and optimized heavy image-processing paths by 87%.\n- Hyoka adds the evaluation/replay side: trace ingestion, validation runs, release gates, audit logs, and reviewable generated outputs.\n- Swish and Postificus show backend product reliability around operational workflows, PostgreSQL/Redis state, retries, status tracking, and human-reviewable decisions.\n\nIf there is scope for an intern around image/health AI workflows, backend APIs, consultation/product workflows, or eval/replay tooling, I would be very interested. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Frex",
    "to": "aditya@frexpay.com",
    "subject": "Backend internship inquiry - Frex",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/frex_fintech_backend_intern_resume.pdf",
    "body": "Hi Frex team,\n\nI looked into Frex and liked the focus on simplifying international money movement. The backend problems around cross-border payments seem reliability-heavy: partner APIs, workflow validation, compliance/KYC steps, audit trails, retries, and operational dashboards.\n\nThat is close to the kind of backend work I have been doing.\n\n- At Bentham AI (https://www.bentham.legal/), I built backend automation for compliance-sensitive workflows with API lookups, retries, session recovery, validation checks, and checkpoints.\n- Hyoka is relevant because it models audit logs, validation runs, gate decisions, worker leases, and replayable workflow records.\n- Postificus adds the integration reliability side with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, health checks, and metrics.\n\nIf there is room for an intern on backend APIs, partner integrations, KYC/compliance tooling, audit logs, or operational workflow reliability, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "ILIOS 72 Alternative Capital",
    "to": "shivansh@ilios72altcap.co.in",
    "subject": "Backend/data internship inquiry - ILIOS 72",
    "resumePath": "tailored_resumes/early_startups_rest_2026_05_30/ilios_72_fintech_data_intern_resume.pdf",
    "body": "Hi ILIOS team,\n\nI looked into ILIOS 72 and liked the research-backed alternative capital/wealth platform direction. Even at an early stage, this kind of product needs clean internal software: research records, reporting, dashboards, audit trails, portfolio/investor views, and tools that make decisions easier to review.\n\nMy closest relevant work:\n\n- Penny Lane Capital is directly relevant because I built a market-research workflow with analyst roles, risk review, typed state, checkpoints, backtests, scorecards, and replayable traces.\n- Hyoka adds the auditability side: validation runs, gate decisions, audit logs, worker leases, and reviewable workflow records.\n- Postificus shows backend reliability around REST APIs, PostgreSQL/Redis state, queues, retries, DLQs, health checks, and metrics.\n\nIf there is scope for an intern around backend APIs, research/reporting workflows, investor dashboards, analytics tooling, or audit-ready records, I would be interested. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Emergent",
    "to": "mukund@emergent.sh",
    "subject": "Backend/AI platform internship inquiry - Emergent",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/emergent_ai_platform_intern_resume.pdf",
    "body": "Hi Emergent team,\n\nI came across Emergent while going through early AI product companies. The app-builder direction stood out to me because the difficult part is not just generation; it is keeping workflows, integrations, previews, deployment state, and user changes reliable enough for people to trust.\n\nMy closest work is Hyoka, where I built trace ingestion, eval/replay workers, validation gates, audit logs, worker leases, and Postgres-backed metadata for AI workflows. I have also built Postificus, a Go backend around fragmented external workflows with queues, retries, DLQs, health checks, metrics, and recoverable job state.\n\nIf there is room for an intern on backend APIs, AI workflow reliability, integrations, eval tooling, or internal platform work, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Vimag Labs",
    "to": "",
    "subject": "Python/systems internship inquiry - Vimag Labs",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/vimag_labs_python_systems_intern_resume.pdf",
    "body": "Hi Vimag Labs team,\n\nI found Vimag Labs in an early-startup tracker, but there was not much public detail available from my side. From the available signal, it looked closer to EV motor/control or deeptech systems than a normal web product.\n\nI do not want to pretend I can contribute to motor-control firmware from day one. The area where I may be useful is Python tooling, backend/internal tools, data workflows, debugging infrastructure, validation records, and making engineering workflows easier to inspect.\n\nSome relevant work: I built Postificus, a Go backend with workers, retries, DLQs, health checks, and Prometheus metrics; Hyoka, an eval/replay backend with worker leases, audit logs, artifacts, and Postgres metadata; and GSoC work involving Python data-processing paths, generated artifacts, correctness checks, and runtime optimization.\n\nIf there is any Python tooling, backend, data workflow, or internal platform work where an intern can help, I would be glad to be considered. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Dazzl",
    "to": "care@dazzlnow.com",
    "subject": "Backend/product internship inquiry - Dazzl",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/dazzl_backend_product_intern_resume.pdf",
    "body": "Hi Dazzl team,\n\nI came across Dazzl while looking at early Bengaluru/Gurugram startups. The quick beauty-services angle looked interesting because the software behind it has to coordinate bookings, provider availability, customer state, service status, payments, support, and internal ops.\n\nThat is close to the kind of backend/product work I have been building. Swish models operational support state with order, evidence, policy, trust, and escalation context. Postificus gave me queue-backed workflow experience with REST APIs, PostgreSQL, Redis, RabbitMQ, retries, DLQs, health checks, and metrics. Seaweed shows I can build user-facing backend flows with Go, PostgreSQL, Firebase Auth, S3-backed submissions, Judge0, and live views.\n\nIf Dazzl is open to interns on backend APIs, booking/provider workflows, internal tools, dashboards, or support/ops automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Escape Plan",
    "to": "abhinav@myescplan.com",
    "subject": "Backend/full-stack internship inquiry - Escape Plan",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/escape_plan_backend_product_intern_resume.pdf",
    "body": "Hi Escape Plan team,\n\nI came across Escape Plan while mapping early consumer startups. If you are building travel/luggage commerce software in-house, the backend work looks practical: catalog, checkout, order status, customer support, inventory, personalization, and internal tools.\n\nMy relevant work is around product workflows rather than generic landing pages. Swish models support and escalation state; Postificus handles queue-backed workflows with PostgreSQL/Redis state, retries, DLQs, and metrics; and Seaweed shows user-facing backend work with auth, submissions, admin controls, and live views.\n\nIf there is room for an intern on backend/full-stack product work, ecommerce workflows, internal tools, or ops dashboards, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Peeko",
    "to": "chetan.sharma@peekonow.com",
    "subject": "Backend/product internship inquiry - Peeko",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/peeko_backend_product_intern_resume.pdf",
    "body": "Hi Peeko team,\n\nI came across Peeko while looking at early consumer-commerce startups. A babycare quick-commerce product seems to need dependable backend workflows around catalog, inventory, delivery slots, order state, customer support, and internal operations.\n\nThe work I can bring is mostly backend/product reliability. Swish models support cases with operational context and deterministic policy; Postificus handles long-running workflows with queues, retries, DLQs, health checks, and metrics; and Seaweed shows I can ship user-facing backend flows with auth, admin controls, and live status.\n\nIf you are open to interns on backend APIs, inventory/order workflows, internal tools, dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "PB Healthcare",
    "to": "",
    "subject": "Healthtech/backend internship inquiry - PB Healthcare",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/pb_healthcare_healthtech_backend_intern_resume.pdf",
    "body": "Hi PB Healthcare team,\n\nI found PB Healthcare in an early-startup tracker, but I did not have enough public detail to identify a specific product page. If you are building healthcare software or internal hospital/clinic workflows, I think my background may still be relevant.\n\nMy strongest match is Google Summer of Code with Invesalius, where I worked on medical-imaging segmentation for 95 anatomical brain regions, generated masks, NIfTI/MGZ MRI preprocessing, label/orientation debugging, and runtime optimization. I have also built Hyoka for traceable AI evaluation/replay workflows and Swish for policy-grounded operational support workflows.\n\nIf there is room for an intern on healthtech backend, data pipelines, internal tools, QA/validation workflows, or AI-assisted product tooling, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "CHINI KUM",
    "to": "priyank@drinkchinikum.com",
    "subject": "Backend/ops tooling internship inquiry - CHINI KUM",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/chini_kum_backend_ops_intern_resume.pdf",
    "body": "Hi CHINI KUM team,\n\nI came across CHINI KUM while looking at early consumer startups. This may be a stretch if you are not hiring software interns, but D2C beverage brands often end up needing useful internal software around ecommerce, inventory, customer support, subscriptions, analytics, and growth workflows.\n\nMy relevant work is backend/product tooling: Swish models support and escalation workflows, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Bentham AI gave me experience building recoverable workflow automation around messy external systems.\n\nIf there is room for an intern on internal tools, ecommerce backend work, analytics/ops dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "CosMoss",
    "to": "",
    "subject": "Backend/ops tooling internship inquiry - CosMoss",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/cosmoss_backend_ops_intern_resume.pdf",
    "body": "Hi CosMoss team,\n\nI came across CosMoss while looking at early consumer/ecommerce startups. If you are building software internally, the useful work likely sits around catalog, checkout, customer support, inventory, CRM, analytics, and operational dashboards.\n\nMy closest work is backend workflow tooling. Swish models support state and escalation decisions, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed shows I can ship user-facing backend flows with auth, admin controls, and live views.\n\nIf there is room for an intern on backend/full-stack internal tools, ecommerce workflows, analytics dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Filli & Me",
    "to": "shikha@filliandme.com",
    "subject": "Backend/ops tooling internship inquiry - Filli & Me",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/filli_and_me_backend_ops_intern_resume.pdf",
    "body": "Hi Filli & Me team,\n\nI came across Filli & Me while mapping early consumer brands. For a school-bag/ecommerce business, the software that can create leverage is often internal: catalog, inventory, order state, customer support, analytics, and fulfillment visibility.\n\nMy relevant work is around backend/product workflows. Swish models support and escalation context, Postificus handles long-running workflow jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed shows user-facing backend work with auth, admin controls, and live status.\n\nIf you are open to interns on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "HandyPanda",
    "to": "contact@handypanda.in",
    "subject": "Marketplace backend internship inquiry - HandyPanda",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/handypanda_marketplace_backend_intern_resume.pdf",
    "body": "Hi HandyPanda team,\n\nI came across HandyPanda while looking at early marketplace startups. Construction/renovation material delivery looks like a stronger software problem than a simple store: vendor inventory, pricing, delivery status, order changes, service reliability, and ops dashboards all matter.\n\nMy closest work is backend workflow reliability. Postificus handles fragmented external workflows with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, health checks, and metrics. Swish models operational support state with evidence, issue type, desired resolution, trust/context, and escalation paths. Seaweed shows I can build user-facing backend flows with Go, PostgreSQL, auth, admin controls, and live views.\n\nIf there is room for an intern on marketplace backend APIs, vendor/order workflows, internal tools, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Nester",
    "to": "support@nesterstore.com",
    "subject": "Backend/ops tooling internship inquiry - Nester",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/nester_backend_ops_intern_resume.pdf",
    "body": "Hi Nester team,\n\nI came across Nester while looking at early ecommerce startups. If you are building internal software around homeware/appliance commerce, useful backend work likely sits around catalog, inventory, checkout, customer support, analytics, and order visibility.\n\nMy relevant work is backend workflow tooling: Swish for support/ops state, Postificus for queue-backed workflow jobs with PostgreSQL/Redis, retries, DLQs, health checks, and metrics, and Seaweed for user-facing backend flows with auth, admin controls, and live views.\n\nIf there is room for an intern on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "OZi",
    "to": "amit@ozi.in",
    "subject": "Backend/product internship inquiry - OZi",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/ozi_backend_product_intern_resume.pdf",
    "body": "Hi OZi team,\n\nI came across OZi while mapping early consumer-commerce startups. A kids/baby quick-delivery app seems to need practical backend systems around catalog, inventory, dispatch, delivery status, customer support, and internal operations.\n\nMy closest relevant work is backend/product workflows. Swish models operational support state, Postificus handles queue-backed jobs with retries, DLQs, health checks, metrics, and PostgreSQL/Redis state, and Seaweed shows user-facing backend flows with Go, PostgreSQL, auth, admin controls, and live views.\n\nIf there is room for an intern on backend APIs, delivery/order workflows, internal tools, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "RARA Barefoot",
    "to": "care@rarabarefoot.in",
    "subject": "Backend/ops tooling internship inquiry - RARA Barefoot",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/rara_barefoot_backend_ops_intern_resume.pdf",
    "body": "Hi RARA Barefoot team,\n\nI came across RARA Barefoot while looking at early consumer brands. This may be a stretch if you are not hiring software interns, but D2C footwear brands often need useful internal tooling around ecommerce, inventory, customer support, analytics, CRM, and fulfillment workflows.\n\nMy relevant work is backend/product tooling. Swish models support and escalation workflows, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Bentham AI gave me experience building recoverable workflow automation around messy external systems.\n\nIf there is room for an intern on internal tools, ecommerce backend work, dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Rotoris",
    "to": "support@rotoris.com",
    "subject": "Backend/ops tooling internship inquiry - Rotoris",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/rotoris_backend_ops_intern_resume.pdf",
    "body": "Hi Rotoris team,\n\nI came across Rotoris while looking at early consumer brands. This may be a stretch if you are not hiring software interns, but a watch/ecommerce brand can still benefit from internal tools around catalog, order visibility, inventory, customer support, analytics, and growth workflows.\n\nMy relevant work is backend/product tooling: Swish for support-state modeling, Postificus for queue-backed workflow jobs with PostgreSQL/Redis, retries, DLQs, health checks, and metrics, and Seaweed for user-facing backend flows with auth, admin controls, and live views.\n\nIf there is room for an intern on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Tvissa",
    "to": "customer.happiness@tvissa.com",
    "subject": "Backend/ops tooling internship inquiry - Tvissa",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/tvissa_backend_ops_intern_resume.pdf",
    "body": "Hi Tvissa team,\n\nI came across Tvissa while looking at early ecommerce brands. For a handcrafted saree or apparel commerce business, useful software often means better catalog workflows, inventory/order visibility, customer support tooling, analytics, and operational dashboards.\n\nMy relevant work is backend workflow tooling. Swish models support and escalation context, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed shows user-facing backend flows with auth, admin controls, and live views.\n\nIf there is room for an intern on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "Unbound",
    "to": "hi@unbound-lifestyle.com",
    "subject": "Backend/ops tooling internship inquiry - Unbound",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/unbound_backend_ops_intern_resume.pdf",
    "body": "Hi Unbound team,\n\nI came across Unbound while mapping early D2C brands. If you are building software internally around skincare/haircare commerce, the useful backend work likely sits around subscriptions, CRM, inventory, customer support, analytics, and growth/ops workflows.\n\nMy closest work is backend/product tooling: Swish for support-state and escalation modeling, Postificus for queue-backed workflow jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed for user-facing backend flows with auth, admin controls, and live views.\n\nIf there is room for an intern on internal tools, ecommerce backend work, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
  },
  {
    "company": "For Real",
    "to": "anurag@for-real.in",
    "subject": "Marketplace/backend internship inquiry - For Real",
    "resumePath": "tailored_resumes/early_startups_remaining_2026_05_31/for_real_marketplace_backend_intern_resume.pdf",
    "body": "Hi For Real team,\n\nI found For Real in an early-startup tracker, but I did not have enough public detail to identify the exact product page. The signal I had was an off-price shopping or online factory-outlet marketplace, which sounds like a backend/product problem around catalog, pricing, order state, inventory, seller flows, and customer support.\n\nMy relevant work is around backend workflow reliability. Seaweed shows user-facing backend flows with Go, PostgreSQL, auth, admin controls, and live views. Postificus handles fragmented external workflows with queues, retries, DLQs, health checks, and metrics. Swish models support/ops state with evidence, issue type, desired resolution, trust/context, and escalation paths.\n\nIf there is room for an intern on marketplace backend APIs, catalog/order workflows, internal tools, dashboards, or support automation, I would be glad to help. I have attached my resume for context.\n\nRegards,\nShuvam Pal\nhttps://github.com/unichronic\nhttps://linkedin.com/in/shuvampal3960"
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
