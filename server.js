// 의존성 없는 최소 웹 서버 (Node 표준 라이브러리만 사용)
// 실행: node server.js  → http://0.0.0.0:3000
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const DATA_FILE = path.join(__dirname, "data.json");

function readData() {
  try { return JSON.parse(fs.readFileSync(DATA_FILE, "utf8")); } catch { return []; }
}
function writeData(items) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(items, null, 2));
}
function send(res, status, body, type = "application/json") {
  res.writeHead(status, { "Content-Type": type + "; charset=utf-8" });
  res.end(typeof body === "string" ? body : JSON.stringify(body));
}

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/") {
    return send(res, 200, fs.readFileSync(path.join(__dirname, "index.html"), "utf8"), "text/html");
  }
  if (req.method === "GET" && req.url === "/health") return send(res, 200, { ok: true });
  if (req.method === "GET" && req.url === "/api/items") return send(res, 200, readData());
  if (req.method === "POST" && req.url === "/api/items") {
    let body = "";
    req.on("data", (c) => (body += c));
    req.on("end", () => {
      try {
        const item = JSON.parse(body || "{}");
        if (!item.text || typeof item.text !== "string") return send(res, 400, { error: "text가 필요합니다" });
        const items = readData();
        items.push({ id: Date.now(), text: item.text.trim() });
        writeData(items);
        send(res, 201, items[items.length - 1]);
      } catch { send(res, 400, { error: "잘못된 JSON" }); }
    });
    return;
  }
  send(res, 404, { error: "not found" });
});

server.listen(PORT, "0.0.0.0", () => console.log(`server listening on http://0.0.0.0:${PORT}`));
