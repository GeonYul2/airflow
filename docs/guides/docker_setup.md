# Plugins 폴더 생성 및 Docker Compose 볼륨 설정 가이드

## 1. Plugins 폴더 생성 완료
프로젝트 루트 경로(`C:\vscode\airflow\plugins`)에 `plugins` 폴더가 생성되었음을 확인했습니다. 커스텀 Operator, Hook, Sensor 등을 이 폴더에 저장하여 Airflow 기능을 확장할 수 있습니다.

## 2. docker-compose.yaml 수정 방법
Docker 컨테이너가 로컬 컴퓨터의 `plugins` 폴더를 인식(마운트)하게 하려면, `docker-compose.yaml` 파일의 `volumes` 섹션을 수정해야 합니다.

### 설정 단계:
1. `docker-compose.yaml` 파일을 엽니다.
2. `x-airflow-common` (또는 개별 서비스 정의) 아래의 `volumes` 섹션을 찾습니다.
3. 아래와 같이 로컬의 `plugins` 경로를 컨테이너의 `/opt/airflow/plugins` 경로와 연결하는 줄을 추가합니다.

```yaml
volumes:
  - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
  - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
  - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins  # <--- 이 줄을 추가하세요
```

### 경로 설명:
- `${AIRFLOW_PROJ_DIR:-.}/plugins`: **호스트(로컬 PC 또는 WSL)** 내의 프로젝트 폴더에 있는 `plugins` 폴더를 가리킵니다.
- `/opt/airflow/plugins`: **Docker 컨테이너 내부**에서 Airflow가 플러그인을 찾는 기본 경로입니다.

> [!NOTE]
> 만약 윈도우 루트 폴더(`C:\vscode\airflow`)에서 `docker-compose.yaml` 파일을 찾을 수 없다면, WSL 홈 디렉토리(`~/`)에 해당 파일이 위치해 있을 가능성이 높습니다. `nano ~/docker-compose.yaml` 명령어로 편집하거나 VS Code에서 해당 경로를 열어 수정해 주세요.

## 3. 변경 사항 반영
파일을 저장한 후, 설정을 적용하려면 Docker 컨테이너를 재시작해야 합니다.
```bash
sudo docker compose down
sudo docker compose up -d
```
