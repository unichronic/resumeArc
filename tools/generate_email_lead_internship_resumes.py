from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

import generate_next_internship_resumes as next_batch
import generate_selected_internship_resumes as base


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "email_leads_2026_05_25"


@dataclass(frozen=True)
class Resume:
    slug: str
    company: str
    role: str
    focus: str
    experience_profile: str
    open_source_profile: str
    project_keys: tuple[str, str, str]
    skills: str
    source: str
    note: str


PROJECTS = dict(base.PROJECTS)
PROJECTS.update(next_batch.PROJECTS)
PROJECTS.update(
    {
        "omni_voice_agent": base.Project(
            "Omni-SSM Voice Agent",
            "Python, PyTorch, ONNX Runtime, Sherpa-ONNX, Moonshine, Hindi ASR, Piper",
            "",
            (
                r"Built a local \textbf{voice-agent research loop} combining STT/TTS experiments, SSAMBA streaming CTC, Piper low-latency TTS, optional Qwen3-TTS output, and WebRTC-style loopback benchmarks.",
                r"Worked on Moonshine Hindi ASR tuning with manifest-driven dataset loading, teacher/student distillation, partial fine-tuning scripts, and WER, first-audio latency, memory, and provider-profile checks.",
            ),
        ),
        "hyoka_regulated_eval": base.Project(
            "Hyoka",
            "Python, FastAPI, PostgreSQL, OpenTelemetry, SQLAlchemy, Typer, Docker",
            "",
            (
                r"Built AI-agent evaluation infrastructure with trace ingestion, evaluator registries, replay modes, failure mining, validation runs, gate decisions, promotions, audit logs, and signed manifests.",
                r"Designed reproducible runs around immutable inputs, content-addressed artifacts, project-scoped API keys, worker leases, JSON schema checks, and latency/cost constraints.",
            ),
        ),
        "penny_data_workflows": base.Project(
            "Penny Lane Capital",
            "Python, Agno, Pydantic, SQLite, Vector Memory, yfinance, JSONL",
            base.href("https://github.com/unichronic/pennylane"),
            (
                r"Built a Python multi-agent research workflow with analyst roles, bull/bear debate, trader, risk review, portfolio approval, typed state, checkpoints, and replayable JSONL traces.",
                r"Evaluated decisions with historical-market backtests, reward-loop scorecards, baseline comparisons, semantic lesson retrieval, and return/drawdown/win-rate signals.",
            ),
        ),
        "seaweed_software_delivery": base.Project(
            "Seaweed: Contest Platform",
            "TypeScript, React, Next.js, Go, PostgreSQL, Judge0, Firebase, Docker",
            base.href("https://github.com/unichronic/seaweed-fe"),
            (
                r"Built a full-stack assessment platform with auth-gated problem pages, code editor, submissions, admin review, shortlisting, live rankings, and reproducible result records.",
                r"Implemented Go judging APIs with Judge0, PostgreSQL rankings/materialized views, Redis-backed runtime state, and Docker/Kubernetes deployment for \textbf{500+ concurrent users}.",
            ),
        ),
    }
)


