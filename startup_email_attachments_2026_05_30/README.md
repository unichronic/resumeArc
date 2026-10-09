# Startup Email Attachments

Upload or sync this folder to Google Drive before running:

- `tailored_resumes/startup_all_gmail_drafts_2026_05_30.gs`
- `tailored_resumes/early_startups_rest_2026_05_30/early_startups_rest_gmail_drafts.gs`

After the files are in Drive, paste that Drive folder ID into `CONFIG.resumeDriveFolderId`, then run:

1. `previewDrafts()`
2. `previewResumeAttachments()`
3. `createDrafts()`

Apps Script cannot read local filesystem paths directly. The `resumePath` values in the script are only used to extract the PDF filename, then the script looks up that filename inside Google Drive.
