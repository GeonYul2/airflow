# ✈️ Airflow Core Concept Cheat Sheet

에어플로우 문법의 핵심 요소를 정리한 가이드입니다.

---

## 🧩 핵심 구성 요소
- **DAG (Directed Acyclic Graph)**: 전체 파이프라인(워크플로우) 그 자체.
- **Task**: 파이프라인 안의 개별 작업 하나하나. (UI의 네모 상자)
- **Operator**: Task를 실제로 수행하는 '일꾼'의 종류 (예: PythonOperator).

## 📝 필수 코드 문법
### 1. DAG 정의하기
```python
with DAG(
    dag_id="이름",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
```

### 2. PythonOperator 만들기
```python
task_name = PythonOperator(
    task_id="상자_이름",
    python_callable=파이썬_함수_이름
)
```

### 3. 순서 정하기 (의존성)
- `t1 >> t2`: t1이 끝난 후 t2 실행
- `t1 >> [t2, t3]`: t1이 끝나면 t2, t3 동시 실행

## 🛑 주의사항
- **dag_id**는 중복되면 안 됩니다.
- **PythonOperator**로 실행할 함수에 괄호를 붙이지 마세요. (`python_callable=fn_name` (O), `fn_name()` (X))
- 대용량 데이터는 **PythonOperator**가 아닌 SQL이나 외부 엔진에 맡기세요.
