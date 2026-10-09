from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "tailored_resumes" / "startup_all_gmail_drafts_2026_05_30.gs"

EMAIL_FILES = (
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "vibrium_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "ateli_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "kluisz_ai_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "stch_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "grevoro_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "pred_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "aamra_seniors_club_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "puresta_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "frex_email.md",
    ROOT / "tailored_resumes" / "early_startups_rest_2026_05_30" / "ilios_72_email.md",
    ROOT / "tailored_resumes" / "myjobb_ai_backend_2026_05_29" / "myjobb_backend_engineer_email.md",
    ROOT / "tailored_resumes" / "algokart_backend_2026_05_29" / "algokart_backend_email.md",
    ROOT / "tailored_resumes" / "circles_software_engineer_intern_2026_05_29" / "circles_software_engineer_intern_email.md",
)


def section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    if not match:
        return ""
    return match.group(1).strip()


def parse_email(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^#\s+(.+?)\s+Email Draft\s*$", text, re.M)
    company = title.group(1).strip() if title else path.stem.replace("_email", "").replace("_", " ").title()

    recipient_block = section(text, "Recipient")
    email_match = re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", recipient_block)
    to = email_match.group(0) if email_match else ""

    attachment_block = section(text, "Attachment")
    attachment_match = re.search(r"`([^`]+\.pdf)`|([A-Za-z0-9_./-]+\.pdf)", attachment_block)
    attachment = attachment_match.group(1) or attachment_match.group(2) if attachment_match else ""
    if attachment:
        attachment_path = path.parent.relative_to(ROOT) / attachment
    else:
        attachment_path = Path("")

    body = section(text, "Body").replace("**", "").strip()
    subject = section(text, "Subject").strip()

    return {
        "company": company,
        "to": to,
        "subject": subject,
        "resumePath": str(attachment_path),
        "body": body,
    }


def build_script(drafts: list[dict[str, str]]) -> str:
    return """/**
 * Gmail draft creator for prepared internship outreach from Vibrium onward.
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
  labelName: 'internship-outreach-drafts',
  dryRun: false,
  dedupe: true,
  attachResumes: true,
  requireResumeAttachment: true,
  // Paste the ID from a Drive folder URL. Leave blank to search all visible Drive files by filename.
  resumeDriveFolderId: '',
  createMissingRecipientDraftsToSelf: true,
  missingRecipientSubjectPrefix: '[ADD TO] ',
};

const DRAFTS = """ + json.dumps(drafts, indent=2) + """;

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
  const raw = [company, to, subject, body, attachmentNames || ''].join('\\n');
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
"""


def main() -> None:
    drafts = [parse_email(path) for path in EMAIL_FILES]
    OUTPUT.write_text(build_script(drafts), encoding="utf-8")
    print(f"Wrote {len(drafts)} drafts to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
