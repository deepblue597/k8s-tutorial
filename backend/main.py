import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/node")
def read_node():
    hostname = os.hostname()
    return {"Node": hostname}

