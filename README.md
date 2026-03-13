# Claude Code Skills

A collection of open-source skills for [Claude Code](https://claude.com/claude-code).

## Quick Start

Copy the following to your AI assistant to install all skills:

```
请帮我安装 Claude Code Skills：
1. git clone https://github.com/lldxflwb/claude-code-skills.git /tmp/claude-code-skills
2. mkdir -p ~/.claude/skills
3. cp -r /tmp/claude-code-skills/skills/* ~/.claude/skills/
4. rm -rf /tmp/claude-code-skills
5. ls ~/.claude/skills/ && echo "安装成功"
每个 skill 可能有额外依赖，请检查对应目录下的 SKILL.md。
```

## Skills

| Skill | Description |
|-------|-------------|
| [codex](skills/codex/) | Invoke Codex CLI from Claude Code to get a second opinion from GPT models. Supports session resume for multi-turn conversations. |

## Installation

Copy the skill directory to your Claude Code skills folder:

```bash
# Install a single skill
cp -r skills/codex ~/.claude/skills/codex
```

## Prerequisites

Each skill may have its own prerequisites. Check the `SKILL.md` file in each skill directory for details.

## Contributing

1. Each skill lives in its own directory under `skills/`
2. Every skill must have a `SKILL.md` with proper frontmatter
3. Supporting scripts go in a `scripts/` subdirectory
4. Include clear prerequisites and usage examples

## License

MIT
