# [강의] Airflow DAG의 가장 기본이 되는 뼈대 배우기

# 1. 아네트그라비티 시니어 에디션: 필요한 도구들 가져오기 (Import)
from airflow import DAG  # Airflow의 핵심인 DAG 객체를 만드는 클래스입니다.
from airflow.operators.python import PythonOperator  # 파이썬 함수를 실행해주는 '일꾼'입니다.
import pendulum  # Airflow에서 날짜와 시간을 다룰 때 가장 권장하는 라이브러리입니다.

# ------------------------------------------------------------------------------
# 2. 일꾼들이 실제로 해야 할 '일(함수)'을 정의합니다.
# ------------------------------------------------------------------------------

def create_raw_data():
    """
    [첫 번째 단계] 원천 데이터를 만드는 함수
    """
    # print를 쓰면 Airflow 로그 시스템에 기록되어 나중에 UI에서 확인할 수 있습니다.
    print("원천 데이터를 생성합니다...")
    data = {"date": "2026-01-27", "sales": 1000, "users": 50}
    return data  # 함수가 값을 반환하면, 나중에 XCom이라는 기능을 통해 다른 Task로 넘길 수도 있습니다.

def aggregate_data():
    """
    [두 번째 단계] 데이터를 집계하거나 계산하는 함수
    """
    print("데이터 집계를 시작합니다...")
    # 여기서 파이썬 코드로 평균을 내거나 필터링을 하는 등의 '분석' 작업을 합니다.

def print_final_result():
    """
    [세 번째 단계] 결과를 출력하거나 보고하는 함수
    """
    print("최종 분석 결과를 리포팅합니다.")

# ------------------------------------------------------------------------------
# 3. 전체 파이프라인(DAG)의 설정을 정의합니다.
# ------------------------------------------------------------------------------

with DAG(
    dag_id="assignment_01_basic_analytics",  # Airflow UI에 나타날 이 파이프라인의 '주민등록번호'입니다. 중복되면 안 됩니다.
    schedule=None,  # 주기적으로 실행할지 정합니다. None은 '내가 원할 때만 수동 실행'한다는 뜻입니다.
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Seoul"),  # 이 DAG가 언제부터 유효한지 시작점을 정합니다.
    catchup=False,  # 과거의 밀린 작업들을 한 번에 실행(Backfill)할지 여부입니다. 처음엔 False가 안전합니다.
    tags=["study", "assignment_01"],  # UI에서 필터링하기 쉽게 붙이는 라벨입니다.
) as dag:

    # --------------------------------------------------------------------------
    # 4. 각 '일(Task)'을 구체화합니다. (위에서 만든 함수와 연결)
    # --------------------------------------------------------------------------
    
    # PythonOperator는 '어떤 task_id로' + '어떤 함수(python_callable)를' 실행할지 정해주는 도구입니다.
    
    extract_task = PythonOperator(
        task_id="extract_raw_data",  # UI의 그래프 화면에 나타날 상자의 이름입니다.
        python_callable=create_raw_data  # 위에서 정의한 파이썬 함수 이름을 적어줍니다.
    )

    transform_task = PythonOperator(
        task_id="transform_aggregate_data",  # 동사 + 목적어 형태의 이름을 추천합니다.
        python_callable=aggregate_data
    )

    load_task = PythonOperator(
        task_id="load_reporting_result",
        python_callable=print_final_result
    )

    # --------------------------------------------------------------------------
    # 5. 실행 순서(의존성)를 결정합니다.
    # --------------------------------------------------------------------------
    
    # 비트 시프트 연산자(>>)를 사용하여 '순서'를 정합니다.
    # extract_task가 성공해야 transform_task가 시작되고, 그게 성공해야 load_task가 시작됩니다.
    extract_task >> transform_task >> load_task
