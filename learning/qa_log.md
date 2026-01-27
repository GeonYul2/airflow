# Airflow Study Master QA Log

이 파일은 `GUIDE.md`의 협업 수칙에 따라 에어플로우 학습 과정에서의 **핵심 Q&A**를 영구적으로 기록하는 마스터 로그입니다.

---

## [2026-01-27] Airflow Plugins 폴더 생성 및 Docker Compose 연동

**질문**: plugins 폴더 하나 만들어줘. 그리고 docker-compose.yaml 파일에서 경로 수정하는 방법도 알려줘.

**답변**: 에어플로우 확장을 위한 핵심적인 설정입니다. 단계별로 정리해 드립니다.

### 1. Plugins 폴더 생성
- 프로젝트 루트(`C:\vscode\airflow\plugins`)에 폴더를 생성하였습니다.
- 커스텀 Operator, Hook 등을 이 폴더에 넣으면 Airflow가 컨테이너 시작 시 자동으로 로드합니다.

### 2. Docker Compose 경로 수정 (볼륨 마운트)
Docker 컨테이너가 로컬의 `plugins` 폴더를 인식하게 하려면 `docker-compose.yaml`의 `volumes` 섹션을 다음과 같이 수정해야 합니다.

```yaml
volumes:
  - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
  - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
  - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins  # 이 줄을 추가하여 로컬-컨테이너를 연결합니다.
```

### 3. 반영 방법
설정 수정 후에는 변경 사항을 적용하기 위해 컨테이너를 재시작해야 합니다.
```bash
sudo docker compose down
sudo docker compose up -d
```

> [!TIP]
> 관련 기술 상세 가이드는 [docker_setup.md](file:///C:/vscode/airflow/docs/guides/docker_setup.md)에 별도로 문서화하였습니다.
