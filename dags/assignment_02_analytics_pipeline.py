import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

# [강의] Assignment 02: XCom을 활용한 실제 데이터 전달(Pull) 배우기
# 핵심: 앞선 작업(Task)이 던진(Push) 데이터를 어떻게 받아올(Pull) 것인가?

def extract_data():
    """1단계: 원천 데이터 수집 (Push)"""
    print("원천 데이터를 생성합니다...")
    # return을 하면 자동으로 XCom에 'return_value'라는 이름으로 저장됩니다.
    return [
        {"id": 1, "name": "Apple", "price": 1000},
        {"id": 2, "name": "Banana", "price": 500},
        {"id": 3, "name": "Cherry", "price": None}, # 결측치 포함
        {"id": 4, "name": "Date", "price": 1200}
    ]

def clean_data(**context):
    """2단계: 데이터 정제 (Pull & Push)"""
    # ti(task_instance)를 통해 이전 Task의 결과물을 가져옵니다.
    ti = context['ti']
    raw_data = ti.xcom_pull(task_ids='extract_raw_data')
    
    print(f"가져온 원본 데이터: {raw_data}")
    
    # 가격이 없는(None) 항목을 제거하는 정제 로직
    cleaned_data = [item for item in raw_data if item['price'] is not None]
    
    print(f"정제된 데이터: {cleaned_data}")
    return cleaned_data

def aggregate_data(**context):
    """3단계: 집계 계산 (Pull & Push)"""
    ti = context['ti']
    cleaned_data = ti.xcom_pull(task_ids='refine_cleaned_data')
    
    total_price = sum(item['price'] for item in cleaned_data)
    avg_price = total_price / len(cleaned_data)
    
    result = {"total": total_price, "average": avg_price}
    print(f"집계 결과: {result}")
    return result

def report_summary(**context):
    """4단계: 최종 리포팅 (Pull)"""
    ti = context['ti']
    agg_result = ti.xcom_pull(task_ids='aggregate_calculation')
    
    print("===== 최종 분석 리포트 =====")
    print(f"오늘의 총 매출액: {agg_result['total']}원")
    print(f"평균 단가: {agg_result['average']}원")
    print("==========================")

with DAG(
    dag_id="assignment_02_analytics_pipeline",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["study", "assignment_02", "xcom"],
) as dag:

    # 1. Raw Data 생성
    extract = PythonOperator(
        task_id="extract_raw_data",
        python_callable=extract_data
    )

    # 2. 데이터 정제 (clean)
    refine = PythonOperator(
        task_id="refine_cleaned_data",
        python_callable=clean_data
        # **context를 쓰려면 별도의 설정 없이 PythonOperator가 자동으로 넘겨줍니다.
    )

    # 3. 집계 (aggregation)
    aggregate = PythonOperator(
        task_id="aggregate_calculation",
        python_callable=aggregate_data
    )

    # 4. 분석 결과 요약 (report)
    report = PythonOperator(
        task_id="report_final_summary",
        python_callable=report_summary
    )

    # 파이프라인 연결: 데이터의 흐름 순서대로!
    extract >> refine >> aggregate >> report
