from dddpy.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema  # Import schemas for user creation and updates.
from dddpy.user.domain.user_repository import UserRepository  # Import the user repository interface.


class UserCmdUsecase:
    """
    Use case class for handling user command operations.
    Provides methods to create, update, and remove test users by interacting with the repository layer.
    """

    def __init__(self, user_repository: UserRepository):
        """
        Initializes the use case with a user repository.

        Args:
            user_repository (UserRepository): The repository instance for user operations.
        """
        self.user_repository = user_repository  # Repository instance for user operations.

    async def create(self, new_user: CreateUserSchema):
        """
        Creates a new user by delegating to the repository.

        Args:
            new_user (CreateUserSchema): Schema containing the new user's data.

        Returns:
            User: The created user object.
        """
        user = await self.user_repository.create(new_user)  # Call the repository to create the user.
        return user  # Return the created user.

    async def update(self, user_id: int, update_user: UpdateUserSchema):
        """
        Updates an existing user by delegating to the repository.

        Args:
            user_id (int): The ID of the user to update.
            update_user (UpdateUserSchema): Schema containing the updated user data.

        Returns:
            User: The updated user object.
        """
        user = await self.user_repository.update(user_id, update_user)  # Call the repository to update the user.
        return user  # Return the updated user.

    async def remove_create_tests(self):
        """
        Removes test users created during testing by delegating to the repository.

        Returns:
            bool: True if the operation is successful.
        """
        await self.user_repository.remove_create_tests()  # Call the repository to remove test users.
        return True  # Return success.
