from pydantic import BaseModel, EmailStr, validator
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class DobModel(BaseModel):
        email: EmailStr
        dateOfBirth : datetime

        @validator("dateOfBirth")
        def validate_date_format_and_range(cls, v):
            min_date = datetime(year=1947, month=1, day=1)
            max_date = datetime.now()
            if not min_date <= v <= max_date:
                raise ValueError(f"Date must be between {min_date} and {max_date}")
            return v
