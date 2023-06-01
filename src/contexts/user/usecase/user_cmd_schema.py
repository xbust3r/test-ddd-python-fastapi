from pydantic import BaseModel
from typing import Optional

class CreateUserSchema(BaseModel):
    name:str="Mike"
    email:str="mike@specter.lit"
    password: str="12345"
    
class UpdateUserSchema(BaseModel):
    name:Optional[str]
    email:Optional[str]
    password: Optional[str]