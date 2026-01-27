# Task 05 — Branch-based Anomaly Routing

## Background
실무 분석 자동화에서는 결과가 “정상/비정상”일 때
후속 처리 경로가 달라지는 경우가 많다.
예: 이상치면 경고 알림, 정상이면 저장만 하고 종료.

이번 과제는 Branch를 통한 분기 설계를 연습한다.

---

## Goal
- BranchPythonOperator (또는 @task.branch)로 분기 처리
- Trigger Rule을 이용한 흐름 제어
- 분기 후 “정상 종료”를 깔끔하게 만드는 패턴 학습

---

## Data Scenario
- KPI 1개를 계산한다고 가정 (더미 데이터 가능)
- 이상치 기준 예시:
  - 전일 대비 3배 이상 증가
  - 0 또는 음수
  - 임계값 초과

---

## DAG Requirements
- Task 최소 6개
- Branch를 1회 이상 사용 (필수)
- 분기 후 두 경로 모두 종착 Task로 합류시키기

---

## Mandatory Task Roles
1. 데이터 생성 또는 로드
2. KPI 계산
3. 이상치 판별 (Branch)
4. 정상 경로 처리 (예: 저장)
5. 이상 경로 처리 (예: 경고 메시지 생성/출력)
6. 마무리 Task (정상/이상 모두 합류)

---

## Constraints
- Sensor 사용 금지
- 외부 API 사용 금지
- execution_date 사용 금지
- XCom 사용은 선택 (필요하면 최소로)

---

## Deliverables
- DAG Python 파일
- 분기 설계 설명 MD (분기 이유/Trigger Rule 포함)

---

## Evaluation Criteria
- Branch 결과가 명확한가?
- 분기 후 합류가 깔끔한가?
- 실무에서 알림/저장으로 확장 가능한가?

