# Airflow Study Diary - 2026-01-26

## 📅 Today's Focus
- Airflow 기초 다지기 및 완벽한 개발 환경 구축
- "내 PC(Win) - GitHub - 서버(WSL)"를 잇는 실무형 워크플로우 정립
- PythonOperator 개념 이해 및 첫 DAG 실행 성공

## 🛠️ What I Did
- **프로젝트 구조화**: `dags/`, `learning/`, `docs/` 등 시니어 수준의 폴더 구조로 리팩토링 완료.
- **문서화 시스템**: 
  - `GUIDE.md`: 대화 정보가 사라져도 즉시 복구 가능한 "맥락 저장소" 생성.
  - `docs/guides/`: 윈도우/WSL/Git 및 에어플로우 기초 치트시트 작성.
  - `qa_log.md`: 누적 질문/답변 기록장 운영 시작.
- **실습 환경 해결**: 
  - 서버(WSL)의 Git 충돌 발생 시 `git reset --hard`를 통한 강제 동기화 원리 학습.
  - 윈도우와 서버 간의 코드 배달(Push/Pull) 과정 체득.
- **Assignment 01 완료**: 3단계(Extract-Transform-Load)로 구성된 기초 파이프라인을 서버에서 성공적으로 실행.

## ❓ Questions & Issues
- **Git 관련**: `pull`이 실패했는데 왜 `reset`으로 해결됐는지? 
  - *Insight: `pull`은 가져오기(Fetch)와 합치기(Merge)의 조합이며, `reset`은 마당에 이미 와 있는 택배(Fetch된 데이터)를 강제로 뜯어서 방(Working Directory)을 갈아치우는 원리임을 배움.*

## 💡 Insights
- Airflow는 파일을 실시간으로 읽는 게 아니라 스케줄러가 "파싱"하는 주기가 있다 (약 30~60초). 수정 후 조금 기다리는 여유가 필요함.
- `PythonOperator`는 단순 함수 실행기지만, 대용량 데이터 처리에는 신중해야 함.
- 잘 정돈된 폴더 구조와 문서는 협업뿐만 아니라 AI와의 소통에서도 강력한 힘을 발휘함.
