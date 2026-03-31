# Claude Agent SDK

Provides local documentation for the Claude Agent SDK (formerly Claude Code SDK).
Use this skill to answer questions about building AI agents with the Agent SDK,
including Python and TypeScript API usage, built-in tools, hooks, subagents, MCP,
sessions, permissions, structured outputs, hosting, deployment, and more.

## When to use

- When the user asks about Claude Agent SDK development, API, or configuration
- When developing code that imports `claude_agent_sdk` or `@anthropic-ai/claude-agent-sdk`
- When the user mentions "agent sdk", "claude agent sdk", or "claude code sdk"
- When building AI agents using the Agent SDK

## When NOT to use

- General Claude API questions that don't involve the Agent SDK
- Claude Code CLI usage questions (use claude-code-guide agent instead)

## Instructions

1. Read the documentation index at `skills/agent-sdk/docs/INDEX.md` to understand the available docs
2. Based on the user's question, read the relevant doc file(s) from `skills/agent-sdk/docs/`
3. Answer the question using the documentation content, providing code examples when appropriate
4. Always include both Python and TypeScript examples when available in the docs

### Documentation update

When the user says "update agent sdk docs" or "更新 agent sdk 文档":

1. Run the update script: `python3 skills/agent-sdk/scripts/update-docs.py`
2. Report how many pages were updated successfully

### Key documentation files

| Topic | File |
|-------|------|
| Overview & getting started | `docs/overview.md` |
| Quickstart tutorial | `docs/quickstart.md` |
| Agent loop internals | `docs/agent-loop.md` |
| Claude Code features | `docs/claude-code-features.md` |
| Sessions & context | `docs/sessions.md` |
| Streaming input | `docs/streaming-vs-single-mode.md` |
| Streaming output | `docs/streaming-output.md` |
| MCP servers | `docs/mcp.md` |
| Custom tools | `docs/custom-tools.md` |
| Tool search | `docs/tool-search.md` |
| Permissions | `docs/permissions.md` |
| User input & approvals | `docs/user-input.md` |
| Hooks | `docs/hooks.md` |
| File checkpointing | `docs/file-checkpointing.md` |
| Structured outputs | `docs/structured-outputs.md` |
| Hosting | `docs/hosting.md` |
| Secure deployment | `docs/secure-deployment.md` |
| System prompts | `docs/modifying-system-prompts.md` |
| Subagents | `docs/subagents.md` |
| Slash commands | `docs/slash-commands.md` |
| Skills | `docs/skills.md` |
| Cost tracking | `docs/cost-tracking.md` |
| Todo lists | `docs/todo-tracking.md` |
| Plugins | `docs/plugins.md` |
| TypeScript SDK ref | `docs/typescript.md` |
| TypeScript V2 | `docs/typescript-v2-preview.md` |
| Python SDK ref | `docs/python.md` |
| Migration guide | `docs/migration-guide.md` |
