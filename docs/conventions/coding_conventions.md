# Airflow Coding Conventions

## 1. DAG & 파일 네이밍

- DAG 파일명: snake_case
  - 예: daily_sales_aggregation_dag.py
- DAG ID:
  - 환경/목적/주기 포함
  - 예: analytics_daily_sales_pipeline

---

## 2. task_id 네이밍 규칙

- 동사 + 목적어 구조 사용
- 의미 없는 숫자/약어 금지

### Good
- load_raw_events
- clean_event_data
- calculate_daily_kpi
- send_slack_notification

### Bad
- task1
- process_data
- run_step

---

## 3. Task 책임 원칙

- 하나의 Task = 하나의 책임
- 한 Task에서 아래를 동시에 하지 말 것:
  - 데이터 로드 + 집계
  - 검증 + 알림

---

## 4. Logging 규칙

- print 사용 금지
- logging 모듈 사용

### Logging Level 가이드
- INFO: 정상 흐름, 요약 정보
- WARNING: 비정상 가능성
- ERROR: Task 실패 직전

---

## 5. XCom 사용 규칙

- 작은 값만 전달 (int, float, dict 요약)
- DataFrame, list 전체 전달 금지
- XCom이 필요 없으면 사용하지 않는다

---

## 6. execution_date 사용 규칙

- 하드코딩 금지
- 템플릿 또는 macro 사용
- 분석 대상 날짜와 실행 날짜를 구분한다

---

## 7. 파일 저장 경로 규칙 (로컬 기준)

- Raw: /data/raw/{date}/
- Clean: /data/clean/{date}/
- Output: /data/output/{date}/

날짜는 execution_date 기준으로 생성
