# Social Lead Internship Application Materials

Checked on 2026-05-26. Resume PDFs are in `tailored_resumes/social_leads_2026_05_26/`.

## Priority

| Priority | Lead | Apply | Resume | Fit |
| --- | --- | --- | --- | --- |
| 1 | Metronis foundation team | `arnav@metronis.space` | `metronis_foundation_intern_resume.pdf` | Very strong: Hyoka maps directly to Aegis eval/training/memory infra. |
| 2 | Omli AI/ML or platform | `sidd@omli.in` | `omli_ai_ml_platform_intern_resume.pdf` | Very strong: speech loop + AI eval/platform work. |
| 3 | Morphle Software Engineer Intern | `shrinidhi.jade@morphle.in` | `morphle_software_engineer_intern_resume.pdf` | Very strong if Bangalore/in-office works: medical imaging + robotics. |
| 4 | SigTuple Software Engineer Intern | `teamhr@sigtuple.com` | `sigtuple_software_engineer_intern_resume.pdf` | Very strong: AI + robotics diagnostics + GSoC medical imaging. |
| 5 | Monsoon Tech Intern | `https://lnkd.in/gJKMfxhA` or comment on LinkedIn | `monsoon_tech_intern_resume.pdf` | Strong technically, but Hyderabad daily in-office is the blocker. |
| 6 | Banking Stack Tech Intern | LinkedIn DM/comment | `banking_stack_tech_intern_resume.pdf` | Strong if 6+ months WFO Bengaluru is possible. |
| 7 | Binary AI Intern | `https://binary.so/em2PZRF` | `binary_ai_intern_resume.pdf` | Good if HSR Layout Monday-Saturday and immediate joining are acceptable. |
| 8 | Navi CloudOps Engineer - I | TurboHire link | `navi_cloudops_engineer_resume.pdf` | Moderate: strong reliability/backend, weaker AWS/Terraform/networking depth. |
| 9 | Walmart Grad Intern | Workday link | `walmart_grad_intern_resume.pdf` | Moderate, but the provided Workday page reports posting unavailable. |

The two Dr. Sanjeev Sabharwal LinkedIn links did not expose usable post content publicly, so I did not create role-specific applications for them.

## Apply Links And Sources

- Monsoon Tech Intern post: `https://www.linkedin.com/posts/charann06_tech-intern-at-monsoon-hyderabad-summer-share-7463351262588153856-7oFs`
- Monsoon form: `https://lnkd.in/gJKMfxhA`
- Banking Stack post: `https://www.linkedin.com/posts/abhijit-das-s_techinternship-internship-ai-share-7463605089983770624-aBJP`
- Metronis post/contact: `arnav@metronis.space`
- Metronis site: `https://www.metronis.space/`
- Morphle apply email: `shrinidhi.jade@morphle.in`
- Morphle site: `https://www.morphlelabs.com/`
- Morphle role PDF found in search: `https://guesthouseb.nitj.ac.in/uploads/job_attachments/1762764723476-Full%20Stack%20Engineer%20%28Intern%2BFTE%29%20-%20Morphle%20Labs%20%28YC%29%20.pdf`
- SigTuple apply email: `teamhr@sigtuple.com`
- SigTuple company page: `https://sigtuple.com/aboutus`
- Binary AI Intern form: `https://binary.so/em2PZRF`
- Omli post: `https://www.linkedin.com/posts/gksiddhant_internship-season-is-back-at-omli-we-are-share-7464659010793869312-zJ_u/`
- Omli site: `https://www.omli.in/`
- Navi TurboHire: `https://navi.turbohire.co/job/publicjobs/57a902de-8498-40b6-b95a-5d5144a825e9`
- Walmart Workday: `https://walmart.wd5.myworkdayjobs.com/en-US/WalmartExternal/job/XMLNAME--IND--Grad-Intern---No-Work-Experience_R-2509924`

## Metronis Email

Subject: Foundation team intern - backend/infra for agent evals

Hi Arnav,

I saw your post about Metronis hiring 2-3 interns for the foundation team. I am interested in the backend + infra / applied ML side.

