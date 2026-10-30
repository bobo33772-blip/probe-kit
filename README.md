# probe-kit

AI 실무 과제용 작업 템플릿 모음 (개인 학습·연습용 공개 저장소).

## 시험장에서 쓰는 법

```bash
ls                                   # 과제 폴더에 이미 있는 파일부터 확인
git clone https://github.com/bobo33772-blip/probe-kit
cp probe-kit/AGREEMENT.md probe-kit/DECISIONS.md ./
cp probe-kit/AGENTS.md ./AGENTS.md   # 과제 폴더에 AGENTS.md가 이미 있으면 덮어쓰지 말 것
```

1. 과제 README의 필수 파일명이 이 키트보다 우선한다.
2. INTERVIEW.md 질문으로 업무 담당자와 대화한다.
3. AGREEMENT.md를 채우고 담당자에게 확인받는다.
4. AGENTS.md 과제 칸을 채운 뒤 Codex 첫 메시지로 보낸다.
5. 단계마다 DECISIONS.md에 한 줄씩 남긴다.
6. 마무리에 PROJECT_README.md 틀로 README를 쓴다.

웹 서버가 필요하면: `cp probe-kit/server.js probe-kit/index.html ./` 후 `node server.js`
(Python: `cp probe-kit/server.py probe-kit/index.html ./` 후 `python3 server.py`) → Browser 도구 PORT 3000, URL `/`

| 파일 | 용도 |
|---|---|
| TIMEBOX.md | 180분 배분, 서술형 답변 틀 |
| INTERVIEW.md | 업무 담당자 인터뷰 질문 |
| AGREEMENT.md | 서면 합의문 |
| AGENTS.md | Codex 작업 지시문 |
| DECISIONS.md | 결정 기록 |
| PROJECT_README.md | 결과물 README 틀 |
| server.js / server.py / index.html | 의존성 없는 최소 웹 서버 (0.0.0.0:3000) |
