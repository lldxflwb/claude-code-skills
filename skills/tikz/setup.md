# TikZ Skill Setup

## Install Dependencies

### macOS (Homebrew)

```bash
brew install tectonic pdf2svg
```

### Verify

```bash
tectonic --version
pdf2svg  # Should show usage info
```

## Environment Variables (optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `TIKZ_SERVER_HOST` | `127.0.0.1` | Host used in display URLs |
| `TIKZ_SERVER_PORT` | `8073` | Server port |

The server always binds to `0.0.0.0` regardless of `TIKZ_SERVER_HOST`. The host variable only affects the URLs returned to the user.

To override, add to `~/.zshrc`:

```bash
export TIKZ_SERVER_HOST="10.8.0.2"
export TIKZ_SERVER_PORT="9094"
```
