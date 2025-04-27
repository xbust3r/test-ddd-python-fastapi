from dddpy.shared.mysql.base import SessionLocal  # Import for database session handling.
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema  # Import schema for searching by email.
from dddpy.user.domain.user_repository import UserRepository  # Import the user repository interface.
from dddpy.user.infrastructure.user_query_repository import UserQueryRepositoryImpl  # Import the query repository implementation.


class UserQueryUsecase:
    """
    Use case class for handling user query operations.
    Provides methods to search for users by email or ID by interacting with the repository layer.
    """

    def __init__(self, user_repository: UserRepository):
        """
        Initializes the use case with a user repository.

        Args:
            user_repository (UserRepository): The repository instance for user query operations.
        """
        self.user_repository = user_repository  # Repository instance for user query operations.

    async def search_by_email(self, email: SearchByEmailSchema):
        """
        Searches for a user by email.

        Args:
            email (SearchByEmailSchema): Schema containing the email to search for.

        Returns:
            User or None: The user object if found, otherwise None.
        """
        return await self.user_repository.search_by_email(email)  # Delegate the search to the repository.

    async def search_by_id(self, user_id: int):
        """
        Searches for a user by ID.

        Args:
            user_id (int): The ID of the user to search for.

        Returns:
            User or None: The user object if found, otherwise None.
        """
        return await self.user_repository.search_by_id(user_id)  # Delegate the search to the repository.
