# NeoSapien Backend Internship Answers

## Have you built anything using AI APIs or AI-assisted workflows?

Yes. The best example is `Swish Support System`, an AI-assisted support backend for food-delivery complaints.

I built the Python/FastAPI agent service, the LLM-based complaint assessment flow, conversation state handling, and Langfuse/local tracing. The LLM was used to understand messy customer messages: issue type, intent, severity, ambiguity, and whether photo evidence was useful. The actual refund/replacement/escalation decision stayed deterministic in code.

The hard part was keeping the AI useful without letting it become the source of truth. I learned that AI workflows need strong backend boundaries: structured context, fallbacks, traceability, tests, and policy logic outside the model.

## Describe the most technically complex backend project you have built or contributed to.

The most technically complex backend project I built was `Seaweed`, a contest platform for registrations, code submissions, judging, scoring, and live rankings.

The backend used Go services, PostgreSQL for users/submissions/results, Redis for runtime contest state and leaderboard-style reads, Judge0 for sandboxed code execution, Docker, Kubernetes, and AWS deployment. My main contribution was designing the submission flow: accepting code, dispatching it asynchronously to Judge0, storing verdicts, updating scores, and keeping rankings responsive during contests.

The hard part was handling many moving pieces at once: user registration, submissions, async judging, verdict polling, score calculation, ranking updates, and failure cases when the judge or network was slow. I learned a lot about designing backend flows where correctness and latency both matter.

## Share one project, repo, demo, or write-up you are most proud of.

My Google Summer of Code project with Invesalius is the work I am most proud of.

I worked on Python-based medical image segmentation tooling for brain MRI workflows. The project involved model inference, preprocessing, orientation correction, generated mask handling, and integration into an existing mature open-source application. I also worked on runtime optimization, reducing segmentation time significantly while keeping outputs inspectable for users.

I am proud of it because it was real open-source work with review constraints, compatibility concerns, and a domain where correctness matters. It taught me how to contribute carefully to an existing codebase instead of only building isolated projects from scratch.

## Why do you want to work with us in this backend internship role?

NeoSapien’s product is interesting to me because conversation memory is a backend-heavy AI problem. Capturing conversations is only the first step; the harder part is turning them into structured, retrievable, useful memory over time.

That matches the kind of work I want to do: async processing, APIs, context management, storage, retrieval, and debugging AI workflows. I have built smaller versions of these ideas in my own projects, and I want to learn how they are built properly in a real product with real users.

## What kind of engineering problems do you enjoy most?

I enjoy problems where I have to build the solution from the ground up and make real design choices along the way.

I like figuring out what the architecture should look like, where state should live, what should be synchronous vs async, which database or queue fits the problem, and how to keep the system debuggable later. I enjoy the process of comparing options, testing assumptions, and gradually arriving at a solution that is simple enough to maintain but strong enough for real use.

## Tell us about a time you debugged a difficult technical issue.

During my GSoC project with Invesalius, I had to debug issues in the brain-subpart segmentation pipeline where the generated masks were not always lining up correctly with the loaded MRI volume.

The difficult part was that the bug could come from many places: image conformation, orientation handling, plane-wise preprocessing, PyTorch vs ONNX/Tinygrad inference, label mapping, or the final binary mask generation. I debugged it by breaking the pipeline into stages, saving/checking intermediate outputs, comparing label IDs, and verifying that the generated masks matched the expected anatomical regions before they were shown in the UI.

The main lesson was to debug complex pipelines step by step instead of guessing at the final output. Once each stage was inspectable, it became much easier to find where the mismatch was introduced.

## What are you hoping to learn during this internship?

I want to learn how production AI backends are built at real usage scale.

For NeoSapien specifically, I would like to learn more about async Python/FastAPI, event-driven architecture, conversation data pipelines, database design for memory/context, production debugging, and observability. I also want to learn how a small team decides what to build quickly without making the backend fragile.

## How did you hear about this role?

LinkedIn

## If referral, who referred you?

N/A

## Anything else you want us to know?

I am not just looking to add "AI" to projects. I am interested in the backend systems that make AI products reliable: context, memory, queues, traces, evals, and failure handling.

I also use AI tools in a practical way. I use them to think through design options, tradeoffs, failure modes, and debugging paths, but I still make the final decisions by reading the code, testing, and checking system behavior.
