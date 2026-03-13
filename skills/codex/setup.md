# Codex CLI 环境检测与安装引导

当用户首次使用 `/codex` 时，按以下步骤检测环境：

## 1. 检测 Codex CLI

```bash
which codex 2>/dev/null && codex --version || echo "CODEX_NOT_FOUND"
```

- 如果输出 `CODEX_NOT_FOUND`，提示用户：

```
Codex CLI 未安装。需要先安装才能使用 /codex skill。

安装命令：
  npm install -g @openai/codex

安装完成后请运行 `codex login` 登录。
```

- 如果已安装，继续检测登录状态。

## 2. 检测登录状态

```bash
codex exec --sandbox read-only --skip-git-repo-check -o /dev/null - <<< "ping" 2>&1 | head -5
```

- 如果输出包含 `auth` 或 `login` 相关错误，提示用户：

```
Codex CLI 已安装但未登录。请运行：
  codex login
```

## 3. 检测结果处理

- **全部通过** → 正常执行 skill
- **任一失败** → 展示上述提示，不执行 Codex 任务
