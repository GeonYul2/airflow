# Task 10 — End-to-End Analytics Automation Pipeline

## Background
이제까지 만든 모든 요소를 하나의 DAG로 통합한다.
이 DAG는 “실무 포트폴리오용 최종 산출물”이다.

---

## Goal
- 수집 → 정제 → 집계 → 검증 → 알림
- 실패 대응 및 재실행 고려
- 설명 가능한 구조 완성

---

## Data Scenario
- 외부 데이터 소스 1개 이상
- 일 단위 분석 기준

---

## DAG Requirements
- Task 최소 8개 이상
- 아래 요소 중 최소 4개 포함:
  - execution_date
  - XCom
  - Branch
  - Sensor
  - Connection/Hook
  - 알림

---

## Mandatory Design Conditions
- 재실행(backfill) 시 중복 처리 방지
- 실패 Task 재시도 전략 명시
- Task 단위 책임 명확화

---

## Deliverables
- DAG Python 파일
- 전체 파이프라인 아키텍처 설명 MD
- 운영 관점 요약 MD

---

## Evaluation Criteria
- 실무 투입이 가능한가?
- 설명 없이도 코드 구조가 읽히는가?
- 장애 대응이 설계에 포함되어 있는가?
