from sqlalchemy import Column, Integer, DateTime, Boolean, BigInteger, String

from contexts.shared.mysql.base import Base


class DBUser(Base):

    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120))
    email = Column(String(220))
    email_verified_at = Column(String(220))
    password = Column(String(255))
    remember_token = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    token_type= Column(Integer)
    auth_token=Column(String(255))
    is_public=Column(Boolean)
    
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "is_public": self.is_public,
        }
