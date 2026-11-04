# probe-kit

AI 실무 과제용 작업 템플릿 모음 (개인 학습·연습용 공개 저장소). 과제 내용은 포함하지 않는 범용 양식이다.

## 시험장에서 쓰는 법

```bash
ls                                   # 과제 폴더에 원래 있는 파일 확인
git clone https://github.com/bobo33772-blip/probe-kit
cp probe-kit/AGREEMENT.md probe-kit/DECISIONS.md probe-kit/UNDERSTAND.md ./
```

- 과제 폴더에 AGENTS.md가 이미 있으면 덮어쓰지 않는다. probe-kit/AGENTS.md는 열어서 보며 Codex 첫 메시지를 쓴다.
- 과제 README의 필수 파일명·형식이 이 키트보다 우선한다.

## 순서
1. TIMEBOX.md를 옆에 둔다.
2. INTERVIEW.md 질문으로 업무 담당자와 대화한다.
3. AGREEMENT.md를 채우고 담당자에게 확인받는다. 흐름(입력 → 처리 → 출력)을 직접 쓴다.
4. AGENTS.md 형식으로 Codex에게 구조 제안만 받고, 이해될 때까지 묻는다.
5. 단계 루프: 위임 → 직접 확인 → 내 말로 DECISIONS 한 줄 → 커밋.
6. 85·140·165분에 UNDERSTAND.md를 갱신하고, 제출 직전에 한 번 읽는다.

| 파일 | 용도 |
|---|---|
| TIMEBOX.md | 180분 배분, 단계 루프, 서술형 대비표 |
| INTERVIEW.md | 업무 담당자 인터뷰 질문 |
| AGREEMENT.md | 서면 합의문 |
| AGENTS.md | Codex 작업 지시문 (단계마다 이유·실패 지점 보고) |
| DECISIONS.md | 결정 기록 |
| UNDERSTAND.md | 내 말로 쓰는 이해 노트 (서술형 답의 재료) |
| PROMPTS.md | 고득점용 문장 모음 (우선순위·지표·테스트·중간 확인·마무리 점검) |
| PROJECT_README.md | 결과물 README 틀 |
| server.js / server.py / index.html | 환경 점검용 최소 웹 서버 (과제에는 사용하지 않음) |
