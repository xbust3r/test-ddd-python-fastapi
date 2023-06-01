from pydantic import BaseModel
from datetime import datetime

from typing import Optional, Dict

class GetUserSchema(BaseModel):
    id: int
    name:str
    email:str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_public: Optional[bool]=False
    
class SearchByEmailSchema(BaseModel):
    email:str
    
class SearchByIdSchema(BaseModel):
    id:str