from fastapi import FastAPI

app = FastAPI()

# 設定版本號，每次想測試重新部署就改這個數字
VERSION = "v1.0.0"

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}

@app.get("/version")
def get_version():
    return {"version": VERSION}