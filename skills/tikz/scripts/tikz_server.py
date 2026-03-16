#!/usr/bin/env python3
"""Lightweight HTTP server for serving rendered TikZ outputs."""

import json
import signal
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

from config import get_host, get_port

CACHE_DIR = Path.home() / ".cache" / "tikz-skill"
RENDERS_DIR = CACHE_DIR / "renders"
STATE_FILE = CACHE_DIR / "server.json"


class TikZHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(RENDERS_DIR), **kwargs)

    def do_GET(self):
        if self.path == "/healthz":
            self._serve_json(200, {"status": "ok"})
        elif self.path == "/":
            self._serve_index()
        else:
            super().do_GET()

    def _serve_json(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_index(self):
        RENDERS_DIR.mkdir(parents=True, exist_ok=True)
        svgs = sorted(
            RENDERS_DIR.glob("*.svg"),
            key=lambda f: f.stat().st_mtime,
            reverse=True,
        )

        host = get_host()
        port = get_port()
        base_url = f"http://{host}:{port}"

        cards = ""
        for svg in svgs:
            name = svg.stem
            svg_url = f"{base_url}/{svg.name}"
            pdf_path = RENDERS_DIR / f"{name}.pdf"
            pdf_link = ""
            if pdf_path.exists():
                pdf_link = f' | <a href="{base_url}/{name}.pdf">PDF</a>'
            cards += f"""
            <div class="card">
                <a href="{svg_url}"><img src="/{svg.name}" alt="{name}"></a>
                <div class="name">{name}{pdf_link}</div>
            </div>"""

        if not cards:
            cards = '<p class="empty">No renders yet.</p>'

        html = f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>TikZ Renders</title>
<style>
body {{ font-family: system-ui, -apple-system, sans-serif; margin: 2rem; background: #f5f5f5; color: #333; }}
h1 {{ margin-bottom: 1.5rem; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }}
.card {{ background: #fff; border-radius: 8px; padding: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,.1); }}
.card img {{ width: 100%; height: auto; border: 1px solid #eee; border-radius: 4px; }}
.name {{ margin-top: .5rem; font-size: .9rem; color: #555; word-break: break-all; }}
.empty {{ color: #888; text-align: center; grid-column: 1/-1; }}
a {{ color: #2563eb; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
</style>
</head><body>
<h1>TikZ Renders</h1>
<div class="grid">{cards}</div>
</body></html>"""

        body = html.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass


def main():
    port = get_port()
    host = get_host()

    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    server = HTTPServer(("0.0.0.0", port), TikZHandler)

    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({
        "pid": __import__("os").getpid(),
        "host": host,
        "port": port,
    }))

    def shutdown(signum, frame):
        server.shutdown()
        STATE_FILE.unlink(missing_ok=True)
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    print(f"TikZ server listening on 0.0.0.0:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
