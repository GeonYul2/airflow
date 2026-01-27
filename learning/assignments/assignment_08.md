# Task 08 — Sensor-based Dependency Waiting

## Background
실무 DAG는 대부분 “기다리는 시간”이 포함된다.
예:
- 파일이 도착할 때까지
- 외부 시스템 처리가 끝날 때까지

이번 과제는 Sensor를 사용해
의존성을 명시적으로 표현하는 연습이다.

---

## Goal
- Sensor의 필요성을 이해
- 불필요한 polling 방지
- DAG 리소스 낭비 최소화

---

## Data Scenario
- 외부 파일 또는 외부 Task가 준비되어야 다음 단계 실행
- FileSensor 또는 PythonSensor 사용

---

## DAG Requirements
- Task 최소 5개
- Sensor Task 1개 이상 필수
- Sensor 이후 실제 처리 Task 존재

---

## Mandatory Design Conditions
- Sensor timeout 설정 명시
- poke_interval 또는 reschedule mode 고려

---

## Constraints
- Branch 사용 금지
- 외부 API 호출은 선택
- execution_date 사용은 선택

---

## Deliverables
- DAG Python 파일
- Sensor 설계 설명 MD
  - 왜 Sensor가 필요한가?
  - Sensor가 실패하면 어떻게 되는가?

---

## Evaluation Criteria
- Sensor가 과하지 않은가?
- 기다림을 코드로 우회하지 않았는가?
- 실무 리소스 관점에서 안전한가?
