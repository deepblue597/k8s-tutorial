import socket
from fastapi import FastAPI
from fastapi  import WebSocket
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/node")
def read_node():
    hostname = socket.gethostname()
    return {"Node": hostname}

