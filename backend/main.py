from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"status":"ok"}

class EchoRequest(BaseModel):
    message:str

@app.post("/echo")
def eccho(req:EchoRequest):
    return {"message":req.message}