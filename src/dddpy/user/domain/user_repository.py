from typing import Optional
from dddpy.user.infrastructure.user import DBUser
from dddpy.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema, SearchByIdSchema


class UserRepository:
    """
    Abstract repository class for user-related operations.
    Defines the contract for interacting with the user data source, such as creating, updating, 
    searching, and removing user records. Concrete implementations must provide the logic for these methods.
    """

    # Abstract method to create a new user.
    # Accepts a `CreateUserSchema` object and returns a `DBUser` instance.
    async def create(self, user: CreateUserSchema) -> DBUser:
        raise NotImplementedError

    # Abstract method to update an existing user.
    # Accepts a user ID and an `UpdateUserSchema` object, and returns a `DBUser` instance.
    async def update(self, user_id: int, user: UpdateUserSchema) -> DBUser:
        raise NotImplementedError

    # Abstract method to remove test users created during testing.
    # Returns a boolean indicating success or failure.
    async def remove_create_tests(self) -> bool:
        raise NotImplementedError
    
    # Abstract method to search for a user by email.
    # Accepts a `SearchByEmailSchema` object and returns the result of the search.
    async def search_by_email(self, email: SearchByEmailSchema):
        raise NotImplementedError

    # Abstract method to search for a user by ID.
    # Accepts a user ID and returns the result of the search.
    async def search_by_id(self, user_id: int):
        raise NotImplementedError
