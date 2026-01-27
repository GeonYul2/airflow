# Task 06 — External API Ingestion (HTTP → Raw → Clean)

## Background
이제부터는 실무에서 가장 흔한 형태:
외부 API에서 데이터를 받아 Raw로 저장하고,
간단히 정제한 결과를 만든다.

이번 과제는 “수집 자동화”의 최소 형태를 만든다.

---

## Goal
- API 호출 → Raw 저장 → 정제 → 요약 까지의 흐름 설계
- 실패/재시도 고려
- (가능하면) Connection을 쓰는 습관 만들기

---

## Data Scenario
- 공개 API 또는 테스트용 API 사용
- 예시:
  - https://jsonplaceholder.typicode.com/
  - 임의의 공공 API
- 응답 JSON을 Raw로 저장한 뒤, 필요한 필드만 추출해 Clean 결과 생성

---

## DAG Requirements
- Task 최소 6개
- HTTP 호출 Task 포함 (Python requests 사용 가능)
- Raw 저장 Task 포함
- Clean 데이터 생성 Task 포함
- 최종 요약 출력 Task 포함 (예: 레코드 수, 특정 필드 빈도)

---

## Mandatory Design Conditions
- API URL을 코드에 하드코딩하더라도,
  토큰/키가 필요하면 반드시 Airflow Variable 또는 Connection을 사용
- 실패 시 재시도 설정을 명시할 것 (retries, retry_delay 등)

---

## Constraints
- Sensor 사용 금지 (다음 과제에서 다룸)
- Branch는 선택
- execution_date 사용은 선택 (해도 됨, 하지만 주 목적은 수집 자동화)

---

## Deliverables
- DAG Python 파일
- 운영 관점 메모 MD:
  - rate limit 발생 시 대응
  - 응답 스키마 변경 시 대응
  - 재처리(backfill) 전략 초안
