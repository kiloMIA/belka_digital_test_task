from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    
class Report(BaseModel):
    id: int
    user_id: int
    raw_material: str
    content_of_iron: int
    content_of_sulfur: int
    content_of_silicon: int
    content_of_calcium: int
    content_of_aluminum: int
    
    