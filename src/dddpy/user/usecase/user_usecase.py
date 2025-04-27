from dddpy.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema  # Import schemas for user creation and updates.
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema  # Import schema for searching by email.

from dddpy.shared.schemas.response_schema import ResponseSuccessSchema  # Import schema for successful responses.
from dddpy.shared.utils.validate_email import validate_email  # Import utility for email validation.
from dddpy.shared.utils.password import password  # Import utility for password handling.

from dddpy.user.domain.user_exception import EmailExistError, EmailInvalidError, PasswordWeakError, UserNotFoundError, EmailNotFound  # Import custom exceptions.
from dddpy.user.domain.user_success import SuccessMessages  # Import predefined success messages.
from dddpy.user.domain.user_validation import CreateUserValidationSchema, UpdateUserValidationSchema  # Import validation schemas.

from marshmallow.exceptions import ValidationError  # Import exception for validation errors.

from dddpy.user.usecase.usecase_factory import user_cmd_usecase, user_query_usecase  # Import factory functions for use cases.


class UserUsecase:
    """
    Use case class for handling user-related operations.
    Provides methods for creating, updating, searching, and removing test users by interacting with the command and query use cases.
    """

    def __init__(self):
        """
        Initializes the use case with command and query use cases.
        """
        self.user_cmd = user_cmd_usecase()  # Command use case for user operations.
        self.user_query = user_query_usecase()  # Query use case for user operations.

    async def create_user(self, user: CreateUserSchema):
        """
        Creates a new user after validating the input data.

        Args:
            user (CreateUserSchema): Schema containing the user's data.

        Returns:
            ResponseSuccessSchema: A success response with the created user data.
        """
        search_email = SearchByEmailSchema(email=user.email)  # Prepare schema for email search.
        check_email = await self.user_query.search_by_email(search_email)  # Check if the email already exists.
        valid_email = validate_email(user.email)  # Validate the email format.

        if not valid_email:
            raise EmailInvalidError()  # Raise an error if the email is invalid.
        if check_email:
            raise EmailExistError()  # Raise an error if the email already exists.
        if password.check_policies(user.password):
            raise PasswordWeakError()  # Raise an error if the password is weak.

        schema = CreateUserValidationSchema()  # Initialize the validation schema.

        try:
            schema.load(user.dict())  # Validate the user data.
            new_password = password.generate(user.password)  # Hash the password.
            user.password = new_password
            new_user = await self.user_cmd.create(user)  # Create the user using the command use case.
            return ResponseSuccessSchema(message=SuccessMessages.USER_CREATED, data=new_user)  # Return success response.
        except ValidationError as e:
            raise e  # Raise validation errors.
        except Exception as e:
            raise e  # Raise other exceptions.

    async def update_user(self, user_id: int, user: UpdateUserSchema):
        """
        Updates an existing user after validating the input data.

        Args:
            user_id (int): The ID of the user to update.
            user (UpdateUserSchema): Schema containing the updated user data.

        Returns:
            ResponseSuccessSchema: A success response with the updated user data.
        """
        search_user = await self.user_query.search_by_id(user_id)  # Search for the user by ID.

        if not search_user:
            raise UserNotFoundError()  # Raise an error if the user is not found.

        if user.email:
            valid_email = validate_email(user.email)  # Validate the email format.

            if not valid_email:
                raise EmailInvalidError()  # Raise an error if the email is invalid.

            search_email = SearchByEmailSchema(email=user.email)  # Prepare schema for email search.
            check_email = await self.user_query.search_by_email(search_email)  # Check if the email already exists.

            if check_email and check_email.id != user_id:
                raise EmailExistError()  # Raise an error if the email is already in use by another user.

        if user.password:
            if password.check_policies(user.password):
                raise PasswordWeakError()  # Raise an error if the password is weak.

        schema = UpdateUserValidationSchema()  # Initialize the validation schema.

        try:
            schema.load(user.dict())  # Validate the user data.

            if user.password:
                new_password = password.generate(user.password)  # Hash the password.
                user.password = new_password

            updated_user = await self.user_cmd.update(user_id, user)  # Update the user using the command use case.
            return ResponseSuccessSchema(message=SuccessMessages.USER_UPDATED, data=updated_user)  # Return success response.
        except ValidationError as e:
            raise e  # Raise validation errors.
        except Exception as e:
            raise e  # Raise other exceptions.

    async def search_by_email(self, email: SearchByEmailSchema):
        """
        Searches for a user by email.

        Args:
            email (SearchByEmailSchema): Schema containing the email to search for.

        Returns:
            ResponseSuccessSchema: A success response with the user data if found.
        """
        check_email = await self.user_query.search_by_email(email)  # Search for the user by email.

        if not check_email:
            raise EmailNotFound()  # Raise an error if the email is not found.

        return ResponseSuccessSchema(message=SuccessMessages.USER_CREATED, data=check_email)  # Return success response.

    async def search_by_email_return_user(self, email: SearchByEmailSchema):
        """
        Searches for a user by email and returns the user object.

        Args:
            email (SearchByEmailSchema): Schema containing the email to search for.

        Returns:
            User: The user object if found.
        """
        check_email = await self.user_query.search_by_email(email)  # Search for the user by email.

        if not check_email:
            raise EmailNotFound()  # Raise an error if the email is not found.

        return check_email  # Return the user object.

    async def erase_create_tests(self):
        """
        Removes test users created during testing.

        Returns:
            ResponseSuccessSchema: A success response indicating the operation was successful.
        """
        delete = await self.user_cmd.remove_create_tests()  # Remove test users using the command use case.
        return ResponseSuccessSchema(message=SuccessMessages.REMOVE_CREATED_TEST, data=delete)  # Return success response.
