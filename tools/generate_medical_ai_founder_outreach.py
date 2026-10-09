from __future__ import annotations

import subprocess
from pathlib import Path

try:
    from tools.generate_first8_startup_applications import (
        BENTHAM_BACKEND,
        P,
        PREAMBLE,
        ResumeConfig,
        SKILLS,
        education,
        heading,
        experience,
        projects,
        skills,
    )
except ModuleNotFoundError:
    from generate_first8_startup_applications import (
        BENTHAM_BACKEND,
        P,
        PREAMBLE,
        ResumeConfig,
        SKILLS,
        education,
        heading,
        experience,
        projects,
        skills,
    )


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "tailored_resumes" / "medical_ai_founder_outreach_2026_07_14"

# Medical AI resumes use slightly larger body text so the dense technical work
# remains readable when reviewed quickly.
MEDICAL_PREAMBLE = (
    PREAMBLE
    .replace(r"\fontsize{9.7pt}{10.25pt}", r"\fontsize{10.2pt}{11.5pt}")
    .replace("itemsep=0.7pt,topsep=1.4pt", "itemsep=1.0pt,topsep=2.0pt")
    .replace("\\vspace{-0.6pt}", "\\vspace{-0.1pt}")
    .replace("\\addtolength{\\topmargin}{-.94in}", "\\addtolength{\\topmargin}{-.72in}")
    .replace("\\vspace{-4pt}\\scshape", "\\vspace{-2pt}\\scshape")
    .replace("\\titlerule \\vspace{-5pt}", "\\titlerule \\vspace{-3pt}")
)


GSOC_MEDICAL = (
    r"Worked across InVesalius, an open-source \textbf{3D medical-imaging and neuronavigation application}, integrating FastSurfer CNN inference for \textbf{95 anatomical brain regions} with PyTorch/TorchScript and ONNX/TinyGrad paths.",
    r"Handled \textbf{DICOM and volumetric MRI workflows} alongside NIfTI/MGZ data, including voxel conformation, orientation-sensitive preprocessing, plane-specific models, label remapping, LUT mapping, generated masks, and 3D surface inspection.",
    r"Debugged \textbf{model-output orientation, label correctness, GPU/CPU paths, progress reporting, and 3D inspection} so segmentation results remained consistent across inference paths.",
    r"Studied model architecture and runtime behavior while converting/integrating inference paths, then reduced processing time by \textbf{87\%} through async/parallel execution with GPU/CPU, output-correctness, and QC checks.",
)


GSOC_MEDICAL_COMPACT = (
    r"Worked across InVesalius, an open-source \textbf{3D medical-imaging and neuronavigation application}, integrating FastSurfer CNN inference for \textbf{95 anatomical brain regions} with PyTorch/TorchScript and ONNX/TinyGrad paths.",
    r"Handled \textbf{DICOM and volumetric MRI workflows}, NIfTI/MGZ preprocessing, voxel conformation, orientation-sensitive label mapping, generated masks, and 3D surface inspection.",
    r"Debugged \textbf{orientation, label correctness, GPU/CPU paths, and output inspection} while keeping results consistent across model runtimes.",
    r"Studied model architecture and runtime behavior during conversion/integration and reduced processing time by \textbf{87\%} with async/parallel execution while preserving output correctness and QC.",
)


BENTHAM_MEDICAL = (
    r"Designed and built a resilient \textbf{Node.js/Puppeteer workflow engine} for MCA company-registration filings, turning browser-driven steps into repeatable backend operations.",
    r"Integrated \textbf{public-site API lookups}, retries, session recovery, and operator checkpoints so partially completed workflows could resume instead of restarting, reducing manual filing time by \textbf{85\%}.",
    r"Implemented an \textbf{AI-assisted drafting flow} for company-name suggestions, object descriptions, and filing fields, with inspectable outputs and deterministic validation before execution.",
    r"Containerized backend services with \textbf{Docker}, deployed them on \textbf{Google Cloud Run}, and automated releases with \textbf{GitHub Actions}, improving deployment velocity by \textbf{70\%}.",
)


OSS_MEDICAL = (
    r"Contributed maintainer-reviewed patches to \textbf{Invesalius} around medical-imaging artifact correctness and parser safety, with additional work in scientific data codebases.",
    r"Also contributed to \textbf{Kuadrant MCP Gateway, Kyverno, Tiled, CRIU, IOOS, and VideoLAN}, covering backend failover behavior, security validation, data and parser correctness, and compatibility fixes.",
)

