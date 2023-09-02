from typing import Annotated, Union
from fastapi import FastAPI, Depends
from models.usermodel import User

app = FastAPI()

@app.get("/")
def root():
    return {
        "app": "Fast Api Developer"
    }

@app.post("/register")
async def register(user: User):
    return user