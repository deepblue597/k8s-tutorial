import socket
from fastapi import FastAPI
from fastapi  import WebSocketimport 
import uvicorn
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/node")
def read_node():
    hostname = socket.gethostname()
    return {"Node": hostname}

if __name__ == "__main__":
    print("Starting server on http://127.0.0.1:8009")
    uvicorn.run(app, host="127.0.0.1", port=8009)