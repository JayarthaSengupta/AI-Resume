import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN")
print("FRONTEND_ORIGIN:", FRONTEND_ORIGIN)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return {"status": "ok"}


class EchoRequest(BaseModel):
    message: str


@app.post("/echo")
def echo(req: EchoRequest):
    return {"message": req.message}
