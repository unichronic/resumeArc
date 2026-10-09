# Medical AI Founder Outreach

Prepared 14 July 2026. The resumes use the Cent Health structure, with the GSoC scope expanded to include InVesalius medical imaging, neuronavigation, DICOM/volumetric data, model conversion, ONNX inference, and output validation.

## Contact list

| Company | Contact email | Verification | Source |
|---|---|---|---|
| BioStack | `sanat@getbiostack.com; parth@getbiostack.com` | Direct founder emails publicly listed by BioStack/Y Combinator. | [source](https://www.ycombinator.com/companies/biostack-platforms) |
| Lattice Health | `christine@latticehealthai.com` | Founder email publicly listed on Lattice Health's YC launch page. | [source](https://www.ycombinator.com/companies/lattice-health) |
| a2z Radiology AI | `pilot@a2zradiology.ai` | Public company/demo contact; no verified direct founder email found. | [source](https://www.a2zradiology.ai/company/) |
| Promaxo | `avohra@promaxo.com` | Publicly listed business email for Amit Vohra. | [source](https://www.allbiz.com/business/promaxo_1e-510-982-1202) |
| nView Medical | `cristian.atria@nviewmed.com` | Publicly listed founder/CEO email in SBIR and NCI records. | [source](https://www.sbir.gov/awards/147755) |

## Tailoring decisions

| Company | Discovery source used in email | Resume emphasis | Selected supporting work |
|---|---|---|---|
| BioStack | [Y Combinator company profile](https://www.ycombinator.com/companies/biostack-platforms) | Imaging data correctness, ML-ready workflows, reproducibility | GSoC medical imaging, Hyoka, Swish |
| Lattice Health | [Y Combinator launch post](https://www.ycombinator.com/companies/lattice-health) | Model-output correctness, evaluation, observability, auditability | GSoC medical imaging, Hyoka, Postificus |
| a2z Radiology AI | [a2z launch story](https://a2zradiology.ai/news/a2z-emerges-from-stealth/) | Inference integration, image conformation, validation, performance | GSoC medical imaging, Hyoka, Postificus |
| Promaxo | [Promaxo product page](https://www.promaxo.com/) | Volumetric MRI, anatomy-aware inference, 3D inspection, platform engineering | GSoC medical imaging, Hyoka, Postificus |
| nView Medical | [nView product page](https://www.nviewmed.com/products) | 3D imaging, neuronavigation-adjacent workflows, anatomy and visualization | GSoC medical imaging, Hyoka, Postificus |

## Resume and email bundles

### BioStack

Resume: [biostack_resume.pdf](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/biostack_resume.pdf)
Email: [biostack_email.txt](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/biostack_email.txt)

**Subject:** Engineering internship in medical imaging and AI data systems

Hi Team,

I was looking through YC's startup directory and came across BioStack. The idea of turning messy clinical and imaging data into useful training environments immediately felt close to my own work, so I thought I would reach out.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked with DICOM and volumetric MRI data in a three dimensional medical imaging and neuronavigation application. I integrated FastSurfer inference for 95 brain regions across PyTorch and ONNX, handled orientation sensitive preprocessing and generated masks, and reduced processing time by 87 percent.

• More recently, I built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, quality gates, and audit logs. It has given me a stronger understanding of how AI outputs can be made reproducible and useful for real workflows.

• Apart from this, I worked at Bentham AI, https://www.bentham.legal/, a legal automation startup, where I built backend automation for compliance workflows involving external APIs, browser execution, retries, and session recovery.

I think this combination of medical imaging, AI reliability, and backend workflow experience could be useful for BioStack's work. I would love to chat if there is an opportunity to contribute through an internship in medical data, ML infrastructure, evaluation, or backend engineering.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic

### Lattice Health

Resume: [lattice_health_resume.pdf](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/lattice_health_resume.pdf)
Email: [lattice_health_email.txt](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/lattice_health_email.txt)

**Subject:** Internship inquiry in medical AI reliability and platform engineering

Hi Christine,

I was scrolling through YC's startup directory and came across Lattice Health. I have some experience in this field but have not had much chance to work in it since my Google Summer of Code project with Invesalius, so naturally it caught my attention. I would love to contribute as an engineer if you are open to bringing someone on.

A little bit about me that might be relevant:

• During GSoC with Invesalius, a software used in over 144 countries, I worked with DICOM and MRI data, orientation and label correctness, PyTorch and ONNX inference, generated masks, and three dimensional inspection in a neuronavigation application. I reduced processing time by 87 percent while preserving output checks.

• More recently, I built Hyoka, an AI Reliability and Evaluation Platform that tracks trace ingestion, evaluations, replayable runs, artifacts, quality gates, and self-improvement workflows for AI agents. While it is aimed at agentic AI rather than medical imaging, building it gave me a deeper understanding of model drift, evaluation pipelines, and production monitoring, which seem closely aligned with what Lattice is solving.

• Apart from these, I worked previously at Bentham AI, https://www.bentham.legal/, a legal automation startup, where I worked on automating legal workflows while considering compliance.

While my previous work was not specifically focused on monitoring deployed medical imaging models, my experience with medical imaging and AI reliability has given me a solid understanding of model drift and evaluation. It is a niche that genuinely interests me, and I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic

### a2z Radiology AI

Resume: [a2z_radiology_ai_resume.pdf](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/a2z_radiology_ai_resume.pdf)
Email: [a2z_radiology_ai_email.txt](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/a2z_radiology_ai_email.txt)

**Subject:** Internship inquiry in medical imaging ML engineering

Hi Samir and Pranav,

I came across a2z while reading your launch story about building an AI safety net for radiologists. The focus on making medical imaging AI reliable and useful in clinical workflows caught my attention, so I thought I would reach out.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked with DICOM and volumetric MRI workflows in a three dimensional medical imaging and neuronavigation application. I integrated FastSurfer inference for 95 brain regions across PyTorch and ONNX, debugged orientation and label correctness, and built generated mask and three dimensional inspection flows.

• I also reduced processing time by 87 percent through asynchronous and parallel execution, while checking GPU and CPU paths and preserving output correctness.

• I have also built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, and quality gates. Before that, I worked at Bentham AI, https://www.bentham.legal/, on backend automation for legal and compliance workflows.

The modality and clinical task are different from a2z, but I believe my experience with inference integration, imaging data conformation, output validation, and performance work could transfer well to imaging ML engineering. I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic

### Promaxo

Resume: [promaxo_resume.pdf](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/promaxo_resume.pdf)
Email: [promaxo_email.txt](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/promaxo_email.txt)

**Subject:** Internship inquiry in MRI and medical AI engineering

Hi Dr. Vohra,

I was reading about Promaxo's point of care MRI and image guided procedures and came across the work your team is doing. The combination of imaging, planning, and intervention is closely related to the kind of work I want to pursue.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked with DICOM and MRI workflows, orientation and voxel conformation in a three dimensional medical imaging and neuronavigation application. I integrated FastSurfer segmentation for 95 brain regions through PyTorch and ONNX model paths.

• I also built generated mask and three dimensional inspection workflows, and reduced processing time by 87 percent through asynchronous and parallel execution while preserving output checks.

• More recently, I built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, and quality gates. I have also worked on backend automation and recovery workflows at Bentham AI, https://www.bentham.legal/.

I have not worked on prostate intervention, robotics, or regulated device development, but I think my experience with medical imaging software, model integration, and reliable backend workflows could be useful to Promaxo. I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic

### nView Medical

Resume: [nview_medical_resume.pdf](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/nview_medical_resume.pdf)
Email: [nview_medical_email.txt](/home/unichronic/intern/tailored_resumes/medical_ai_founder_outreach_2026_07_14/nview_medical_email.txt)

**Subject:** Internship inquiry in three dimensional imaging and neuronavigation engineering

Hi Cristian,

I was looking at companies building intraoperative imaging and navigation and came across nView. After reading about the nView s1, the connection with my own project work felt worth reaching out about.

A little bit about me that might be relevant:

• During GSoC with InVesalius, I worked in a three dimensional medical imaging and neuronavigation application with DICOM and volumetric MRI data. I integrated FastSurfer inference for 95 brain regions through PyTorch and ONNX conversion and integration.

• I worked on generated masks, label mapping, three dimensional surface inspection, and reduced processing time by 87 percent through asynchronous and parallel execution.

• I have also built Hyoka, an AI reliability and evaluation platform for trace ingestion, evaluations, replayable runs, artifacts, and quality gates. Before that, I worked at Bentham AI, https://www.bentham.legal/, on backend automation involving external systems, retries, and recovery.

I have not worked on C arm reconstruction or surgical device engineering, but I think my experience with imaging software, neuronavigation adjacent workflows, AI model integration, and backend reliability could be useful to nView. I would love to chat if there is an opportunity to contribute.

I've attached my resume below.

Regards,
Shuvam
https://github.com/unichronic

## Positioning guardrails

The GSoC work demonstrates medical-imaging software integration, model inference, spatial/data handling, neuronavigation-adjacent workflows, and performance engineering. It does not by itself demonstrate clinical validation, FDA submission work, hospital deployment, DICOM/PACS integration, patient-data governance, surgical robotics, or training a diagnostic model from scratch.

Bentham is linked as https://www.bentham.legal/ in the email drafts wherever that experience is mentioned. The emails are plain text and do not include a phone number.
