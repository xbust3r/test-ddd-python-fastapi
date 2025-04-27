from dddpy.shared.mysql.base import SessionLocal
from dddpy.user.domain.user_repository import UserRepository
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema
from dddpy.user.infrastructure.user import DBUser
from dddpy.user.domain.user import User


class UserQueryRepositoryImpl(UserRepository):
    """
    Implementation of the UserRepository interface for querying user data.
    Provides methods to search for users in the database by email or ID.
    """

    def __init__(self):
        """
        Initializes the repository with a database session.
        """
        self.repo = SessionLocal()  # Database session for querying user data.

    async def search_by_email(self, email: SearchByEmailSchema):
        """
        Searches for a user in the database by email.

        Args:
            email (SearchByEmailSchema): Schema containing the email to search for.

        Returns:
            User or None: A domain-level User object if found, otherwise None.
        """
        db_user = self.repo.query(DBUser).filter(DBUser.email == email.email).first()  # Query the database for the user.

        if db_user is None:  # Check if the user was not found.
            return None

        return User.from_dbuser(db_user)  # Convert the DBUser object to a domain-level User object.

    async def search_by_id(self, user_id: int):
        """
        Searches for a user in the database by ID.

        Args:
            user_id (int): The ID of the user to search for.

        Returns:
            User or None: A domain-level User object if found, otherwise None.
        """
        user = self.repo.query(DBUser).filter(DBUser.id == user_id).first()  # Query the database for the user.

        if not user:  # Check if the user was not found.
            return None

        return User.from_dbuser(user)  # Convert the DBUser object to a domain-level User object.
