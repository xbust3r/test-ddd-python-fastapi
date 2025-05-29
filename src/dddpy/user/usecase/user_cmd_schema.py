from pydantic import BaseModel  # Import Pydantic for data validation and parsing.
from typing import Optional  # Import for optional type annotations.

class CreateUserSchema(BaseModel):
    """
    Schema for creating a user.
    Defines the required fields and their default values for creating a new user.
    """

    # Field 'name': The name of the user. Default value is "Mike".
    name: str = "Mike"

    # Field 'email': The email address of the user. Default value is "mike@specter.lit".
    email: str = "mike@specter.lit"

    # Field 'password': The password of the user. Default value is "12345".
    password: str = "12345"
    
class UpdateUserSchema(BaseModel):
    """
    Schema for updating a user.
    Defines optional fields that can be updated for an existing user.
    """

    # Field 'name': The updated name of the user. Optional.
    name: Optional[str] = None

    # Field 'email': The updated email address of the user. Optional.
    email: Optional[str] = None

    # Field 'password': The updated password of the user. Optional.
    password: Optional[str] = None