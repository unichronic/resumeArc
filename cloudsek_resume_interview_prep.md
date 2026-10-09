# CloudSEK Resume Interview Prep

Use these answers as your base script. Keep the tone concrete: problem, implementation, tradeoffs, failure handling, and what you would improve.

## 30-Second Intro

I am Shuvam Pal, an AIML undergrad focused on backend, cloud, and reliability-heavy systems. Most of my work is around Go/Python services, automation workflows, queues, observability, Docker, AWS/GCP, and security-oriented tooling. Recently I worked at Bentham AI where I built browser automation and Cloud Run/GitHub Actions deployment paths, did GSoC with Invesalius on medical-image segmentation, and built projects like Murdoc, Postificus, and Seaweed that involve API gateways, distributed workers, PostgreSQL, Redis, RabbitMQ, Judge0, Prometheus, and containerized deployment.

## Resume Defense Notes

- For Seaweed, the public `seaweed-fe` repo says Kubernetes manifests are in a separate `seaweed-infra` repo. If asked where Kubernetes is, say backend/frontend code is in `seaweed-fe`, while infra manifests were separated for deployment hygiene.
- For Postificus, the repo has RabbitMQ retry/DLQ implementation, Redis cache/autosave/rate-limit usage, S3-compatible storage, Docker Compose, and Prometheus metrics.
- For Murdoc, the repo has FastAPI gateway code, route profiles, policy/PII/prompt-injection checks, decision ledger, OpenTelemetry and Prometheus instrumentation.
- Do not overclaim production ownership. Say "production-style" or "deployed/tested with" unless the interviewer asks about exact live scale.

## Bentham AI

### Short Answer

At Bentham AI, I worked on automating MCA company-registration workflows. I built a Puppeteer/Node.js workflow that handled browser sessions, form retries, CAPTCHA handoff, and state recovery. I also helped containerize backend services with Docker and wired GitHub Actions deployments to Google Cloud Run, which made releases faster and more repeatable.

### Implementation

- The workflow used Puppeteer to drive the MCA portal where normal APIs were not enough.
- I tracked workflow state so a filing could resume from a known step instead of restarting manually.
- I added retry logic around brittle steps like page loads, network-idle waits, form submission, and validation.
- CAPTCHA was handled as a human/vision handoff rather than pretending it was a normal deterministic API call.
- The AI-assisted part generated company-name suggestions, descriptions, and field drafts, but final filing still required validation.
- Docker packaged the service with a consistent runtime.
- GitHub Actions built/tested the service and deployed a container to Cloud Run.
- Cloud Run was useful because it ran a container without managing VMs or Kubernetes nodes and could autoscale request-based workloads.

### Follow-Ups

**Why Puppeteer?**  
Because some workflow steps were only exposed through a browser UI or behaved differently from simple API calls. Puppeteer let me automate the real user path while still adding deterministic state checks.

**How did you avoid flaky automation?**  
I avoided fixed sleeps where possible, waited for specific selectors/network-idle states, retried known transient steps, stored progress state, and validated each step before moving forward.

**Why Cloud Run instead of Kubernetes?**  
For that workload, Cloud Run was simpler. It accepted a Docker container, handled HTTPS and scaling, and did not require node/cluster management. Kubernetes would be justified if we needed more control over networking, scheduling, service mesh, or multiple long-running services.

**How did GitHub Actions improve release velocity?**  
Before automation, release steps were manual and error-prone. The workflow made build and deploy repeatable: checkout, install dependencies, run checks, build image, push/deploy, and use GitHub Secrets for credentials.

## GSoC: Invesalius

### Short Answer

In GSoC, I built medical-image segmentation tooling for brain subparts in Invesalius. The tool used FastSurfer-style CNN models, supported PyTorch and ONNX paths, handled preprocessing/orientation, ran inference, converted labeled output volumes into masks, and integrated the generated masks/surfaces into the existing UI workflow.

