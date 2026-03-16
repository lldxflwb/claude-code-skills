"""Shared config: env vars > config.json > hardcoded defaults."""

import json
import os
from pathlib import Path

_CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.json"
_DEFAULTS = {"host": "127.0.0.1", "port": 8073, "default_view_mode": "normal"}


def _load_file_config():
    try:
        return json.loads(_CONFIG_FILE.read_text())
    except Exception:
        return {}


_file_cfg = _load_file_config()


def get_host():
    return os.environ.get("TIKZ_SERVER_HOST") or _file_cfg.get("host") or _DEFAULTS["host"]


def get_port():
    val = os.environ.get("TIKZ_SERVER_PORT")
    if val:
        return int(val)
    return _file_cfg.get("port") or _DEFAULTS["port"]


def get_default_view_mode():
    val = os.environ.get("TIKZ_DEFAULT_VIEW_MODE")
    if val and val in ("eink", "normal"):
        return val
    return _file_cfg.get("default_view_mode") or _DEFAULTS["default_view_mode"]
