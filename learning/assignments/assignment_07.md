# Task 07 — Connection & Hook based Pipeline

## Background
실무에서 가장 먼저 리뷰받는 지점 중 하나는
“비밀정보를 코드에 직접 적었는가?”이다.

이번 과제는 Connection과 Hook을 사용해
운영 가능한 파이프라인 구조를 만든다.

---

## Goal
- Airflow Connection의 역할 이해
- Hook을 사용한 데이터 접근
- 코드와 환경 설정의 분리

---

## Data Scenario
- 외부 시스템에서 데이터를 읽어온다고 가정
- 예:
  - Postgres
  - API (HTTP Connection)
- 실제 DB 연결이 어렵다면 mock 또는 간단한 테스트용으로 대체 가능

---

## DAG Requirements
- PythonOperator 기반
- Task 최소 5개
- Connection 또는 Hook 반드시 1회 이상 사용

---

## Mandatory Task Roles
1. Connection을 통해 외부 자원 접근
2. 데이터 로드
3. 간단한 검증 (row 수, 필드 존재 여부 등)
4. 집계 또는 요약
5. 결과 출력 또는 저장

---

## Constraints
- 비밀정보를 코드에 하드코딩 금지
- Airflow Variable/Connection 외 다른 방식 금지
- execution_date 사용은 선택

---

## Deliverables
- DAG Python 파일
- Connection/Hooks 설계 설명 MD

---

## Evaluation Criteria
- 코드에서 환경 의존성이 제거되어 있는가?
- Connection 변경 시 코드 수정이 필요 없는가?
- 실무 배포가 가능한 구조인가?