### Implementation

- Input was a medical image volume loaded inside Invesalius.
- I implemented preprocessing/conformation so the model received data in the expected orientation, spacing, and shape.
- Model inference produced a labeled segmentation volume.
- Post-processing mapped labels to specific brain subparts.
- Binary masks were generated from the labeled output.
- Masks were categorized in the data panel, such as cortical and subcortical groups.
- I preserved user inspection workflows by integrating with existing mask and surface-generation paths.
- Performance was improved using asynchronous/parallel execution so the UI workflow did not feel blocked.

### Follow-Ups

**Why ONNX?**  
ONNX makes the model easier to run outside a pure PyTorch environment and can help portability. The tradeoff is that conversion/debugging and runtime performance need careful validation.

**What was hard?**  
Medical image orientation and reproducibility. A small mismatch in spacing/orientation can produce plausible-looking but wrong masks, so preprocessing and post-processing had to be explicit.

**How did you verify correctness?**  
By checking generated masks, label mappings, expected anatomy categories, 3D surfaces, and reproducible outputs across runs.

## Open Source

### Short Answer

My open-source work taught me to make small, maintainable patches inside mature codebases. I contributed to Invesalius, IOOS, VideoLAN, CRIU, and Tiled, including security fixes like Zip Slip prevention, parsing robustness, UI bugs, cleanup issues, and compatibility fixes.

### Follow-Ups

**What did you learn from open source?**  
Maintainer constraints matter. A correct patch is not enough; it has to match project style, preserve compatibility, include a clear reproduction or test path, and avoid widening the scope unnecessarily.

**Security example?**  
In Invesalius I worked on a Zip Slip directory traversal fix. The core issue is that extracting archives using untrusted paths can write outside the intended directory. The fix pattern is to normalize paths, verify the final path remains inside the destination, and reject dangerous entries.

## Murdoc

### Short Answer

Murdoc is a self-hosted AI security gateway for LLM, HTTP-tool, and MCP traffic. Instead of trusting prompts or individual agents to enforce policy, Murdoc sits in front of the downstream model/tool/API, normalizes requests, runs security layers, and records an audit-safe decision before execution.

### Implementation

- Built with Python and FastAPI.
- Supports OpenAI-compatible LLM gateway, HTTP tool/API gateway, and MCP proxy paths.
- Shared runtime applies prompt-injection checks, PII scanning/redaction, OPA-compatible policy decisions, semantic guardrails, and output inspection.
- Route profiles configure guardrail modes, latency budget, rate limit, cache behavior, and policy version.
- Decision ledger records request id, route, policy/config versions, layer outcomes, prompt fingerprint, usage estimates, and blocked reason without storing raw secrets.
- Observability uses Prometheus metrics and OpenTelemetry traces.
- The attack lab validates prompt-injection, exfiltration, schema-injection, browser-action hijack, OAuth abuse, retrieval poisoning, and similar cases.

### Follow-Ups

**Why is Murdoc relevant to CloudSEK?**  
CloudSEK is security-focused, and Murdoc shows I understand enforcement boundaries, auditability, policy checks, telemetry, and failure modes around AI/tool traffic.

**How does a request flow?**  
Client request -> gateway adapter -> shared runtime -> prompt scanner -> PII scan/redaction -> policy decision -> optional semantic guardrails -> downstream execution -> output scan/redaction -> decision ledger and metrics.

**What data is stored in audit logs?**  
Decision summaries, prompt hash/fingerprint, route/profile metadata, layer statuses, violations, duration, and usage estimates. Raw prompts, responses, API keys, SSNs, emails, and secrets should not be stored.

## Postificus

### Short Answer

Postificus is a Go/Echo content distribution platform. The API accepts drafting and publishing actions, stores state in PostgreSQL, uses Redis for cache/autosave/rate limiting, sends publish jobs to RabbitMQ workers, and uses browser automation where external publishing APIs are unreliable or unavailable.

