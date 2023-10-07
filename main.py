import os

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "OK",
        "status": 200,
        "hostname": os.uname()[1]
    }