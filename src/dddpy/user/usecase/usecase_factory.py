from dddpy.user.usecase.user_cmd_usecase import UserCmdUsecase  # Import the command use case for user operations.
from dddpy.user.usecase.user_query_usecase import UserQueryUsecase  # Import the query use case for user operations.
from dddpy.user.infrastructure.user_cmd_repository import UserCmdRepositoryImpl  # Import the command repository implementation.
from dddpy.user.infrastructure.user_query_repository import UserQueryRepositoryImpl  # Import the query repository implementation.

# Factory function to create an instance of UserCmdUsecase.
def user_cmd_usecase():
    """
    Creates and returns an instance of UserCmdUsecase.

    Returns:
        UserCmdUsecase: The use case for handling user command operations.
    """
    user_cmd_repository = UserCmdRepositoryImpl()  # Initialize the command repository implementation.
    return UserCmdUsecase(user_cmd_repository)  # Return the use case with the repository injected.

# Factory function to create an instance of UserQueryUsecase.
def user_query_usecase():
    """
    Creates and returns an instance of UserQueryUsecase.

    Returns:
        UserQueryUsecase: The use case for handling user query operations.
    """
    user_query_repository = UserQueryRepositoryImpl()  # Initialize the query repository implementation.
    return UserQueryUsecase(user_query_repository)  # Return the use case with the repository injected.