The reason Metronis stood out is that Aegis is very close to what I have been building in Hyoka: trace ingestion, eval/replay runs, failure mining, validation runs, release gates, signed artifacts, worker leases, and audit logs for AI-agent behavior. I like the idea of making traces, training, and memory share one reliable record instead of treating evals as a separate dashboard.

A few relevant things I have shipped:

- Hyoka: AI-agent reliability control plane with SDK/proxy/OTLP ingestion, evaluators, replay, gates, signed manifests, and a Next.js dashboard.
- Swish: support-agent workflow with grounded context, deterministic policy checks, Langfuse traces, and regression cases.
- Bentham AI: production automation with Docker, Cloud Run, GitHub Actions, retries, and recoverable browser/API workflows.

I would be useful on trace intake, API/CLI workflows, eval orchestration, worker execution, artifact lineage, release gates, deployment, or observability.

Resume: attached  
GitHub: `https://github.com/unichronic`

Best,  
Shuvam

Attach: `metronis_foundation_intern_resume.pdf`

## Omli Email

Subject: AI/ML or platform internship - Shuvam Pal

Hi Sidd,

I saw your post about Omli internships and read about Omli Kids. I am interested in the AI/ML or platform role.

The closest work I have done is a local speech-agent loop where I worked with STT/TTS experiments, Moonshine Hindi ASR tuning, ONNX Runtime, Sherpa-ONNX, Piper TTS, WER checks, and first-audio latency tracking. Separately, I have built Hyoka, an AI-agent reliability/control plane for traces, evals, replay, validation runs, and release gates.

I am also comfortable on backend/product work. At Bentham AI, I shipped production automation with Node.js, Docker, Cloud Run, GitHub Actions, retries, and state recovery. In GSoC, I worked inside Invesalius on Python model-output workflows and reduced runtime by 87%.

Keeping this short: I like building systems where the AI part is measurable, debuggable, and useful in the actual product. Omli's speech + kids + consumer-product angle is exactly the kind of problem I would like to work on.

Resume: attached  
GitHub: `https://github.com/unichronic`

Best,  
Shuvam

Attach: `omli_ai_ml_platform_intern_resume.pdf`

## Morphle Email

Subject: Software Engineer Intern - Shuvam Pal

Hi Shrinidhi,

I saw the Software Engineer Intern opening for Morphle Labs and wanted to apply.

Morphle stood out because the work is at the intersection of medical imaging, robotics, and software workflows. My strongest relevant experience is from Google Summer of Code with Invesalius, where I worked on Python medical-imaging/model-output tooling for MRI segmentation across 95 anatomical regions, including preprocessing, generated masks, large-volume data paths, and 3D inspection. I also reduced runtime by 87% using async/parallel execution.

On the software side, I have built and shipped full-stack/backend systems:

- Seaweed: React/Next.js + Go + PostgreSQL assessment platform used by 500+ concurrent users.
- Postificus: Go/Echo workflow automation with PostgreSQL, Redis, RabbitMQ, retries, DLQs, and Prometheus.
- Bentham AI: production automation with Node.js, Docker, Cloud Run, GitHub Actions, and recoverable browser/API workflows.

I would be excited to work on Morphle's web-based digital pathology workflows, image-processing systems, scanner software interfaces, or product engineering around doctors/labs.

Resume: attached  
GitHub: `https://github.com/unichronic`

Best,  
Shuvam Pal

Attach: `morphle_software_engineer_intern_resume.pdf`

## SigTuple Email

Subject: Software Engineer Intern - Shuvam Pal

Hi Team,

I am applying for the Software Engineer Intern role at SigTuple.

SigTuple's work in AI-assisted microscopy and robotics is very close to the kind of medical-imaging engineering I worked on during Google Summer of Code. At Invesalius, I built Python model-output workflows for MRI segmentation across 95 anatomical regions, handled preprocessing and generated masks, debugged PyTorch/ONNX-style inference paths, and improved runtime by 87% using async/parallel execution.

