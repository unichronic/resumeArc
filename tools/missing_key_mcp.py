#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP


def main() -> None:
    service = sys.argv[1] if len(sys.argv) > 1 else "service"
    key_name = sys.argv[2] if len(sys.argv) > 2 else "API_KEY"
    key_file = Path.home() / ".config" / "intern-outreach" / "keys.env"
    server = FastMCP(f"{service}-missing-key")

    @server.tool()
    def connection_status() -> dict[str, str]:
        """Explain why this MCP is not connected yet."""
        return {
            "service": service,
            "status": "missing_api_key",
            "needed_key": key_name,
            "key_file": str(key_file),
            "setup_command": "tools/configure_outreach_keys.sh",
        }

    server.run()


if __name__ == "__main__":
    main()

