# Failure Scenarios & 대응 전략

## 1. API 호출 실패

### 원인
- 네트워크 오류
- Rate limit 초과
- 일시적 서버 장애

### 대응
- retries 설정
- retry_delay 설정
- 실패 시 알림 전송
- 멱등성 고려 (중복 수집 방지)

---

## 2. API 응답 스키마 변경

### 원인
- 필드 추가/삭제
- 타입 변경

### 대응
- 필드 존재 여부 검증 Task 추가
- 필수 필드 누락 시 DAG 실패
- 스키마 변경 감지 로그 남기기

---

## 3. Backfill 실행 시 문제

### 원인
- 과거 데이터 재처리
- 중복 데이터 생성

### 대응
- execution_date 기반 경로 분리
- 동일 날짜 데이터 overwrite 또는 skip 정책 명시
- backfill 전 dry-run 검토

---

## 4. 멱등성(Idempotency) 문제

### 원인
- 동일 DAG 재실행 시 결과 누적

### 대응
- 날짜 기반 파티션 사용
- insert 전에 delete or overwrite
- Task 재실행 시 동일 결과 보장

---

## 5. Sensor 무한 대기

### 원인
- 조건이 절대 만족되지 않음

### 대응
- timeout 명시
- 실패 시 알림
- reschedule mode 고려

---

## 6. 알림 폭주

### 원인
- 잦은 실패
- 불필요한 경고 기준

### 대응
- 알림 조건 명확화
- critical 이벤트만 알림
- 요약 알림 사용
