from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello"}

@app.get("/api")
def read_api():
    return {"message": "good"}
