#!/usr/bin/env bash
set -euo pipefail

KEY_FILE="${OUTREACH_KEYS_FILE:-$HOME/.config/intern-outreach/keys.env}"
if [[ -f "$KEY_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$KEY_FILE"
  set +a
fi

if [[ -z "${HUNTER_API_KEY:-}" ]]; then
  exec /home/unichronic/intern/tools/missing_key_mcp.py hunter HUNTER_API_KEY
fi

exec npx -y mcp-remote https://mcp.hunter.io/sse --header "X-API-KEY:${HUNTER_API_KEY}"
