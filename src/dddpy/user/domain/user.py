from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict
from dddpy.user.infrastructure.user import DBUser


class User:
    def __init__(self, id: int, name: str, email: str, password: str, created_at: datetime, updated_at: datetime, active_token: str, status=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.active_token = active_token
        self.created_at = created_at
        self.updated_at = updated_at
        self.status= status

        
    @classmethod
    def from_dbuser(cls, dbuser: DBUser):
        return cls(
            id=dbuser.id,
            name=dbuser.name, 
            email=dbuser.email, 
            password=dbuser.password, 
            created_at=dbuser.created_at, 
            updated_at=dbuser.updated_at, 
            active_token=dbuser.active_token,
            status=dbuser.status
        )

    def to_dbuser(self) -> DBUser:
        return DBUser(
            id=self.id, 
            name=self.name, 
            email=self.email, 
            password=self.password, 
            created_at=self.created_at, 
            updated_at=self.updated_at, 
            active_token=self.active_token,
            status=self.status
        )
