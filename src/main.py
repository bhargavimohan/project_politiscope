from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import os
import asyncio
from fastapi.responses import JSONResponse
from models import UserCreate,ValidationError
from schemas import Users, Session


app = FastAPI()
users = []

@app.post("/sign-up")
async def create_user(user: UserCreate):
    db_user = Users(name=user.name, email=user.email, password=user.password)
    #TODO
    #1.insert user if not already registered
    # check email validation
    Session.add(db_user)
    Session.commit()
    return {"Message" : "New user : " + user.name + " is created"}
        

# Add CORS middleware
# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add the HTTP methods you need
    allow_headers=["*"],  # Allow all headers
)