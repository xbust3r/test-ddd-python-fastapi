from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict
from contexts.user.infrastructure.user import DBUser


class User:
    def __init__(self, id: int, name: str, email: str, password: str, created_at: datetime, updated_at: datetime, is_public: bool = False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_public = is_public
        
    @classmethod
    def from_dbuser(cls, dbuser: DBUser):
        return cls(id=dbuser.id, name=dbuser.name, email=dbuser.email, password=dbuser.password, created_at=dbuser.created_at, updated_at=dbuser.updated_at, is_public=dbuser.is_public)

    def to_dbuser(self) -> DBUser:
        return DBUser(id=self.id, name=self.name, email=self.email, password=self.password, created_at=self.created_at, updated_at=self.updated_at, is_public=self.is_public)