OSS_IMAGING = (
    r"Contributed maintainer-reviewed patches to \textbf{Invesalius} around medical-imaging artifact correctness and parser safety, with additional work in scientific data codebases.",
)

OSS_DATA = (
    r"Contributed maintainer-reviewed patches across \textbf{Invesalius, Tiled, and IOOS}, working on medical/scientific data correctness, parser safety, and compatibility.",
)


CONFIGS = {
    "BioStack": ResumeConfig(
        "Healthcare AI data / ML infrastructure intern",
        BENTHAM_MEDICAL,
        GSOC_MEDICAL,
        OSS_MEDICAL,
        ("hyoka_agent", "swish_agent"),
        SKILLS["health"],
    ),
    "Lattice Health": ResumeConfig(
        "Medical AI reliability / platform intern",
        BENTHAM_MEDICAL,
        GSOC_MEDICAL_COMPACT,
        OSS_MEDICAL,
        ("hyoka_health", "postificus_backend"),
        SKILLS["health"],
    ),
    "a2z Radiology AI": ResumeConfig(
        "Medical imaging ML / inference engineering intern",
        BENTHAM_MEDICAL,
        GSOC_MEDICAL,
        OSS_MEDICAL,
        ("hyoka_agent", "postificus_backend"),
        SKILLS["health"],
    ),
    "Promaxo": ResumeConfig(
        "Medical imaging / AI platform intern",
        BENTHAM_MEDICAL,
        GSOC_MEDICAL,
        OSS_MEDICAL,
        ("hyoka_health", "postificus_backend"),
        SKILLS["health"],
    ),
    "nView Medical": ResumeConfig(
        "Medical imaging / neuronavigation engineering intern",
        BENTHAM_MEDICAL,
        GSOC_MEDICAL,
        OSS_MEDICAL,
        ("hyoka_health", "postificus_backend"),
        SKILLS["health"],
    ),
}


CONTACTS = {
    "BioStack": {
        "emails": "sanat@getbiostack.com; parth@getbiostack.com",
        "confidence": "Direct founder emails publicly listed by BioStack/Y Combinator.",
        "source": "https://www.ycombinator.com/companies/biostack-platforms",
    },
    "Lattice Health": {
        "emails": "christine@latticehealthai.com",
        "confidence": "Founder email publicly listed on Lattice Health's YC launch page.",
        "source": "https://www.ycombinator.com/companies/lattice-health",
    },
    "a2z Radiology AI": {
        "emails": "pilot@a2zradiology.ai",
        "confidence": "Public company/demo contact; no verified direct founder email found.",
        "source": "https://www.a2zradiology.ai/company/",
    },
    "Promaxo": {
        "emails": "avohra@promaxo.com",
        "confidence": "Publicly listed business email for Amit Vohra.",
        "source": "https://www.allbiz.com/business/promaxo_1e-510-982-1202",
    },
    "nView Medical": {
        "emails": "cristian.atria@nviewmed.com",
        "confidence": "Publicly listed founder/CEO email in SBIR and NCI records.",
        "source": "https://www.sbir.gov/awards/147755",
    },
}


