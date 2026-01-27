# Task 04 — XCom KPI Handoff Pipeline

## Background
분석 파이프라인에서는 “중간 결과(예: KPI)”를 다음 Task로 넘겨
후속 작업(저장/알림/검증)에 활용한다.

이번 과제는 XCom을 “필요한 곳에만 최소로” 쓰는 연습이다.

---

## Goal
- XCom의 역할과 한계를 이해한다.
- “넘겨야 하는 값”과 “넘기면 안 되는 값”을 구분한다.
- KPI 산출 → 후속 처리 흐름을 설계한다.

---

## Data Scenario
- 하루치 이벤트 데이터(더미 생성 가능)
- KPI 예시:
  - DAU
  - 결제 전환율
  - 총 매출
  - 이벤트 수

---

## DAG Requirements
- PythonOperator 기반
- Task 최소 5개
- XCom을 최소 1회 이상 사용 (필수)
- 단, XCom에는 "작은 요약 값"만 넣어야 한다.

---

## Mandatory Task Roles
1. Raw 이벤트 데이터 생성
2. 정제/필터링
3. KPI 계산 (딕셔너리 형태의 작은 결과)
4. KPI 검증(예: 값이 0이거나 비정상적으로 크면 실패 처리)
5. KPI 후속 처리(저장/출력/알림 준비 중 택1)

---

## Constraints
- 큰 데이터프레임/리스트 전체를 XCom으로 넘기지 말 것
- Branch 사용 금지
- execution_date 사용 금지 (이번 과제에선 XCom에 집중)

---

## Deliverables
- DAG Python 파일
- DAG 설명 MD (DAG_EXPLANATION_TEMPLATE.md 사용)

---

## Evaluation Criteria
- XCom 사용이 과하지 않은가?
- KPI의 정의가 명확한가?
- 검증 Task가 논리적으로 설계되어 있는가?
