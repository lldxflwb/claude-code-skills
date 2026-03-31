#!/usr/bin/env python3
"""
Update Claude Agent SDK documentation using `claude -p` with WebFetch.

The docs site (platform.claude.com) is JS-rendered, so plain HTTP requests
only get "Loading..." placeholders. This script uses Claude Code's WebFetch
tool to fetch fully rendered content.

Usage: python3 scripts/update-docs.py
"""

import os
import subprocess
import sys
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "..", "docs")
BASE_URL = "https://platform.claude.com/docs/en/agent-sdk"

PAGES = [
    ("overview", "Agent SDK Overview"),
    ("quickstart", "Quickstart"),
    ("agent-loop", "How the Agent Loop Works"),
    ("claude-code-features", "Use Claude Code Features"),
    ("sessions", "Work with Sessions"),
    ("streaming-vs-single-mode", "Streaming Input"),
    ("streaming-output", "Stream Responses in Real-time"),
    ("mcp", "Connect MCP Servers"),
    ("custom-tools", "Define Custom Tools"),
    ("tool-search", "Tool Search"),
    ("permissions", "Handling Permissions"),
    ("user-input", "User Approvals and Input"),
    ("hooks", "Control Execution with Hooks"),
    ("file-checkpointing", "File Checkpointing"),
    ("structured-outputs", "Structured Outputs in the SDK"),
    ("hosting", "Hosting the Agent SDK"),
    ("secure-deployment", "Securely Deploying AI Agents"),
    ("modifying-system-prompts", "Modifying System Prompts"),
    ("subagents", "Subagents in the SDK"),
    ("slash-commands", "Slash Commands in the SDK"),
    ("skills", "Agent Skills in the SDK"),
    ("cost-tracking", "Track Cost and Usage"),
    ("todo-tracking", "Todo Lists"),
    ("plugins", "Plugins in the SDK"),
    ("typescript", "TypeScript SDK Reference"),
    ("typescript-v2-preview", "TypeScript V2 (Preview)"),
    ("python", "Python SDK Reference"),
    ("migration-guide", "Migration Guide"),
]


def fetch_with_claude(url: str) -> str | None:
    """Use `claude -p` to fetch a page via WebFetch and return markdown content."""
    prompt = (
        f"Use WebFetch to fetch {url} and return the COMPLETE page content as markdown. "
        "Include ALL text, code examples, tables, and headings. "
        "Do not summarize - return everything verbatim. "
        "Output ONLY the markdown content, no commentary."
    )
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--allowedTools", "WebFetch"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0 and len(result.stdout.strip()) > 100:
            return result.stdout.strip()
        return None
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"  Error: {e}")
        return None


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Check claude CLI is available
    try:
        subprocess.run(["claude", "--version"], capture_output=True, timeout=10)
    except FileNotFoundError:
        print("Error: `claude` CLI not found. Install Claude Code first.")
        sys.exit(1)

    total = len(PAGES)
    success = 0
    fail = 0

    print(f"Updating {total} Agent SDK doc pages...")
    print(f"Target: {DOCS_DIR}")
    print(f"Using: claude -p + WebFetch")
    print()

    for i, (slug, title) in enumerate(PAGES, 1):
        url = f"{BASE_URL}/{slug}"
        outfile = os.path.join(DOCS_DIR, f"{slug}.md")
        print(f"[{i}/{total}] {title}... ", end="", flush=True)

        content = fetch_with_claude(url)

        if not content:
            print("FAILED")
            fail += 1
            continue

        with open(outfile, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"Source: https://docs.anthropic.com/en/agent-sdk/{slug}\n")
            f.write(f"Updated: {today}\n\n")
            f.write("---\n\n")
            f.write(content)
            f.write("\n")

        size = len(content)
        print(f"OK ({size} chars)")
        success += 1

    # Write index file
    index_path = os.path.join(DOCS_DIR, "INDEX.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# Claude Agent SDK Documentation Index\n\n")
        f.write(f"Updated: {today}\n\n")
        f.write(f"Source: https://docs.anthropic.com/en/agent-sdk\n\n")
        for slug, title in PAGES:
            f.write(f"- [{title}]({slug}.md)\n")

    print()
    print(f"Done! Success: {success}, Failed: {fail}")
    print(f"Index: {index_path}")


if __name__ == "__main__":
    main()
