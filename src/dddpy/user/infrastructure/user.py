from sqlalchemy import Column, Integer, DateTime, Boolean, BigInteger, String

from dddpy.shared.mysql.base import Base


class DBUser(Base):
    """
    Represents the database model for a user.
    Maps the `users` table in the database to a Python object, allowing ORM-based interactions.
    """

    # Table name in the database.
    __tablename__ = "users"

    # Column 'id': Primary key, auto-incremented, and indexed.
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    # Column 'name': Stores the user's name as a string (max length 120).
    name = Column(String(120))

    # Column 'email': Stores the user's email as a string (max length 220).
    email = Column(String(220))

    # Column 'password': Stores the user's password as a string (max length 255).
    password = Column(String(255))

    # Column 'created_at': Stores the timestamp when the user was created. Cannot be null.
    created_at = Column(DateTime, nullable=False)

    # Column 'updated_at': Stores the timestamp when the user was last updated. Cannot be null.
    updated_at = Column(DateTime, nullable=False)

    # Column 'active_token': Stores the user's active token as a string (max length 255).
    active_token = Column(String(255))

    # Column 'auth_token': Stores the user's authentication token as a string (max length 255).
    auth_token = Column(String(255))

    # Column 'refresh_token': Stores the user's refresh token as a string (max length 255).
    refresh_token = Column(String(255))

    # Column 'status': Stores the user's status as a boolean. Defaults to False.
    status = Column(Boolean, default=False)

    def as_dict(self):
        """
        Converts the DBUser instance into a dictionary representation.

        Returns:
            dict: A dictionary containing the user's id, name, email, created_at, and updated_at.
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