MAILS = {
    "BioStack": {
        "subject": "Engineering internship in medical imaging and AI data systems",
        "body": """Hi Sanat and Parth,

I was looking through YC's startup directory and came across BioStack. The idea of turning messy clinical and imaging data into useful training environments immediately felt close to my own work, so I thought I would reach out.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked with DICOM and volumetric MRI data in a three dimensional medical imaging and neuronavigation application. I integrated FastSurfer inference for 95 brain regions across PyTorch and ONNX, handled orientation sensitive preprocessing and generated masks, and reduced processing time by 87 percent.

• More recently, I built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, quality gates, and audit logs. It has given me a stronger understanding of how AI outputs can be made reproducible and useful for real workflows.

• Apart from this, I worked at Bentham AI, https://www.bentham.legal/, a legal automation startup, where I built backend automation for compliance workflows involving external APIs, browser execution, retries, and session recovery.

I think this combination of medical imaging, AI reliability, and backend workflow experience could be useful for BioStack's work. I would love to chat if there is an opportunity to contribute through an internship in medical data, ML infrastructure, evaluation, or backend engineering.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic/hyoka
""",
    },
    "Lattice Health": {
        "subject": "Internship inquiry in medical AI reliability and platform engineering",
        "body": """Hi Christine,

I was scrolling through YC's startup directory and came across Lattice Health. I have some experience in this field but have not had much chance to work in it since my Google Summer of Code project with Invesalius, so naturally it caught my attention. I would love to contribute as an engineer if you are open to bringing someone on.

A little bit about me that might be relevant:

• During GSoC with Invesalius, a software used in over 144 countries, I worked with DICOM and MRI data, orientation and label correctness, PyTorch and ONNX inference, generated masks, and three dimensional inspection in a neuronavigation application. I reduced processing time by 87 percent while preserving output checks.

• More recently, I built Hyoka, an AI Reliability and Evaluation Platform that tracks trace ingestion, evaluations, replayable runs, artifacts, quality gates, and self-improvement workflows for AI agents. While it is aimed at agentic AI rather than medical imaging, building it gave me a deeper understanding of model drift, evaluation pipelines, and production monitoring, which seem closely aligned with what Lattice is solving.

• Apart from these, I worked previously at Bentham AI, https://www.bentham.legal/, a legal automation startup, where I worked on automating legal workflows while considering compliance.

While my previous work was not specifically focused on monitoring deployed medical imaging models, my experience with medical imaging and AI reliability has given me a solid understanding of model drift and evaluation. It is a niche that genuinely interests me, and I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic/hyoka
""",
    },
    "a2z Radiology AI": {
        "subject": "Internship inquiry in medical imaging ML engineering",
        "body": """Hi Samir and Pranav,

I came across a2z while reading your launch story about building an AI safety net for radiologists. The focus on making medical imaging AI reliable and useful in clinical workflows caught my attention, so I thought I would reach out.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked with DICOM and volumetric MRI workflows in a three dimensional medical imaging and neuronavigation application. I integrated FastSurfer inference for 95 brain regions across PyTorch and ONNX, debugged orientation and label correctness, and built generated mask and three dimensional inspection flows.

• I also reduced processing time by 87 percent through asynchronous and parallel execution, while checking GPU and CPU paths and preserving output correctness.

• I have also built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, and quality gates. Before that, I worked at Bentham AI, https://www.bentham.legal/, on backend automation for legal and compliance workflows.

The modality and clinical task are different from a2z, but I believe my experience with inference integration, imaging data conformation, output validation, and performance work could transfer well to imaging ML engineering. I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic/hyoka
""",
    },
    "Promaxo": {
        "subject": "Internship inquiry in MRI and medical AI engineering",
        "body": """Hi Dr. Vohra,

I was reading about Promaxo's point of care MRI and image guided procedures and came across the work your team is doing. The combination of imaging, planning, and intervention is closely related to the kind of work I want to pursue.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked with DICOM and MRI workflows, orientation and voxel conformation in a three dimensional medical imaging and neuronavigation application. I integrated FastSurfer segmentation for 95 brain regions through PyTorch and ONNX model paths.

• I also built generated mask and three dimensional inspection workflows, and reduced processing time by 87 percent through asynchronous and parallel execution while preserving output checks.

• More recently, I built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, and quality gates. I have also worked on backend automation and recovery workflows at Bentham AI, https://www.bentham.legal/.

I have not worked on prostate intervention, robotics, or regulated device development, but I think my experience with medical imaging software, model integration, and reliable backend workflows could be useful to Promaxo. I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic/hyoka
""",
    },
    "nView Medical": {
        "subject": "Internship inquiry in three dimensional imaging and neuronavigation engineering",
        "body": """Hi Cristian,

I was looking at companies building intraoperative imaging and navigation and came across nView. After reading about the nView s1, the connection with my own project work felt worth reaching out about.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked in a three dimensional medical imaging and neuronavigation application with DICOM and volumetric MRI data. I integrated FastSurfer inference for 95 brain regions through PyTorch and ONNX conversion and integration.

• I worked on generated masks, label mapping, three dimensional surface inspection, and reduced processing time by 87 percent through asynchronous and parallel execution.

• I have also built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, and quality gates. Before that, I worked at Bentham AI, https://www.bentham.legal/, on backend automation involving external systems, retries, and recovery.

I have not worked on C arm reconstruction or surgical device engineering, but I think my experience with imaging software, neuronavigation adjacent workflows, AI model integration, and backend reliability could be useful to nView. I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic/hyoka
""",
    },
}


