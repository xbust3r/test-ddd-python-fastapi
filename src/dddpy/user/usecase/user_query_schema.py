from pydantic import BaseModel  # Import Pydantic for data validation and parsing.
from datetime import datetime  # Import for handling date and time.
from typing import Optional, Dict  # Import for optional type annotations and dictionaries.

class GetUserSchema(BaseModel):
    """
    Schema for retrieving user details.
    Defines the fields returned when fetching user data, including optional timestamps.
    """

    # Field 'id': The unique identifier of the user.
    id: int

    # Field 'name': The name of the user.
    name: str

    # Field 'email': The email address of the user.
    email: str

    # Field 'created_at': The timestamp when the user was created. Optional.
    created_at: Optional[datetime]

    # Field 'updated_at': The timestamp when the user was last updated. Optional.
    updated_at: Optional[datetime]
    
    
class SearchByEmailSchema(BaseModel):
    """
    Schema for searching a user by email.
    Defines the required field for performing a search operation using an email address.
    """

    # Field 'email': The email address to search for.
    email: str
    
class SearchByIdSchema(BaseModel):
    """
    Schema for searching a user by ID.
    Defines the required field for performing a search operation using a user ID.
    """

    # Field 'id': The unique identifier of the user to search for.
    id: str