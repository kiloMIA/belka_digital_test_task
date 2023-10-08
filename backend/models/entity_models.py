from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

class UserInDB(User):
    hashed_password: str

class Report(BaseModel):
    id: int
    user_id: int
    month: str
    raw_material: str
    content_of_iron: float
    content_of_sulfur: float
    content_of_silicon: float
    content_of_calcium: float
    content_of_aluminum: float
    
    