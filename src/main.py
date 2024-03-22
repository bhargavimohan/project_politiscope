from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random
import os
import asyncio
from fastapi.responses import JSONResponse
from models import UserCreate,UserAuth, DobModel
from schemas import Users, Session
from passlib.context import CryptContext


app = FastAPI()
users = []

@app.post("/sign-up")
async def create_user(user: UserCreate):
    existing_user = Session.query(Users).filter(Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail=f"{user.email} is already registered")
        #return {"Message" : user.email + " is already registered"}
    #create new user
    hashed_password = pwd_context.hash(user.password)
    db_user = Users(name=user.name, email=user.email, password=hashed_password)
    # TODO : check email validation
    Session.add(db_user)
    Session.commit()
    return  user.name 

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/login")
async def authenticate_user(signedupuser: UserAuth):
    loggedIn_user = Session.query(Users).filter(Users.email == signedupuser.email).first()
    if not loggedIn_user:
        raise HTTPException(status_code=400, detail=f"{signedupuser.email} is not registered")
    # authentical pwd
    if not pwd_context.verify(signedupuser.password, loggedIn_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    return {"username" : loggedIn_user.name, "email" :loggedIn_user.email}

@app.post("/storedob")
async def store_dob_in_db(DOB : DobModel):
    user = Session.query(Users).filter_by(email=DOB.email).first()
    if user:
        # Update the date of birth (dob) for the user
        user.DOB = DOB.dateOfBirth  # Replace '1990-01-01' with the actual date of birth
        # Commit the changes
        Session.add(user)
        Session.commit()
        return "Date of birth added successfully."
    else:
        return f"User with email {DOB.dateOfBirth} not found."

        

# Add CORS middleware
# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add the HTTP methods you need
    allow_headers=["*"],  # Allow all headers
)