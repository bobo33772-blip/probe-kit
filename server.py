"""의존성 없는 최소 웹 서버 (Python 표준 라이브러리만 사용)
실행: python3 server.py  → http://0.0.0.0:3000
"""
import json
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "3000"))
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "data.json")


def read_data():
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def write_data(items):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, ctype="application/json"):
        data = body if isinstance(body, str) else json.dumps(body, ensure_ascii=False)
        self.send_response(status)
        self.send_header("Content-Type", f"{ctype}; charset=utf-8")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
                return self._send(200, f.read(), "text/html")
        if self.path == "/health":
            return self._send(200, {"ok": True})
        if self.path == "/api/items":
            return self._send(200, read_data())
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/items":
            return self._send(404, {"error": "not found"})
        length = int(self.headers.get("Content-Length", "0"))
        try:
            item = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            return self._send(400, {"error": "잘못된 JSON"})
        text = item.get("text")
        if not isinstance(text, str) or not text.strip():
            return self._send(400, {"error": "text가 필요합니다"})
        items = read_data()
        items.append({"id": int(time.time() * 1000), "text": text.strip()})
        write_data(items)
        self._send(201, items[-1])


if __name__ == "__main__":
    print(f"server listening on http://0.0.0.0:{PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
