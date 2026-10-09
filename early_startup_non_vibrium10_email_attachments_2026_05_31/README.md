# Early Startup Spreadsheet Email Attachments

Upload or sync this folder to Google Drive before running:

- `tailored_resumes/early_startups_non_vibrium10_gmail_drafts_2026_05_31.gs`

Paste the Drive folder ID into `CONFIG.resumeDriveFolderId`, then run:

1. `previewDrafts()`
2. `previewResumeAttachments()`
3. `createDrafts()`

Apps Script cannot read local filesystem paths directly. The script uses each `resumePath` only to extract the PDF filename, then looks up that filename inside Google Drive.