EXPERIENCE = {
    "renate": {
        "bentham": (
            r"Shipped production automation in a small team, connecting Node.js services, Puppeteer browser workflows, operator validation, API lookups, Docker, Cloud Run, and GitHub Actions.",
            r"Built failure-aware execution with retries, session recovery, and state validation, reducing manual filing time by \textbf{85\%}.",
            r"Worked on AI-assisted structured drafts that were validated before downstream automation, keeping generated outputs inspectable instead of prompt-only.",
        ),
        "gsoc": (
            r"Built Python model-inference workflows inside a mature open-source app, integrating preprocessing, model execution, generated masks, and visual inspection paths.",
            r"Reduced processing runtime by \textbf{87\%} using async/parallel execution while preserving correctness on large MRI volumes.",
            r"Debugged PyTorch/ONNX-adjacent outputs, label mapping, data transformation, and UI integration issues across unfamiliar code quickly.",
        ),
    },
    "statsby": {
        "bentham": (
            r"Built data-backed automation flows that combined public-site API lookups, generated AI-assisted drafts, validation, retries, and operator review before execution.",
            r"Reduced manual filing time by \textbf{85\%} through backend state checks, failure recovery, and repeatable browser automation.",
            r"Deployed Dockerized services through Google Cloud Run and GitHub Actions, improving iteration speed by \textbf{70\%}.",
        ),
        "gsoc": (
            r"Built Python ML tooling for MRI segmentation across \textbf{95 anatomical regions}, covering preprocessing, inference integration, generated masks, and large-array data paths.",
            r"Reduced runtime by \textbf{87\%} using asynchronous and parallel execution over expensive NumPy/PyTorch-style workflows.",
            r"Validated model outputs through inspectable masks and 3D surfaces while debugging label mapping and data-orientation issues.",
        ),
    },
    "gallery": {
        "bentham": (
            r"Built practical AI-assisted automation that turned messy filing workflows into validated drafts, API-backed lookups, browser actions, and recoverable execution states.",
            r"Reduced manual workflow time by \textbf{85\%} by hardening multi-step public-site automation with retries and session recovery.",
            r"Packaged and deployed services with Docker, Google Cloud Run, and GitHub Actions to keep delivery repeatable.",
        ),
        "gsoc": (
            r"Built scientific Python features in an open-source medical-imaging system, connecting model inference, generated artifacts, performance-sensitive processing, and visualization.",
            r"Cut processing runtime by \textbf{87\%} with async/parallel execution over large data paths.",
            r"Worked across model output handling, UI inspection workflows, and mature-codebase constraints under mentor review.",
        ),
    },
    "peculiar": {
        "bentham": (
            r"Built Node.js/Puppeteer workflow automation with REST-style service boundaries, public-site API lookups, retries, state recovery, and operator-visible errors.",
            r"Reduced manual filing time by \textbf{85\%} and shipped Dockerized services through Cloud Run and GitHub Actions.",
            r"Improved deployment velocity by \textbf{70\%} by turning repeated setup and release steps into reproducible CI/CD paths.",
        ),
        "gsoc": (
            r"Contributed Python features inside a mature open-source desktop application with large data paths, generated artifacts, and user-facing visualization.",
            r"Reduced processing runtime by \textbf{87\%} through asynchronous and parallel execution.",
            r"Debugged integration issues across Python, NumPy, PyTorch/ONNX-adjacent outputs, and VTK/wxPython UI code.",
        ),
    },
}


OPEN_SOURCE = {
    "ai": (
        r"Contributed maintainer-reviewed patches across \textbf{Kuadrant MCP Gateway}, Kyverno, IOOS, Tiled, CRIU, and VideoLAN, with emphasis on reliability, integration behavior, parser robustness, and security-validation paths.",
    ),
    "software": (
        r"Contributed maintainer-reviewed patches across \textbf{Tiled}, Kuadrant MCP Gateway, Kyverno, IOOS, CRIU, and VideoLAN, adapting fixes to existing code style, review feedback, CI behavior, and integration constraints.",
    ),
}


SKILLS = {
    "renate": r"""\textbf{Languages}{: Python, TypeScript, JavaScript, Go, SQL} \\
   \textbf{Frameworks}{: FastAPI, React, Next.js, Node.js, PyTorch, ONNX Runtime} \\
   \textbf{Tools}{: PostgreSQL, Redis, Docker, GCP, GitHub Actions, OpenTelemetry, Langfuse, Firebase Auth, Git} \\""",
    "statsby": r"""\textbf{Languages}{: Python, TypeScript, SQL, Go} \\
   \textbf{Frameworks}{: FastAPI, PyTorch, scikit-learn, React, Next.js, Agno} \\
   \textbf{Tools}{: NumPy, pandas, PostgreSQL/pgvector, SQLite, Redis, Docker, OpenTelemetry, Langfuse, JSONL} \\""",
    "gallery": r"""\textbf{Languages}{: Python, TypeScript, Go, SQL, C++} \\
   \textbf{Frameworks}{: FastAPI, PyTorch, React, Next.js, Agno, VTK, wxPython} \\
   \textbf{Tools}{: PostgreSQL, SQLite, Redis, Vector Memory, Docker, OpenTelemetry, GitHub Actions, JSONL} \\""",
    "peculiar": r"""\textbf{Languages}{: JavaScript, TypeScript, Python, Go, SQL} \\
   \textbf{Frameworks}{: React, Next.js, Node.js, Express, FastAPI, Echo} \\
   \textbf{Tools}{: PostgreSQL, Redis, RabbitMQ, Docker, GitHub Actions, Firebase Auth, Judge0, Prometheus} \\""",
}