def resume_tex(config: ResumeConfig) -> str:
    return "\n".join([
        MEDICAL_PREAMBLE,
        heading(),
        education(),
        experience(config),
        projects(config),
        skills(config),
        r"\end{document}",
    ])


def compile_pdf(tex_path: Path) -> None:
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
        cwd=tex_path.parent,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )


def write_bundle() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = [
        "# Medical AI Founder Outreach",
        "",
        "Prepared 14 July 2026. The resumes use the Cent Health structure, with the GSoC scope expanded to include InVesalius medical imaging, neuronavigation, DICOM/volumetric data, model conversion, ONNX inference, and output validation.",
        "",
        "## Contact list",
        "",
        "| Company | Contact email | Verification | Source |",
        "|---|---|---|---|",
    ]
    for company, contact in CONTACTS.items():
        rows.append(f"| {company} | `{contact['emails']}` | {contact['confidence']} | [source]({contact['source']}) |")

    rows.extend([
        "",
        "## Tailoring decisions",
        "",
        "| Company | Discovery source used in email | Resume emphasis | Selected supporting work |",
        "|---|---|---|---|",
        "| BioStack | [Y Combinator company profile](https://www.ycombinator.com/companies/biostack-platforms) | Imaging data correctness, ML-ready workflows, reproducibility | GSoC medical imaging, Hyoka, Swish |",
        "| Lattice Health | [Y Combinator launch post](https://www.ycombinator.com/companies/lattice-health) | Model-output correctness, evaluation, observability, auditability | GSoC medical imaging, Hyoka, Postificus |",
        "| a2z Radiology AI | [a2z launch story](https://a2zradiology.ai/news/a2z-emerges-from-stealth/) | Inference integration, image conformation, validation, performance | GSoC medical imaging, Hyoka, Postificus |",
        "| Promaxo | [Promaxo product page](https://www.promaxo.com/) | Volumetric MRI, anatomy-aware inference, 3D inspection, platform engineering | GSoC medical imaging, Hyoka, Postificus |",
        "| nView Medical | [nView product page](https://www.nviewmed.com/products) | 3D imaging, neuronavigation-adjacent workflows, anatomy and visualization | GSoC medical imaging, Hyoka, Postificus |",
        "",
        "## Resume and email bundles",
        "",
    ])
    for company, config in CONFIGS.items():
        slug = company.lower().replace(" ", "_").replace("/", "_")
        tex_path = OUT_DIR / f"{slug}_resume.tex"
        pdf_path = OUT_DIR / f"{slug}_resume.pdf"
        mail_path = OUT_DIR / f"{slug}_email.txt"
        tex_path.write_text(resume_tex(config), encoding="utf-8")
        compile_pdf(tex_path)
        mail_path.write_text(
            f"To: {CONTACTS[company]['emails']}\nSubject: {MAILS[company]['subject']}\n\n{MAILS[company]['body'].strip()}\n",
            encoding="utf-8",
        )
        rows.extend([
            f"### {company}",
            "",
            f"Resume: [{pdf_path.name}]({pdf_path})",
            f"Email: [{mail_path.name}]({mail_path})",
            "",
            f"**Subject:** {MAILS[company]['subject']}",
            "",
            MAILS[company]["body"].strip(),
            "",
        ])

    rows.extend([
        "## Positioning guardrails",
        "",
        "The GSoC work demonstrates medical-imaging software integration, model inference, spatial/data handling, neuronavigation-adjacent workflows, and performance engineering. It does not by itself demonstrate clinical validation, FDA submission work, hospital deployment, DICOM/PACS integration, patient-data governance, surgical robotics, or training a diagnostic model from scratch.",
        "",
        "Bentham is linked as https://www.bentham.legal/ in the email drafts wherever that experience is mentioned. The emails are plain text and do not include a phone number.",
        "",
    ])
    (OUT_DIR / "medical_ai_founder_outreach.md").write_text("\n".join(rows), encoding="utf-8")


if __name__ == "__main__":
    write_bundle()
    print(OUT_DIR)
