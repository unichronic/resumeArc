from __future__ import annotations

import importlib.util
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST8_DIR = ROOT / "tailored_resumes" / "early_startups_first8_2026_05_28"
REST_DIR = ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30"
MYJOBB_DIR = ROOT / "tailored_resumes" / "myjobb_ai_backend_2026_05_29"
OUT_DIR = ROOT / "tailored_resumes" / "early_startups_remaining_2026_05_31"
MASTER_SCRIPT = ROOT / "tailored_resumes" / "early_startups_all_gmail_drafts_2026_05_31.gs"
ATTACH_DIR = ROOT / "early_startup_all_email_attachments_2026_05_31"
NON_VIBRIUM10_SCRIPT = ROOT / "tailored_resumes" / "early_startups_non_vibrium10_gmail_drafts_2026_05_31.gs"
NON_VIBRIUM10_ATTACH_DIR = ROOT / "early_startup_non_vibrium10_email_attachments_2026_05_31"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


R = load_module("resume_builder", ROOT / "tools" / "rebuild_vibrium_onwards_resumes.py")
GMAIL = load_module("gmail_builder", ROOT / "tools" / "generate_all_startup_gmail_drafts.py")


@dataclass(frozen=True)
class ResumeSpec:
    out_dir: Path
    attachment: str
    experience: str
    gsoc: str
    projects: tuple
    skills: str


@dataclass(frozen=True)
class EmailSpec:
    slug: str
    company: str
    recipient: str
    subject: str
    attachment: str
    body: str


FIRST8_RESUMES: dict[str, ResumeSpec] = {
    "atlas": ResumeSpec(
        FIRST8_DIR,
        "atlas_intern_resume.pdf",
        "backend",
        "data",
        (R.ref("hyoka_platform"), R.ref("postificus_ops"), R.ref("swish_ops", 2)),
        R.SKILLS["ai_backend"],
    ),
    "bhindi_ai": ResumeSpec(
        FIRST8_DIR,
        "bhindi_ai_intern_resume.pdf",
        "backend",
        "default",
        (R.ref("hyoka_agent"), R.ref("postificus_ops"), R.ref("swish_ops", 2)),
        R.SKILLS["ai_backend"],
    ),
    "cent": ResumeSpec(
        FIRST8_DIR,
        "cent_intern_resume.pdf",
        "health",
        "health",
        (R.ref("hyoka_audit"), R.ref("swish_care"), R.ref("postificus_ops", 2)),
        R.SKILLS["health"],
    ),
    "maieutic_semiconductor": ResumeSpec(
        FIRST8_DIR,
        "maieutic_semiconductor_intern_resume.pdf",
        "platform",
        "default",
        (R.ref("hyoka_agent"), R.ref("postificus_ops"), R.ref("penny_finance", 2)),
        R.SKILLS["ai_backend"],
    ),
    "pulse": ResumeSpec(
        FIRST8_DIR,
        "pulse_intern_resume.pdf",
        "health",
        "health",
        (R.ref("swish_ops"), R.ref("postificus_ops", 2), R.ref("hyoka_audit")),
        R.SKILLS["health"],
    ),
    "trupeer_ai": ResumeSpec(
        FIRST8_DIR,
        "trupeer_ai_intern_resume.pdf",
        "backend",
        "data",
        (R.ref("hyoka_agent"), R.ref("postificus_ops"), R.ref("seaweed_short", 1)),
        R.SKILLS["ai_backend"],
    ),
    "enerzolve_smart_technologies": ResumeSpec(
        FIRST8_DIR,
        "enerzolve_smart_technologies_intern_resume.pdf",
        "platform",
        "data",
        (R.ref("postificus_ops"), R.ref("hyoka_platform"), R.ref("seaweed_short", 1)),
        R.SKILLS["platform"],
    ),
    "sedna_horeca": ResumeSpec(
        FIRST8_DIR,
        "sedna_horeca_intern_resume.pdf",
        "backend",
        "data",
        (R.ref("swish_ops"), R.ref("postificus_ops"), R.ref("seaweed_short", 1)),
        R.SKILLS["backend"],
    ),
}