### Implementation

- Go/Echo backend exposes REST APIs.
- PostgreSQL stores users, drafts, credentials, and activity state.
- Redis is used for best-effort draft cache, dashboard cache, and IP-based rate limiting.
- RabbitMQ decouples API requests from long-running publish jobs.
- Worker service consumes messages manually, uses retry headers, and moves exhausted jobs to a DLQ.
- Circuit breakers isolate failing platforms like Medium or Dev.to so one bad external dependency does not collapse the whole worker pipeline.
- Prometheus metrics track HTTP latency, DB/Redis durations, publish success/failure, worker jobs, and circuit breaker state.
- Dockerfile builds separate API and worker binaries and installs Chromium dependencies for Go-Rod.
- Docker Compose runs API, worker, PostgreSQL, Redis, RabbitMQ, MinIO/S3, and Grafana Agent locally.

### Follow-Ups

**Why RabbitMQ?**  
Publishing is slow and failure-prone because it depends on external websites and APIs. RabbitMQ lets the API enqueue work quickly and lets workers retry, acknowledge, or DLQ jobs independently.

**What is a DLQ?**  
A dead-letter queue stores messages that could not be processed after retries. It prevents bad jobs from blocking the main queue and gives operators a place to inspect/replay failures.

**What does the circuit breaker do?**  
After repeated failures for a platform, it opens and fails fast for a cooldown period. That protects worker capacity and avoids hammering an unhealthy external dependency.

**Where did Redis fit?**  
Redis held short-lived operational state: draft autosave cache, dashboard cache, and rate-limit counters.

## Seaweed Contest Platform

### Short Answer

Seaweed is a coding-contest platform with Go backend services for registration, submissions, sandboxed execution through Judge0, scoring, and rankings. It uses PostgreSQL for relational contest/submission data, Redis/runtime state where needed, AWS S3 for storing submitted code, Docker for backend packaging, and Kubernetes manifests in a separate infra repo.

### Implementation

- Users register for contests and submit code during valid contest windows.
- Submission service validates contest registration, contest timing, and problem existence.
- Submitted source is stored in S3 under a structured key like `submissions/{contest}/{user}/{submission}`.
- Submission row is written to PostgreSQL with status `pending`.
- Judging runs asynchronously; current code launches judging in a goroutine and calls Judge0 with language ID, stdin, and expected output.
- Judge0 status IDs are mapped to internal states like `pass`, `wrong_answer`, `tle`, and `rte`.
- Results are applied in a PostgreSQL transaction: update submission status, insert test-case results, update rankings, and refresh ranking materialized view.
- Dockerfile builds a static Go binary, copies migrations, exposes port 8080, uses non-root user, and includes a health check.
- Kubernetes deployment lived in `seaweed-infra`, separate from app code.

### Follow-Ups

**Why async judging?**  
Code execution can take seconds and may involve external sandbox capacity. The API should return a submission id quickly, while status/results are fetched later.

**How did you get sub-5s P95 verdict latency?**  
By keeping the submission path lightweight, using Judge0 as the sandbox, storing code in S3, and applying verdict/ranking updates transactionally. For higher scale, I would move from goroutines to a durable queue so jobs survive process restarts.

**What would you improve?**  
Replace in-process goroutines with a queue like RabbitMQ/SQS, add idempotency keys, add worker autoscaling, cache leaderboard reads, and add stronger observability around Judge0 latency/error rates.

**Where was AWS used?**  
S3 stored submitted source code. The app used the AWS SDK default credential chain and a bucket configured through `S3_SUBMISSIONS_BUCKET`. The deployment target mentioned in the resume was AWS with Docker/Kubernetes.

## AWS

**Why did you use AWS?**  
For cloud primitives around storage and deployment. In Seaweed, S3 was useful for durable source-code storage because submitted files are objects, not relational data. Kubernetes on AWS was the deployment target for containerized backend services.

