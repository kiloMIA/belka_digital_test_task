from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    disabled: bool

    class Config:
        orm_mode = True

class ReportCreate(BaseModel):
    user_id: int
    month: str
    raw_material: str
    content_of_iron: float
    content_of_sulfur: float
    content_of_silicon: float
    content_of_calcium: float
    content_of_aluminum: float

class Report(ReportCreate):
    id: int

    
    