from pydantic import BaseModel  # For data validation and parsing.
from datetime import datetime  # For handling date and time.
from typing import Optional, Dict  # For optional types and dictionaries.
from dddpy.user.infrastructure.user import DBUser  # Infrastructure-level user model.


class User:
    """
    Represents a user in the domain layer.
    Encapsulates user-related data and logic, and provides methods for converting
    between the domain model (`User`) and the infrastructure model (`DBUser`).
    """

    def __init__(self, id: int, name: str, email: str, password: str, created_at: datetime, updated_at: datetime, active_token: str, status=None):
        """
        Initializes a User instance.

        Args:
            id (int): Unique identifier for the user.
            name (str): The user's name.
            email (str): The user's email address.
            password (str): The user's password.
            created_at (datetime): The timestamp when the user was created.
            updated_at (datetime): The timestamp when the user was last updated.
            active_token (str): The active token associated with the user.
            status (Optional): The user's status (default is None).
        """
        self.id = id  # Unique identifier for the user.
        self.name = name  # The user's name.
        self.email = email  # The user's email address.
        self.password = password  # The user's password.
        self.active_token = active_token  # The active token associated with the user.
        self.created_at = created_at  # Timestamp of user creation.
        self.updated_at = updated_at  # Timestamp of the last user update.
        self.status = status  # Optional user status.

    @classmethod
    def from_dbuser(cls, dbuser: DBUser):
        """
        Creates a User instance from a DBUser object.

        Args:
            dbuser (DBUser): The infrastructure-level user object.

        Returns:
            User: A domain-level User instance.
        """
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
        """
        Converts the User instance into a DBUser object.

        Returns:
            DBUser: An infrastructure-level user object.
        """
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
