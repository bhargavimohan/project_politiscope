from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., case_sensitive=False)
    email: EmailStr
    password: str