MISSING_RESUMES: dict[str, ResumeSpec] = {
    "emergent": ResumeSpec(OUT_DIR, "emergent_ai_platform_intern_resume.pdf", "backend", "default", (R.ref("hyoka_agent"), R.ref("postificus_ops"), R.ref("seaweed_short", 1)), R.SKILLS["ai_backend"]),
    "vimag_labs": ResumeSpec(OUT_DIR, "vimag_labs_python_systems_intern_resume.pdf", "platform", "data", (R.ref("postificus_ops"), R.ref("hyoka_platform"), R.ref("seaweed_short", 1)), R.SKILLS["platform"]),
    "dazzl": ResumeSpec(OUT_DIR, "dazzl_backend_product_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "escape_plan": ResumeSpec(OUT_DIR, "escape_plan_backend_product_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "peeko": ResumeSpec(OUT_DIR, "peeko_backend_product_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "pb_healthcare": ResumeSpec(OUT_DIR, "pb_healthcare_healthtech_backend_intern_resume.pdf", "health", "health", (R.ref("hyoka_audit"), R.ref("swish_care"), R.ref("postificus_ops", 2)), R.SKILLS["health"]),
    "chini_kum": ResumeSpec(OUT_DIR, "chini_kum_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "cosmoss": ResumeSpec(OUT_DIR, "cosmoss_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "filli_and_me": ResumeSpec(OUT_DIR, "filli_and_me_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "handypanda": ResumeSpec(OUT_DIR, "handypanda_marketplace_backend_intern_resume.pdf", "backend", "data", (R.ref("postificus_content"), R.ref("swish_ops", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "nester": ResumeSpec(OUT_DIR, "nester_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "ozi": ResumeSpec(OUT_DIR, "ozi_backend_product_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "rara_barefoot": ResumeSpec(OUT_DIR, "rara_barefoot_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "rotoris": ResumeSpec(OUT_DIR, "rotoris_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "tvissa": ResumeSpec(OUT_DIR, "tvissa_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "unbound": ResumeSpec(OUT_DIR, "unbound_backend_ops_intern_resume.pdf", "backend", "data", (R.ref("swish_ops"), R.ref("postificus_content", 2), R.ref("seaweed_short", 1)), R.SKILLS["backend"]),
    "for_real": ResumeSpec(OUT_DIR, "for_real_marketplace_backend_intern_resume.pdf", "backend", "data", (R.ref("seaweed_short"), R.ref("postificus_content", 2), R.ref("swish_care")), R.SKILLS["backend"]),
}


MISSING_EMAILS: tuple[EmailSpec, ...] = (
    EmailSpec(
        "emergent",
        "Emergent",
        "",
        "Backend/AI platform internship inquiry - Emergent",
        "emergent_ai_platform_intern_resume.pdf",
        """Hi Emergent team,

I came across Emergent while going through early AI product companies. The app-builder direction stood out to me because the difficult part is not just generation; it is keeping workflows, integrations, previews, deployment state, and user changes reliable enough for people to trust.

My closest work is Hyoka, where I built trace ingestion, eval/replay workers, validation gates, audit logs, worker leases, and Postgres-backed metadata for AI workflows. I have also built Postificus, a Go backend around fragmented external workflows with queues, retries, DLQs, health checks, metrics, and recoverable job state.

If there is room for an intern on backend APIs, AI workflow reliability, integrations, eval tooling, or internal platform work, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "vimag_labs",
        "Vimag Labs",
        "",
        "Python/systems internship inquiry - Vimag Labs",
        "vimag_labs_python_systems_intern_resume.pdf",
        """Hi Vimag Labs team,

I found Vimag Labs in an early-startup tracker, but there was not much public detail available from my side. From the available signal, it looked closer to EV motor/control or deeptech systems than a normal web product.

I do not want to pretend I can contribute to motor-control firmware from day one. The area where I may be useful is Python tooling, backend/internal tools, data workflows, debugging infrastructure, validation records, and making engineering workflows easier to inspect.

Some relevant work: I built Postificus, a Go backend with workers, retries, DLQs, health checks, and Prometheus metrics; Hyoka, an eval/replay backend with worker leases, audit logs, artifacts, and Postgres metadata; and GSoC work involving Python data-processing paths, generated artifacts, correctness checks, and runtime optimization.

If there is any Python tooling, backend, data workflow, or internal platform work where an intern can help, I would be glad to be considered. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "dazzl",
        "Dazzl",
        "",
        "Backend/product internship inquiry - Dazzl",
        "dazzl_backend_product_intern_resume.pdf",
        """Hi Dazzl team,

I came across Dazzl while looking at early Bengaluru/Gurugram startups. The quick beauty-services angle looked interesting because the software behind it has to coordinate bookings, provider availability, customer state, service status, payments, support, and internal ops.

That is close to the kind of backend/product work I have been building. Swish models operational support state with order, evidence, policy, trust, and escalation context. Postificus gave me queue-backed workflow experience with REST APIs, PostgreSQL, Redis, RabbitMQ, retries, DLQs, health checks, and metrics. Seaweed shows I can build user-facing backend flows with Go, PostgreSQL, Firebase Auth, S3-backed submissions, Judge0, and live views.

If Dazzl is open to interns on backend APIs, booking/provider workflows, internal tools, dashboards, or support/ops automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "escape_plan",
        "Escape Plan",
        "",
        "Backend/full-stack internship inquiry - Escape Plan",
        "escape_plan_backend_product_intern_resume.pdf",
        """Hi Escape Plan team,

I came across Escape Plan while mapping early consumer startups. If you are building travel/luggage commerce software in-house, the backend work looks practical: catalog, checkout, order status, customer support, inventory, personalization, and internal tools.

My relevant work is around product workflows rather than generic landing pages. Swish models support and escalation state; Postificus handles queue-backed workflows with PostgreSQL/Redis state, retries, DLQs, and metrics; and Seaweed shows user-facing backend work with auth, submissions, admin controls, and live views.

If there is room for an intern on backend/full-stack product work, ecommerce workflows, internal tools, or ops dashboards, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "peeko",
        "Peeko",
        "",
        "Backend/product internship inquiry - Peeko",
        "peeko_backend_product_intern_resume.pdf",
        """Hi Peeko team,

I came across Peeko while looking at early consumer-commerce startups. A babycare quick-commerce product seems to need dependable backend workflows around catalog, inventory, delivery slots, order state, customer support, and internal operations.

The work I can bring is mostly backend/product reliability. Swish models support cases with operational context and deterministic policy; Postificus handles long-running workflows with queues, retries, DLQs, health checks, and metrics; and Seaweed shows I can ship user-facing backend flows with auth, admin controls, and live status.

If you are open to interns on backend APIs, inventory/order workflows, internal tools, dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "pb_healthcare",
        "PB Healthcare",
        "",
        "Healthtech/backend internship inquiry - PB Healthcare",
        "pb_healthcare_healthtech_backend_intern_resume.pdf",
        """Hi PB Healthcare team,

I found PB Healthcare in an early-startup tracker, but I did not have enough public detail to identify a specific product page. If you are building healthcare software or internal hospital/clinic workflows, I think my background may still be relevant.

My strongest match is Google Summer of Code with Invesalius, where I worked on medical-imaging segmentation for 95 anatomical brain regions, generated masks, NIfTI/MGZ MRI preprocessing, label/orientation debugging, and runtime optimization. I have also built Hyoka for traceable AI evaluation/replay workflows and Swish for policy-grounded operational support workflows.

If there is room for an intern on healthtech backend, data pipelines, internal tools, QA/validation workflows, or AI-assisted product tooling, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "chini_kum",
        "CHINI KUM",
        "care@drinkchinikum.com",
        "Backend/ops tooling internship inquiry - CHINI KUM",
        "chini_kum_backend_ops_intern_resume.pdf",
        """Hi CHINI KUM team,

I came across CHINI KUM while looking at early consumer startups. This may be a stretch if you are not hiring software interns, but D2C beverage brands often end up needing useful internal software around ecommerce, inventory, customer support, subscriptions, analytics, and growth workflows.

My relevant work is backend/product tooling: Swish models support and escalation workflows, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Bentham AI gave me experience building recoverable workflow automation around messy external systems.

If there is room for an intern on internal tools, ecommerce backend work, analytics/ops dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "cosmoss",
        "CosMoss",
        "",
        "Backend/ops tooling internship inquiry - CosMoss",
        "cosmoss_backend_ops_intern_resume.pdf",
        """Hi CosMoss team,

I came across CosMoss while looking at early consumer/ecommerce startups. If you are building software internally, the useful work likely sits around catalog, checkout, customer support, inventory, CRM, analytics, and operational dashboards.

My closest work is backend workflow tooling. Swish models support state and escalation decisions, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed shows I can ship user-facing backend flows with auth, admin controls, and live views.

If there is room for an intern on backend/full-stack internal tools, ecommerce workflows, analytics dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "filli_and_me",
        "Filli & Me",
        "",
        "Backend/ops tooling internship inquiry - Filli & Me",
        "filli_and_me_backend_ops_intern_resume.pdf",
        """Hi Filli & Me team,

I came across Filli & Me while mapping early consumer brands. For a school-bag/ecommerce business, the software that can create leverage is often internal: catalog, inventory, order state, customer support, analytics, and fulfillment visibility.

My relevant work is around backend/product workflows. Swish models support and escalation context, Postificus handles long-running workflow jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed shows user-facing backend work with auth, admin controls, and live status.

If you are open to interns on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "handypanda",
        "HandyPanda",
        "contact@handypanda.in",
        "Marketplace backend internship inquiry - HandyPanda",
        "handypanda_marketplace_backend_intern_resume.pdf",
        """Hi HandyPanda team,

I came across HandyPanda while looking at early marketplace startups. Construction/renovation material delivery looks like a stronger software problem than a simple store: vendor inventory, pricing, delivery status, order changes, service reliability, and ops dashboards all matter.

My closest work is backend workflow reliability. Postificus handles fragmented external workflows with REST APIs, PostgreSQL, Redis, RabbitMQ workers, retries, DLQs, health checks, and metrics. Swish models operational support state with evidence, issue type, desired resolution, trust/context, and escalation paths. Seaweed shows I can build user-facing backend flows with Go, PostgreSQL, auth, admin controls, and live views.

If there is room for an intern on marketplace backend APIs, vendor/order workflows, internal tools, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "nester",
        "Nester",
        "",
        "Backend/ops tooling internship inquiry - Nester",
        "nester_backend_ops_intern_resume.pdf",
        """Hi Nester team,

I came across Nester while looking at early ecommerce startups. If you are building internal software around homeware/appliance commerce, useful backend work likely sits around catalog, inventory, checkout, customer support, analytics, and order visibility.

My relevant work is backend workflow tooling: Swish for support/ops state, Postificus for queue-backed workflow jobs with PostgreSQL/Redis, retries, DLQs, health checks, and metrics, and Seaweed for user-facing backend flows with auth, admin controls, and live views.

If there is room for an intern on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "ozi",
        "OZi",
        "",
        "Backend/product internship inquiry - OZi",
        "ozi_backend_product_intern_resume.pdf",
        """Hi OZi team,

I came across OZi while mapping early consumer-commerce startups. A kids/baby quick-delivery app seems to need practical backend systems around catalog, inventory, dispatch, delivery status, customer support, and internal operations.

My closest relevant work is backend/product workflows. Swish models operational support state, Postificus handles queue-backed jobs with retries, DLQs, health checks, metrics, and PostgreSQL/Redis state, and Seaweed shows user-facing backend flows with Go, PostgreSQL, auth, admin controls, and live views.

If there is room for an intern on backend APIs, delivery/order workflows, internal tools, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "rara_barefoot",
        "RARA Barefoot",
        "",
        "Backend/ops tooling internship inquiry - RARA Barefoot",
        "rara_barefoot_backend_ops_intern_resume.pdf",
        """Hi RARA Barefoot team,

I came across RARA Barefoot while looking at early consumer brands. This may be a stretch if you are not hiring software interns, but D2C footwear brands often need useful internal tooling around ecommerce, inventory, customer support, analytics, CRM, and fulfillment workflows.

My relevant work is backend/product tooling. Swish models support and escalation workflows, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Bentham AI gave me experience building recoverable workflow automation around messy external systems.

If there is room for an intern on internal tools, ecommerce backend work, dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "rotoris",
        "Rotoris",
        "support@rotoris.com",
        "Backend/ops tooling internship inquiry - Rotoris",
        "rotoris_backend_ops_intern_resume.pdf",
        """Hi Rotoris team,

I came across Rotoris while looking at early consumer brands. This may be a stretch if you are not hiring software interns, but a watch/ecommerce brand can still benefit from internal tools around catalog, order visibility, inventory, customer support, analytics, and growth workflows.

My relevant work is backend/product tooling: Swish for support-state modeling, Postificus for queue-backed workflow jobs with PostgreSQL/Redis, retries, DLQs, health checks, and metrics, and Seaweed for user-facing backend flows with auth, admin controls, and live views.

If there is room for an intern on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "tvissa",
        "Tvissa",
        "",
        "Backend/ops tooling internship inquiry - Tvissa",
        "tvissa_backend_ops_intern_resume.pdf",
        """Hi Tvissa team,

I came across Tvissa while looking at early ecommerce brands. For a handcrafted saree or apparel commerce business, useful software often means better catalog workflows, inventory/order visibility, customer support tooling, analytics, and operational dashboards.

My relevant work is backend workflow tooling. Swish models support and escalation context, Postificus handles queue-backed jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed shows user-facing backend flows with auth, admin controls, and live views.

If there is room for an intern on backend/full-stack internal tools, ecommerce workflows, dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "unbound",
        "Unbound",
        "",
        "Backend/ops tooling internship inquiry - Unbound",
        "unbound_backend_ops_intern_resume.pdf",
        """Hi Unbound team,

I came across Unbound while mapping early D2C brands. If you are building software internally around skincare/haircare commerce, the useful backend work likely sits around subscriptions, CRM, inventory, customer support, analytics, and growth/ops workflows.

My closest work is backend/product tooling: Swish for support-state and escalation modeling, Postificus for queue-backed workflow jobs with PostgreSQL/Redis state, retries, DLQs, health checks, and metrics, and Seaweed for user-facing backend flows with auth, admin controls, and live views.

If there is room for an intern on internal tools, ecommerce backend work, dashboards, or support automation, I would be glad to contribute. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
    EmailSpec(
        "for_real",
        "For Real",
        "",
        "Marketplace/backend internship inquiry - For Real",
        "for_real_marketplace_backend_intern_resume.pdf",
        """Hi For Real team,

I found For Real in an early-startup tracker, but I did not have enough public detail to identify the exact product page. The signal I had was an off-price shopping or online factory-outlet marketplace, which sounds like a backend/product problem around catalog, pricing, order state, inventory, seller flows, and customer support.

My relevant work is around backend workflow reliability. Seaweed shows user-facing backend flows with Go, PostgreSQL, auth, admin controls, and live views. Postificus handles fragmented external workflows with queues, retries, DLQs, health checks, and metrics. Swish models support/ops state with evidence, issue type, desired resolution, trust/context, and escalation paths.

If there is room for an intern on marketplace backend APIs, catalog/order workflows, internal tools, dashboards, or support automation, I would be glad to help. I have attached my resume for context.

Regards,
Shuvam Pal
https://github.com/unichronic
https://linkedin.com/in/shuvampal3960""",
    ),
)


EXISTING_EMAIL_FILES = (
    FIRST8_DIR / "atlas_email.md",
    FIRST8_DIR / "bhindi_ai_email.md",
    FIRST8_DIR / "cent_email.md",
    FIRST8_DIR / "maieutic_semiconductor_email.md",
    FIRST8_DIR / "pulse_email.md",
    FIRST8_DIR / "trupeer_ai_email.md",
    FIRST8_DIR / "enerzolve_smart_technologies_email.md",
    FIRST8_DIR / "sedna_horeca_email.md",
    MYJOBB_DIR / "myjobb_backend_engineer_email.md",
    REST_DIR / "vibrium_email.md",
    REST_DIR / "ateli_email.md",
    REST_DIR / "kluisz_ai_email.md",
    REST_DIR / "stch_email.md",
    REST_DIR / "grevoro_email.md",
    REST_DIR / "pred_email.md",
    REST_DIR / "aamra_seniors_club_email.md",
    REST_DIR / "puresta_email.md",
    REST_DIR / "frex_email.md",
    REST_DIR / "ilios_72_email.md",
)


NON_VIBRIUM10_EXISTING_EMAIL_FILES = (
    FIRST8_DIR / "atlas_email.md",
    FIRST8_DIR / "bhindi_ai_email.md",
    FIRST8_DIR / "cent_email.md",
    FIRST8_DIR / "maieutic_semiconductor_email.md",
    FIRST8_DIR / "pulse_email.md",
    FIRST8_DIR / "trupeer_ai_email.md",
    FIRST8_DIR / "enerzolve_smart_technologies_email.md",
    FIRST8_DIR / "sedna_horeca_email.md",
    MYJOBB_DIR / "myjobb_backend_engineer_email.md",
)


def write_resume(spec: ResumeSpec) -> None:
    spec.out_dir.mkdir(parents=True, exist_ok=True)
    target = R.ResumeTarget(spec.attachment, spec.experience, spec.gsoc, spec.projects, spec.skills)
    tex_path = spec.out_dir / spec.attachment.replace(".pdf", ".tex")
    tex_path.write_text(R.build_tex(target), encoding="utf-8")
    R.compile_pdf(tex_path)
    R.compile_pdf(tex_path)


def write_email(spec: EmailSpec) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"{spec.slug}_email.md"
    recipient = spec.recipient or "No verified public email in tracker. Use founder/key-person LinkedIn, company LinkedIn, or website contact route."
    path.write_text(
        f"""# {spec.company} Email Draft

## Recipient

{recipient}

## Subject

{spec.subject}

## Attachment

`{spec.attachment}`

## Body

{spec.body}
""",
        encoding="utf-8",
    )
    return path


def build_script_file(
    email_files: list[Path],
    script_path: Path,
    attach_dir: Path,
    label_name: str,
    description: str,
) -> None:
    drafts = [GMAIL.parse_email(path) for path in email_files]
    script = GMAIL.build_script(drafts)
    script = script.replace(
        "prepared internship outreach from Vibrium onward",
        description,
    )
    script = script.replace("startup_email_attachments_2026_05_30", attach_dir.name)
    script = script.replace("internship-outreach-drafts", label_name)
    script_path.write_text(script, encoding="utf-8")


def copy_attachments(email_files: list[Path], attach_dir: Path, script_path: Path) -> None:
    attach_dir.mkdir(parents=True, exist_ok=True)
    for old_file in attach_dir.glob("*.pdf"):
        old_file.unlink()

    for path in email_files:
        draft = GMAIL.parse_email(path)
        src = ROOT / draft["resumePath"]
        if not src.exists():
            raise FileNotFoundError(f"Missing resume for {draft['company']}: {src}")
        shutil.copy2(src, attach_dir / src.name)

    (attach_dir / "README.md").write_text(
        f"""# Early Startup Spreadsheet Email Attachments

Upload or sync this folder to Google Drive before running:

- `{script_path.relative_to(ROOT)}`

Paste the Drive folder ID into `CONFIG.resumeDriveFolderId`, then run:

1. `previewDrafts()`
2. `previewResumeAttachments()`
3. `createDrafts()`

Apps Script cannot read local filesystem paths directly. The script uses each `resumePath` only to extract the PDF filename, then looks up that filename inside Google Drive.
""",
        encoding="utf-8",
    )


def write_manifest(email_files: list[Path], manifest_path: Path, title: str) -> None:
    lines = [f"# {title}", "", "| Company | Recipient | Subject | Resume | Email Draft |", "|---|---|---|---|---|"]
    for email_path in email_files:
        draft = GMAIL.parse_email(email_path)
        lines.append(
            f"| {draft['company']} | {draft['to'] or 'LinkedIn/contact route'} | {draft['subject']} | `{Path(draft['resumePath']).name}` | `{email_path.relative_to(ROOT)}` |"
        )
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    for spec in FIRST8_RESUMES.values():
        write_resume(spec)
        print(f"rebuilt first8: {spec.attachment}")

    missing_email_files: list[Path] = []
    for slug, spec in MISSING_RESUMES.items():
        write_resume(spec)
        print(f"built missing: {spec.attachment}")

    for spec in MISSING_EMAILS:
        missing_email_files.append(write_email(spec))

    email_files = [*EXISTING_EMAIL_FILES, *missing_email_files]
    non_vibrium10_email_files = [*NON_VIBRIUM10_EXISTING_EMAIL_FILES, *missing_email_files]

    build_script_file(
        email_files,
        MASTER_SCRIPT,
        ATTACH_DIR,
        "early-startup-spreadsheet-drafts",
        "all early-startup spreadsheet outreach",
    )
    copy_attachments(email_files, ATTACH_DIR, MASTER_SCRIPT)
    write_manifest(email_files, OUT_DIR / "README.md", "Early Startup Spreadsheet Pack")

    build_script_file(
        non_vibrium10_email_files,
        NON_VIBRIUM10_SCRIPT,
        NON_VIBRIUM10_ATTACH_DIR,
        "early-startup-non-vibrium10-drafts",
        "early-startup spreadsheet outreach excluding the 10-company Vibrium batch",
    )
    copy_attachments(non_vibrium10_email_files, NON_VIBRIUM10_ATTACH_DIR, NON_VIBRIUM10_SCRIPT)
    write_manifest(
        non_vibrium10_email_files,
        OUT_DIR / "README_non_vibrium10.md",
        "Early Startup Pack Excluding Vibrium 10",
    )

    print(f"wrote {len(email_files)} drafts to {MASTER_SCRIPT.relative_to(ROOT)}")
    print(f"copied {len(email_files)} PDFs to {ATTACH_DIR.relative_to(ROOT)}")
    print(f"wrote {len(non_vibrium10_email_files)} drafts to {NON_VIBRIUM10_SCRIPT.relative_to(ROOT)}")
    print(f"copied {len(non_vibrium10_email_files)} PDFs to {NON_VIBRIUM10_ATTACH_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
