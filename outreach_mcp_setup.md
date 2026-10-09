# Internship Outreach Automation Setup

This setup is for finding and verifying staff emails for internship cold outreach with free or low-credit tools. It does not automate bulk sending.

## What Is Configured

- `intern_outreach`: local MCP with credit-aware tools for email guesses, role scoring, Reoon verification, Hunter API calls, and Prospeo enrichment.
- `hunter`: official Hunter remote MCP via a local `mcp-remote` wrapper.
- `prospeo`: official Prospeo local MCP via `@prospeo/prospeo-mcp-server`.

## Keys To Add

Create free accounts and put keys in:

```bash
~/.config/intern-outreach/keys.env
```

Use:

```bash
tools/configure_outreach_keys.sh
```

Supported variables:

```bash
HUNTER_API_KEY=
PROSPEO_API_KEY=
REOON_API_KEY=
```

## Recommended Prompt

After restarting Codex so MCP servers load, ask:

```text
Use intern_outreach plus Hunter/Prospeo only if needed.
For these companies, find 2-3 high-signal internship outreach contacts, conserve credits, verify emails, and write a CSV:
company, domain, target roles, reason, verified email, source, confidence, draft note angle.
```

## Free-Credit Strategy

1. Use public web search and names first.
2. Generate likely emails with `intern_outreach.generate_email_guesses`.
3. Verify guessed emails with Reoon `power` mode.
4. Spend Hunter/Prospeo credits only when the person is high-signal.
5. Send 10-20 personalized emails/day manually or as drafts.

## CLI Examples

Generate guesses without credits:

```bash
python3 tools/intern_outreach_mcp.py guess --first-name Jane --last-name Doe --domain example.com
```

Prepare a CSV:

```bash
python3 tools/intern_outreach_mcp.py prepare-csv \
  --input outreach_targets_template.csv \
  --output outreach_results/candidates.csv \
  --verify-with none
```

Check configured keys:

```bash
python3 tools/intern_outreach_mcp.py connections
```
