import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "hostname": os.uname()[1]
    }
