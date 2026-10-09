#!/usr/bin/env bash
set -euo pipefail

KEY_FILE="${OUTREACH_KEYS_FILE:-$HOME/.config/intern-outreach/keys.env}"
mkdir -p "$(dirname "$KEY_FILE")"
touch "$KEY_FILE"
chmod 600 "$KEY_FILE"

python3 - "$KEY_FILE" <<'PY'
import getpass
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
current = {}
for line in path.read_text().splitlines():
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or "=" not in stripped:
        continue
    key, value = stripped.split("=", 1)
    current[key.strip()] = value.strip().strip('"').strip("'")

for key in ("HUNTER_API_KEY", "PROSPEO_API_KEY", "REOON_API_KEY"):
    existing = "set" if current.get(key) else "blank"
    value = getpass.getpass(f"{key} ({existing}; leave blank to keep): ").strip()
    if value:
        current[key] = value

lines = [
    "# Private outreach automation keys. Do not commit this file.",
    *(f"{key}={current.get(key, '')}" for key in ("HUNTER_API_KEY", "PROSPEO_API_KEY", "REOON_API_KEY")),
    "",
]
path.write_text("\n".join(lines))
PY

chmod 600 "$KEY_FILE"
echo "Updated $KEY_FILE"