**What AWS services should you mention?**  
S3 confidently. For Kubernetes deployment, say EKS if that is what the infra repo used; otherwise say "Kubernetes on AWS" and avoid naming EKS unless asked. For production hardening, mention IAM roles, least-privilege bucket access, security groups, logs/metrics, and private networking.

**How did credentials work?**  
Application code loaded AWS config through the AWS SDK default provider chain. In production this should come from IAM roles/service accounts instead of hardcoded access keys.

**How would you secure S3?**  
Private bucket, least-privilege IAM policy, server-side encryption, object key structure scoped by contest/user/submission, no public read, and audit logs if required.

## Kubernetes

**Explain Kubernetes in your project.**  
The backend was containerized with Docker, then deployed through Kubernetes manifests kept in a separate infra repo. The basic deployment model was a Deployment for backend pods, a Service for stable networking, ConfigMaps/Secrets for configuration, health checks for readiness/liveness, and resource requests/limits. Kubernetes gave rolling updates, self-healing, and scaling.

**What happens if a pod crashes?**  
The kubelet/container runtime restarts it based on the pod restart policy, and the Deployment/ReplicaSet keeps the desired replica count.

**Readiness vs liveness?**  
Readiness decides whether the pod should receive traffic. Liveness decides whether Kubernetes should restart the container.

**How do rolling updates work?**  
Kubernetes creates pods with the new image while gradually terminating old pods, respecting availability constraints. If the rollout fails, you can roll back to the previous ReplicaSet.

**How would you scale Seaweed?**  
Scale API pods horizontally, separate judge workers from API pods, use a durable queue, autoscale workers on queue depth, use RDS/managed Postgres, and cache leaderboard reads.

## Google Cloud Run

**Explain Cloud Run.**  
Cloud Run runs containers serverlessly. You push/build a Docker image, deploy it as a service, configure env vars/secrets, and Cloud Run handles HTTPS, autoscaling, and revisions.

**Why Cloud Run for Bentham?**  
The service was containerized and request-driven, so Cloud Run was faster to operate than managing Kubernetes. It gave revisions, traffic shifting, and easy rollback.

**Cloud Run vs Kubernetes?**  
Cloud Run is simpler and serverless, good for APIs/webhooks/background-ish request services. Kubernetes gives deeper control over networking, scheduling, sidecars, multiple services, custom autoscaling, and long-running workloads.

## GitHub Actions

**Explain your automation.**  
I used GitHub Actions to make CI/CD repeatable. A typical workflow checks out code, sets up the language runtime, installs dependencies, runs tests/lint/build, builds a Docker image if needed, authenticates to the cloud provider using GitHub Secrets, and deploys only after checks pass.

**What did Seaweed's workflow do?**  
It ran on pull requests and pushes to main. Backend job used Go, then ran `go build`, `go vet`, and `go test`. Frontend job used Node 20, ran `npm ci`, lint, and build.

**How were secrets handled?**  
Through GitHub Secrets or cloud identity, not committed to the repo. Examples: cloud credentials, registry tokens, API keys, database URLs, and deploy tokens.

**How would rollback work?**  
For Cloud Run, route traffic back to a previous revision or redeploy the previous image tag. For Kubernetes, use `kubectl rollout undo` or deploy the previous image tag.

## Technical Skills Rapid Answers

**Go**  
I used Go for backend services where concurrency, simple deployment, and strong standard library support mattered. In Postificus and Seaweed, Go handled APIs, workers, database access, S3, RabbitMQ, and Judge0 integration.

**Python/FastAPI**  
I used Python/FastAPI in Murdoc because security/AI tooling had Python-native libraries like Presidio, policy/testing utilities, and easier integration with AI/MCP experiments.

**PostgreSQL**  
I used it for relational state: users, contests, submissions, drafts, credentials, rankings. Transactions matter for verdict application and ranking updates.

