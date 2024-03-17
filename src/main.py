from fastapi import FastAPI,UploadFile, File
import random
import os
import asyncio
from models import Results, Session


app = FastAPI()


@app.post("/sign-up")
async def create_user():
    return {"Info" :  "Hello User"}