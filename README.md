# probe-kit

AI 실무 과제용 작업 템플릿 모음 (개인 학습·연습용 공개 저장소).

## 시험장에서 쓰는 법 (3분)

```bash
git clone https://github.com/<GITHUB_ID>/probe-kit
cp probe-kit/templates/AGREEMENT.md ./AGREEMENT.md
cp probe-kit/templates/AGENTS.md    ./AGENTS.md
cp probe-kit/templates/DECISIONS.md ./DECISIONS.md
```

1. 과제 README를 읽고 **필수 파일명**을 확인한다 (README가 지정한 이름이 이 키트보다 우선).
2. `INTERVIEW.md`의 질문으로 업무 담당자와 대화한다.
3. `AGREEMENT.md`를 채우고 담당자에게 확인받는다.
4. `AGENTS.md`의 과제 칸을 채운 뒤, 그 내용을 Codex 첫 메시지로 보낸다.
5. 단계마다 `DECISIONS.md`에 한 줄씩 남긴다.
6. 마무리에 `templates/PROJECT_README.md`로 README를 쓴다.

웹 서비스가 필요하면 `starter-node/` 또는 `starter-python/`을 복사해 시작한다 (의존성 없음, 0.0.0.0 바인딩).

## 구성

| 파일 | 용도 |
|---|---|
| `TIMEBOX.md` | 180분 시간 배분, 서술형 답변 틀 |
| `INTERVIEW.md` | 업무 담당자 인터뷰 질문 세트 |
| `templates/AGREEMENT.md` | 서면 합의문 |
| `templates/AGENTS.md` | 코딩 에이전트 작업 지시문 |
| `templates/DECISIONS.md` | 결정 기록 |
| `templates/PROJECT_README.md` | 결과물 README(핸드오프) |
| `starter-node/` | Node 표준 라이브러리만 쓰는 최소 웹 서버 |
| `starter-python/` | Python 표준 라이브러리만 쓰는 최소 웹 서버 |