RESUMES = [
    Resume(
        "renate_ai_engineer_intern_resume",
        "Renate",
        "AI Engineer Intern",
        "full-stack AI, voice agents, model eval/deployment, auth/security, CI/CD, Mumbai in-office",
        "renate",
        "ai",
        ("omni_voice_agent", "hyoka_control_plane", "swish_ai_product"),
        SKILLS["renate"],
        "mailto:rishi@renate.in",
        "Best fit in this batch if Mumbai in-office/relocation is realistic. Lead with voice-agent work, Hyoka, shipped automation, and open source.",
    ),
    Resume(
        "statsby_ai_intern_resume",
        "Statsby Solutions",
        "AI Intern",
        "Python, GenAI, pandas, scikit-learn, PyTorch, regulated AI/data workflows, Pune WFO",
        "statsby",
        "ai",
        ("hyoka_regulated_eval", "penny_data_workflows", "swish_ai_product"),
        SKILLS["statsby"],
        "mailto:varnika.gupta@statsby.ai",
        "Strong AI/data fit. Public intern posting was not found, but company context strongly matches GenAI, data engineering, MLOps, and regulated production AI.",
    ),
    Resume(
        "gallery_of_code_ai_engineer_intern_resume",
        "Gallery of Code",
        "AI Engineers Internship",
        "AI R&D, applied AI systems, data/forecasting workflows, research and software engineering",
        "gallery",
        "ai",
        ("hyoka_regulated_eval", "penny_data_workflows", "seaweed_software_delivery"),
        SKILLS["gallery"],
        "mailto:info@galleryofcode.com",
        "Medium fit. Company is verified as an AI/R&D/design lab, but the exact internship post was not publicly verified.",
    ),
    Resume(
        "peculiar_technologies_software_development_intern_resume",
        "Peculiar Technologies",
        "Software Development Intern",
        "software development, React/Next.js, Node/Python/Go APIs, databases, deployment, 2-month June internship",
        "peculiar",
        "software",
        ("seaweed_software_delivery", "postificus_product", "swish_ai_product"),
        SKILLS["peculiar"],
        "mailto:peculiartechnologies18@gmail.com",
        "Use a cautious email-first approach. I could not verify the posting/company page publicly from the provided email/WhatsApp details.",
    ),
]


def render_project(key: str) -> str:
    project = PROJECTS[key]
    return rf"""
\resumeProjectHeading
{{\textbf{{{project.title}}} $|$ \emph{{{project.tech}}}}}{{{project.link}}}
\resumeItemListStart
\resumeItem{{{project.bullets[0]}}}
\resumeItem{{{project.bullets[1]}}}
\resumeItemListEnd
"""


