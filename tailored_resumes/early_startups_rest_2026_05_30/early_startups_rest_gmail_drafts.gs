/**
 * Gmail draft creator for early-startup internship outreach.
 *
 * How to use:
 * 1. Open https://script.google.com and create a new Apps Script project.
 * 2. Upload or sync the PDFs from startup_email_attachments_2026_05_30/ to one Google Drive folder.
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
  labelName: 'early-startup-internship-drafts',
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
