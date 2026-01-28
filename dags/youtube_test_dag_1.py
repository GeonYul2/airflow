from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

log = logging.getLogger(__name__)

# ✅ Docker/Airflow 컨테이너 기준 기본값
# docker-compose에서 PROJECT_PATH=/opt/airflow/project 로 넣어둔 상태를 전제
PROJECT_PATH = os.environ.get("PROJECT_PATH", "/opt/airflow/project")

# config / output 경로
CONFIG_PATH = os.environ.get("CONFIG_PATH", os.path.join(PROJECT_PATH, "config", "config.yaml"))
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", os.path.join(PROJECT_PATH, "output"))


def _bootstrap_project() -> None:
    """프로젝트 경로/설정 파일 존재 확인 + import 경로 세팅"""
    project_dir = Path(PROJECT_PATH)

    if not project_dir.is_dir():
        raise FileNotFoundError(
            f"PROJECT_PATH not found: {PROJECT_PATH}\n"
            f"docker-compose에서 프로젝트 볼륨 마운트가 되어있는지 확인하세요."
        )

    config_file = Path(CONFIG_PATH)
    if not config_file.is_file():
        raise FileNotFoundError(
            f"Config not found: {CONFIG_PATH}\n"
            f"예: {PROJECT_PATH}/config/config.yaml"
        )

    # ✅ 'from src.xxx import ...'가 되려면 루트(PROJECT_PATH)가 sys.path에 있어야 함
    project_root = str(project_dir.resolve())
    if project_root not in sys.path:
        sys.path.insert(0, project_root)


def youtube_test_task() -> None:
    _bootstrap_project()

    # 프로젝트 내부 모듈 import
    from src.monitor import get_latest_videos
    from src.transcript import get_transcript
    from src.generator import generate_prompt_file

    import yaml  # 컨테이너에 pyyaml 설치돼 있어야 함

    # Load config
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    try:
        channel_id = config["youtube"]["channel_id"]
    except Exception as e:
        raise KeyError(f"Missing config key: youtube.channel_id in {CONFIG_PATH}") from e

    log.info("TEST: Fetching 2 latest videos from channel: %s", channel_id)
    videos = get_latest_videos(channel_id, count=2)

    if not videos:
        log.info("No videos found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for video_info in videos:
        title = video_info.get("title")
        vid = video_info.get("id")

        log.info("Processing Test Video: %s (%s)", title, vid)

        transcript = get_transcript(vid)
        if not transcript:
            log.warning("FAILED: No transcript for %s", vid)
            continue

        result_path = generate_prompt_file(
            vid,
            title,
            transcript,
            output_dir=OUTPUT_DIR,
        )
        log.info("SUCCESS: Generated test prompt file: %s", result_path)


with DAG(
    dag_id="youtube_summary_TEST_DAG",
    default_args={"retries": 0},
    description="TEST DAG: Fetches 2 latest videos regardless of history",
    schedule=None,  # ✅ Airflow 3.x: 수동 실행 전용
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["test", "youtube"],
) as dag:
    test_run = PythonOperator(
        task_id="fetch_2_latest_videos_test",
        python_callable=youtube_test_task,
    )
