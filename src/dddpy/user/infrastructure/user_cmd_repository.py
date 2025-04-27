from dddpy.shared.mysql.base import SessionLocal
from dddpy.user.domain.user_repository import UserRepository
from dddpy.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from dddpy.shared.timezone import Timezone
from dddpy.user.infrastructure.user import DBUser
from sqlalchemy import delete
from dddpy.user.domain.user import User
from dddpy.user.infrastructure.user_query_repository import UserQueryRepositoryImpl


class UserCmdRepositoryImpl(UserRepository):
    """
    Implementation of the UserRepository interface for command operations.
    Provides methods to create, update, and remove test users in the database.
    """

    def __init__(self):
        """
        Initializes the repository with a database session.
        """
        self.repo = SessionLocal()  # Database session for executing commands.

    async def create(self, user: CreateUserSchema):
        """
        Creates a new user in the database.

        Args:
            user (CreateUserSchema): Schema containing the user's data.

        Returns:
            User: A domain-level User object representing the newly created user.
        """
        today = Timezone.get_datetime()  # Get the current datetime.
        domain_user = User(  # Create a domain-level User object.
            id=None,
            name=user.name,
            email=user.email,
            password=user.password,
            status=None,
            active_token="asd123",
            created_at=today,
            updated_at=today
        )
        new_user = User.to_dbuser(domain_user)  # Convert the domain User to a DBUser object.
        self.repo.add(new_user)  # Add the new user to the database session.
        self.repo.commit()  # Commit the transaction.
        self.repo.refresh(new_user)  # Refresh the session to get the updated user data.
        return User.from_dbuser(new_user)  # Convert the DBUser object back to a domain User object.

    async def update(self, user_id: int, user: UpdateUserSchema):
        """
        Updates an existing user in the database.

        Args:
            user_id (int): The ID of the user to update.
            user (UpdateUserSchema): Schema containing the updated user data.

        Returns:
            User or None: A domain-level User object if the update is successful, otherwise None.
        """
        db_user = await UserQueryRepositoryImpl().search_by_id(user_id)  # Search for the user by ID.

        if not db_user:  # Check if the user was not found.
            return None

        # Update the user's attributes if provided.
        if user.name:
            db_user.name = user.name
        if user.email:
            db_user.email = user.email
        if user.password:
            db_user.password = user.password

        db_user.updated_at = Timezone.get_datetime()  # Update the timestamp.
        self.repo.commit()  # Commit the transaction.

        return User.from_dbuser(db_user)  # Convert the DBUser object back to a domain User object.

    async def remove_create_tests(self):
        """
        Removes test users created during testing.

        Returns:
            bool: True if the operation is successful.
        """
        test_domain = "@qa_unitestexample.com"  # Define the test email domain.
        stmt = delete(DBUser).where(DBUser.email.like(f"%{test_domain}"))  # Create a delete statement for test users.
        self.repo.execute(stmt)  # Execute the delete statement.
        self.repo.commit()  # Commit the transaction.

        return True  # Return success.
