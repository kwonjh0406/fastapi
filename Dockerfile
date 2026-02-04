# Python 3.11 slim 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치를 위해 requirements.txt 복사
COPY requirements.txt .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# FastAPI 실행 (uvicorn)
# --host 0.0.0.0: 모든 인터페이스에서 접속 허용
# --port 8000: 8000번 포트 사용
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