def render_resume(resume: Resume) -> str:
    exp = EXPERIENCE[resume.experience_profile]
    open_source = OPEN_SOURCE[resume.open_source_profile][0]
    projects = "\n".join(render_project(key) for key in resume.project_keys)
    return rf"""{base.PREAMBLE}
\begin{{center}}
    {{\Huge \scshape Shuvam Pal}} \\ \vspace{{1pt}}
    \small \raisebox{{-0.1\height}}\faPhone\ +91 85830 54679 ~
    \href{{mailto:ishuvam.pal@gmail.com}}{{\raisebox{{-0.2\height}}\faEnvelope\ {{ishuvam.pal@gmail.com}}}} ~
    \href{{https://linkedin.com/in/shuvampal3960}}{{\raisebox{{-0.2\height}}\faLinkedin\ {{Shuvam Pal}}}}  ~
    \href{{https://github.com/unichronic}}{{\raisebox{{-0.2\height}}\faGithub\ {{unichronic}}}}
    \vspace{{-8pt}}
\end{{center}}

\section{{Education}}
\resumeSubHeadingListStart
  \resumeSubheading
    {{Dayananda Sagar College of Engineering}}{{Bengaluru, India}}
    {{B.E. Artificial Intelligence and Machine Learning}}{{}}
\resumeSubHeadingListEnd

\section{{Experience}}
\resumeSubHeadingListStart

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://www.bentham.legal/}}{{Bentham AI}}}} & \textit{{Dec 2025 -- Feb 2026}} \\
\textit{{Backend Engineering Intern: Node.js, JavaScript, Go, Docker, GCP, GitHub Actions}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
\resumeItem{{{exp["bentham"][0]}}}
\resumeItem{{{exp["bentham"][1]}}}
\resumeItem{{{exp["bentham"][2]}}}
\resumeItemListEnd

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{\bodyhref{{https://gist.github.com/unichronic/4d7f61048fda1312d5d30bb151ee4eb5}}{{Google Summer of Code}}}} & \textit{{May 2025 -- Sept 2025}} \\
\textit{{Mentee at Invesalius: Python, VTK, wxPython, NumPy, PyTorch, ONNX}} & \textit{{Remote}} \\
\end{{tabular*}}
\vspace{{-4pt}}
\resumeItemListStart
\resumeItem{{{exp["gsoc"][0]}}}
\resumeItem{{{exp["gsoc"][1]}}}
\resumeItem{{{exp["gsoc"][2]}}}
\resumeItemListEnd

\item
\begin{{tabular*}}{{\textwidth}}{{l@{{\extracolsep{{\fill}}}}r}}
\textbf{{Open Source}} & \bodyhref{{https://gist.github.com/unichronic/ad59b914acf303066db8239e29ebb8a6}}{{\textit{{Contributions}}}} \\
\end{{tabular*}}
\resumeItemListStart
\resumeItem{{{open_source}}}
\resumeItemListEnd

\resumeSubHeadingListEnd

\section{{Projects}}
\resumeSubHeadingListStart
{projects}
\resumeSubHeadingListEnd

\section{{Technical Skills}}
\begin{{itemize}}[leftmargin=0.15in, label={{}}]
  \small{{\item{{
   {resume.skills}
  }}}}
\end{{itemize}}

\end{{document}}
"""


def write_report() -> Path:
    rows = [
        "# Email Lead Internship Tailored Resumes",
        "",
        "Generated by `tools/generate_email_lead_internship_resumes.py`.",
        "",
        "| Company | Role | Resume PDF | Focus | Source | Note |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for resume in RESUMES:
        rows.append(
            f"| {resume.company} | {resume.role} | `{resume.slug}.pdf` | "
            f"{resume.focus} | {resume.source} | {resume.note} |"
        )
    path = OUT_DIR / "resume_fit_report.md"
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return path


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tex_paths: list[Path] = []
    for resume in RESUMES:
        path = OUT_DIR / f"{resume.slug}.tex"
        path.write_text(render_resume(resume), encoding="utf-8")
        tex_paths.append(path)

    report = write_report()
    failures: list[str] = []
    for path in tex_paths:
        result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-output-directory",
                str(OUT_DIR),
                str(path),
            ],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode != 0:
            failures.append(path.name)

    for pattern in ("*.aux", "*.log", "*.out"):
        for path in OUT_DIR.glob(pattern):
            path.unlink()

    print(f"Generated {len(tex_paths)} TeX resumes in {OUT_DIR.relative_to(ROOT)}")
    print(f"Wrote fit report to {report.relative_to(ROOT)}")
    print(f"Compiled {len(tex_paths) - len(failures)} PDFs")
    if failures:
        print("Failures:")
        for name in failures:
            print(f"  {name}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
