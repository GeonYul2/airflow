# Task 01 — Basic Analytics DAG

## Background
당신은 데이터 분석팀의 주니어 분석가다.
매일 발생하는 간단한 원천 데이터를 집계해
분석 테이블을 생성하는 자동화 DAG를 만들어야 한다.

이 DAG는 “Airflow DAG의 최소 단위”를 학습하기 위한 것이다.

---

## Goal
- Airflow DAG의 기본 구조를 이해한다.
- Task 간 의존성을 명확히 설계한다.
- “왜 이 DAG가 필요한지”를 설명할 수 있다.

---

## Requirements

### Data Scenario
- 외부 입력은 필요 없다.
- Python 함수 내부에서 더미 데이터를 생성해도 된다.
- 예: 일별 매출 데이터, 사용자 수, 이벤트 수 등

---

### DAG Requirements
- DAG 1개
- PythonOperator 사용
- Task 최소 3개 이상
- Task 간 명확한 의존성 note 필요

---

### Task Structure (예시 방향)
- Task A: 원천 데이터 생성
- Task B: 데이터 집계
- Task C: 결과 출력 또는 저장 (print 또는 파일)

※ 위 구조는 예시이며, 반드시 따를 필요는 없다.

---

## Constraints
- BashOperator 사용 금지
- XCom 사용 금지
- execution_date 사용 금지

---

## Deliverables
- DAG Python 파일
- DAG 설명 MD (설명 템플릿 사용)

---

## Evaluation Criteria
- DAG 구조가 단순한가?
- 각 Task의 책임이 명확한가?
- 이 DAG를 왜 만들었는지 말로 설명 가능한가?
