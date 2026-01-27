# Task 02 — PythonOperator-based Analytics Pipeline

## Background
이제 단순한 DAG를 넘어서,
“분석 파이프라인”다운 구조를 설계해야 한다.

Task 01과 달리,
각 Task는 **명확한 분석 단계**를 나타내야 한다.

---

## Goal
- PythonOperator 중심의 분석 파이프라인 설계
- Task 단위 책임 분리
- 코드 재사용 가능성 고려

---

## Data Scenario
- 하루치 로그 또는 이벤트 데이터가 있다고 가정
- Python 함수 내부에서 리스트 또는 dict 형태로 생성

---

## DAG Requirements
- PythonOperator만 사용
- Task 최소 4개 이상
- Task 간 데이터 흐름이 자연스러워야 함

---

## Mandatory Task Roles
아래 역할은 반드시 포함할 것:

1. Raw Data 생성
2. 데이터 정제
3. 집계 (aggregation)
4. 분석 결과 요약

---

## Constraints
- XCom 사용 가능
- execution_date 사용 금지
- Branch / Sensor 사용 금지

---

## Deliverables
- DAG Python 파일
- 각 Task의 역할을 설명하는 MD 문서

---

## Evaluation Criteria
- Task 이름만 보고 역할이 유추되는가?
- 한 Task가 너무 많은 일을 하고 있지는 않은가?
- 이 구조를 내일 다른 분석에 재사용할 수 있는가?
