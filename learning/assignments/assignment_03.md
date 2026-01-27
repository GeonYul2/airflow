# Task 03 — Execution Date-aware Analytics DAG

## Background
실제 분석 자동화에서 가장 많이 발생하는 문제는
“날짜가 바뀌면 분석 결과의 의미가 달라지는 것”이다.

이번 과제에서는 execution_date를 고려한 DAG를 설계한다.

---

## Goal
- execution_date 개념 이해
- 날짜 기반 분석 파이프라인 설계
- 재실행(backfill)을 고려한 구조 만들기

---

## Data Scenario
- 하루 단위 분석
- execution_date 기준으로 분석 대상 날짜가 결정됨

---

## DAG Requirements
- PythonOperator 사용
- execution_date 또는 Airflow macro 사용
- Task 최소 4개 이상

---

## Mandatory Design Conditions
- 분석 대상 날짜를 하드코딩하지 말 것
- DAG 재실행 시 결과가 일관되어야 함
- 오늘 실행해도, 과거 날짜로 실행해도 의미 유지

---

## Constraints
- XCom 사용 가능
- Branch / Sensor 사용 금지

---

## Deliverables
- DAG Python 파일
- execution_date 설계 설명 MD

---

## Evaluation Criteria
- 날짜 개념이 명확히 분리되어 있는가?
- backfill 시 문제가 생기지 않는 구조인가?
- 실무에서 바로 쓸 수 있는가?
