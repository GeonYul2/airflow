# 🌐 Project Global Guide (Context Keeper)

이 파일은 대화 내용이 초기화되어도 안티그래비티(AI)가 사용자님의 현재 환경과 학습 맥락을 즉시 파악할 수 있도록 돕는 "기억 저장소"입니다.

---

## 🏗️ 1. 현재 환경 설정 (Current Environment)
- **OS**: Windows (Local) + WSL (Ubuntu)
- **Sync**: Git Push/Pull 기반 원격 서버 동기화
- **Editor**: VS Code (Remote-WSL 활용)
- **Airflow**: Docker Container 기반 운영 중
- **명령어**: 서버 실행 시 `sudo docker compose up` (또는 `airflow standalone`)

## 📂 2. 프로젝트 구조 (Project Structure)
- `dags/`: 실제 실행될 DAG 파일들
- `learning/`: 학습 전용 공간
  - `assignments/`: 과제 01-10
  - `diary/`: 매일의 학습 기록 및 에셋(assets/)
  - `qa_log.md`: 핵심 Q&A 세션 기록
- `docs/`: 각종 참조 문서
  - `guides/`: WSL/Git, Airflow 치트시트
  - `conventions/`: 코딩 규칙 및 장애 대응
  - `templates/`: 설명/리뷰 요청 템플릿

## 🤝 3. 협업 수칙 (Working Rules)
1. **AI의 역할**: 시니어 데이터 엔지니어로서 코드 설계, 리팩토링, 개념 설명을 담당함.
2. **코드 반영**: AI가 `dags/` 등에 코드를 작성하면, 사용자가 이를 검토 후 **Git Push -> Remote Pull** 하여 반영함.
3. **학습 기록**: 모든 새로운 가이드는 `docs/guides/`에, 질문은 `qa_log.md`에, 매일의 기록은 `diary/`에 남겨 맥락을 유지함.

---
> [!IMPORTANT]
> **대화가 초기화되었을 때**: 안티그래비티에게 "GUIDE.md 파일을 읽어줘"라고 말하면 모든 맥락이 즉시 복원됩니다.
