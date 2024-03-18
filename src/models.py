from pydantic import BaseModel, EmailStr, ValidationError

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserAuth(BaseModel):
    email: EmailStr
    password: str