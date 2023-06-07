from sqlalchemy import Column, Integer, DateTime, Boolean, BigInteger, String

from dddpy.shared.mysql.base import Base


class DBUser(Base):

    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120))
    email = Column(String(220))
    password = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    active_token=Column(String(255))
    auth_token=Column(String(255))
    refresh_token=Column(String(255))
    status=Column(Boolean, default=False)
    
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

