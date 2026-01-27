# Task 09 — Analytics Result Notification Pipeline

## Background
분석 자동화의 가치는
“결과를 사람이 확인할 수 있을 때” 완성된다.

이번 과제는 분석 결과를
Slack/Email 등으로 전달하는 파이프라인을 만든다.

---

## Goal
- 분석 결과 알림 자동화
- 실패/성공 알림 분리
- 메시지 내용 설계

---

## Data Scenario
- 이전 Task에서 KPI 또는 요약 결과가 생성됨
- 해당 결과를 메시지로 전달

---

## DAG Requirements
- Task 최소 5개
- 알림 Task 1개 이상 포함
- 성공/실패 알림 구분

---

## Mandatory Task Roles
1. 데이터 생성 또는 수집
2. KPI 계산
3. KPI 검증
4. 알림 메시지 생성
5. 알림 전송

---

## Constraints
- 알림 채널은 Slack 또는 Email 중 택1
- 메시지에 “의미 없는 숫자 나열” 금지
- execution_date 사용은 선택

---

## Deliverables
- DAG Python 파일
- 알림 메시지 설계 MD

---

## Evaluation Criteria
- 알림 메시지만 보고 상황 파악이 가능한가?
- 불필요한 알림이 발생하지 않는가?
- 실무에서 신뢰할 수 있는가?
