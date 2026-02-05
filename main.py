from fastapi import FastAPI
import pymysql

app = FastAPI()

# DB 연결 정보
DB_CONFIG = {
    "host": "zones-db.c5yaia0yq0x2.ap-southeast-1.rds.amazonaws.com",
    "user": "admin",
    "password": "123456789",
    "database": "zones",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}

@app.get("/")
def read_root():
    return {"message": "hello"}

@app.get("/api")
def read_api():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        with connection.cursor() as cursor:
            # name 테이블에서 모든 정보 조회
            sql = "SELECT * FROM name"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