I also have product/backend experience from Bentham AI, where I shipped automation services with Node.js, Docker, Cloud Run, GitHub Actions, retries, state validation, and operator-visible failure recovery. My projects include Hyoka for AI-agent eval/replay infrastructure and Seaweed, a full-stack judging platform with Go, React, PostgreSQL, Redis, and Docker.

I would be happy to contribute to engineering work around diagnostics workflows, model-output reliability, backend services, internal tools, or product systems.

Resume: attached  
GitHub: `https://github.com/unichronic`

Best,  
Shuvam Pal

Attach: `sigtuple_software_engineer_intern_resume.pdf`

## Monsoon Comment / Form Answer

Use this as the LinkedIn comment if you want to apply through the comments:

Seaweed - end-to-end contest/evaluation platform with React/Next.js, Go, PostgreSQL, Redis, Judge0, auth, submissions, admin review, live rankings, and reproducible judging records. Built for 500+ concurrent users with sub-5s P95 verdict latency. GitHub: `https://github.com/unichronic/seaweed-fe`

If the form asks for a short project description, use:

Seaweed is a full-stack contest/evaluation platform I built with React/Next.js, Go, PostgreSQL, Redis, Judge0, and Docker/Kubernetes. It handles auth-gated problem pages, code submissions, admin review, live rankings, and reproducible result records for 500+ concurrent users. I also have maintainer-reviewed open-source contributions across Invesalius, IOOS, Tiled, VideoLAN, CRIU, Kyverno, and Kuadrant.

Attach: `monsoon_tech_intern_resume.pdf`

## Banking Stack DM

Hi Abhijit,

I saw your post about the 6-month WFO tech internship for the banking stack. I am interested.

I am based in Bengaluru and I have shipped full-stack/backend projects end to end, not n8n/vibe-coded demos. A few relevant ones:

- Seaweed: React/Next.js + Go + PostgreSQL assessment platform with submissions, judging, admin review, and live rankings.
- Postificus: Go/Echo backend with PostgreSQL, Redis, RabbitMQ, retries, DLQs, and browser automation.
- Penny Lane Capital: Python multi-agent financial research workflow with typed state, checkpoints, backtests, and replayable traces.

At Bentham AI, I also built production automation for high-friction filing workflows with retries, state validation, Docker, Cloud Run, and GitHub Actions.

Resume: attached  
GitHub: `https://github.com/unichronic`

Best,  
Shuvam

Attach: `banking_stack_tech_intern_resume.pdf`

## Binary Form

Use these answers:

- Name: Shuvam Pal
- Email: `ishuvam.pal@gmail.com`
- HSR Layout Monday-Saturday: Yes, if you are actually okay with it. If not, do not apply.
- Immediate joining: I can join immediately / within X days after selection.
- Current location: Bengaluru, Karnataka
- College: Dayananda Sagar College of Engineering
- CV: `binary_ai_intern_resume.pdf`

If there is an extra intro field:

I am an AIML undergraduate at DSCE, Bengaluru. I have built AI/product systems including Hyoka, an AI-agent reliability control plane with trace ingestion, eval/replay, validation runs, release gates, and audit logs; Swish, a support-agent workflow using grounded context, pgvector, Redis state, and Langfuse traces; and Penny Lane Capital, a Python multi-agent financial research workflow with checkpoints and replayable traces. I also worked at Bentham AI on production automation with Node.js, Docker, Cloud Run, GitHub Actions, retries, and state recovery.

## Navi Form Note

Apply only if you are comfortable with a CloudOps-heavy role. The JD asks for AWS, Python/Shell, Linux/Windows systems, networking, Docker/Kubernetes, and Terraform/CDK. Your strongest matching points are Docker, backend reliability, CI/CD, Kubernetes, observability, and production debugging. Do not overclaim Terraform/CDK.

Attach: `navi_cloudops_engineer_resume.pdf`

## Walmart Note

The provided Workday page currently reports the posting as unavailable from the page metadata. If it opens for you in browser, use:

Attach: `walmart_grad_intern_resume.pdf`

If it does not open, skip this requisition and look for a fresh Walmart Global Tech Grad Intern requisition instead.