**Redis**  
Used for short-lived state like cache, autosave, rate-limit counters, and runtime state. It should not be the only durable source of truth.

**RabbitMQ**  
Used for durable async jobs, retries, manual ack/nack, and DLQs around external browser/API workflows.

**Prometheus/OpenTelemetry**  
Prometheus gives metrics like request counts, latency, publish outcomes, worker jobs, and security decisions. OpenTelemetry gives traces across request flow and security layers.

## Likely Interview Questions

**1. Tell me about your strongest project.**  
Murdoc is my strongest for CloudSEK because it is security-focused. It acts as an enforcement gateway for AI/tool traffic, applies prompt-injection checks, PII redaction, policy decisions, and audit logging before downstream execution.

**2. Why should we believe the numbers on your resume?**  
The percentages are based on before/after measurements in the workflow. For example, Bentham's manual filing workflow had repeated human steps; automation reduced that manual time significantly. Murdoc's prevention rate came from an attack corpus. I can explain the measurement setup and limitations.

**3. Tell me about a failure you handled.**  
Postificus is a good example. External publishing/browser workflows fail often, so I added retries, DLQs, circuit breakers, and metrics instead of letting one platform failure cascade through the worker system.

**4. Difference between Docker and Kubernetes?**  
Docker packages and runs a container. Kubernetes orchestrates many containers: scheduling, service discovery, health checks, scaling, rolling updates, and self-healing.

**5. Difference between Kubernetes and Cloud Run?**  
Cloud Run is managed serverless container hosting with less operational overhead. Kubernetes is more flexible but requires managing cluster-level concerns.

**6. What happens when a request enters Postificus?**  
The API validates and stores state, publishes a job to RabbitMQ, worker consumes it, fetches credentials, executes API/browser automation, updates metrics/status, and ack/retries/DLQs based on outcome.

**7. What happens when a submission enters Seaweed?**  
Validate user/contest/problem, upload code to S3, insert pending submission, run Judge0 asynchronously, store test-case results, update submission status, update rankings transactionally.

**8. What happens when a request enters Murdoc?**  
Normalize request, load route profile, scan for prompt injection, scan/redact PII, evaluate policy, optionally run semantic guardrails, call downstream only if allowed, inspect output, then write a decision/audit record.

**9. How did you monitor systems?**  
Prometheus metrics for latency, request counts, worker job duration, circuit breaker state, security decisions, and policy outcomes. Murdoc also used OpenTelemetry for traces and structured security events.

**10. How did you handle secrets?**  
No secrets in code. Use environment variables, GitHub Secrets for CI, cloud secret manager or platform secrets in deployment, and IAM/service-account based access where possible.

**11. What would you improve in your projects now?**  
Seaweed: durable queue and worker autoscaling. Postificus: stronger idempotency and replay tooling for DLQ jobs. Murdoc: more real-provider evaluation and policy regression tests. Bentham: deeper workflow observability and structured run history.

**12. Why CloudSEK?**  
CloudSEK is security-oriented, and my strongest overlap is building backend systems that need reliability, observability, and security enforcement: Murdoc for AI security gateway patterns, Postificus for resilient async workflows, and open-source security fixes.

## LeetCode Evaluation Strategy

Use this script in the coding round:

1. Restate the problem and constraints.
2. Give brute force briefly.
3. Identify pattern: hash map, two pointers, sliding window, stack, BFS/DFS, heap, DP.
4. Code the clean solution.
5. Dry run with sample and edge cases.
6. State time and space complexity.

High-priority problems for this interview:

- Two Sum
- Roman to Integer
- Valid Parentheses
- Valid Anagram
- Best Time to Buy and Sell Stock
- Longest Substring Without Repeating Characters
- Move Zeroes
- Merge Sorted Array
- Group Anagrams
- First Unique Character in a String

