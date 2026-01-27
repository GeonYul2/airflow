# 🐧 WSL & 🐙 Git Cheat Sheet

이 문서는 Airflow 학습 과정에서 가장 자주 사용하는 명령어들을 정리한 가이드입니다.

---

## 📂 폴더 이동 및 확인 (WSL)
- `pwd`: 현재 내가 어느 폴더에 있는지 확인
- `ls`: 현재 폴더에 있는 파일 목록 보기
- `ls -al`: 숨겨진 파일까지 자세히 보기
- `cd [폴더명]`: 특정 폴더로 들어가기
- `cd ..`: 상위 폴더로 나가기
- `cd /c/vscode/airflow/airflow`: 윈도우 작업 폴더로 바로 이동 (C드라이브 기준)

## 🚢 Git 코드 동기화 (내 PC -> 원격 서버)
1. `git status`: 현재 바뀐 파일이 무엇인지 확인
2. `git add .`: 변경된 모든 파일을 보낼 바구니에 담기
3. `git commit -m "메시지"`: 바구니에 이름표 붙이기
4. `git push`: 원격 서버(수업 서버)로 보내기

## 🚀 Airflow 실행 (가상환경 내)
1. `source .venv/bin/activate`: 가상환경 켜기
2. `airflow standalone`: 에어플로우 서버 켜기 (ID/PW 터미널 확인)
3. `airflow version`: 에어플로우 버전 확인

---
> [!TIP]
> 명령어 앞 글자만 치고 `Tab` 키를 누르면 자동 완성됩니다!
