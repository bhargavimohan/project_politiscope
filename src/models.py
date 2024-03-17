from pydantic import BaseModel, EmailStr, ValidationError

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str