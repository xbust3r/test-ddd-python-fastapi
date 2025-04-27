class EmailExistError(Exception):
    """
    Exception raised when an email already exists in the system.
    """

    # Error message indicating the email already exists.
    message = "Your Email has exist, please try with other email"

    # Returns the error message as a string.
    def __str__(self):
        return EmailExistError.message


class EmailInvalidError(Exception):
    """
    Exception raised when an email is invalid.
    """

    # Error message indicating the email is invalid.
    message = "Your Email is invalid"

    # Returns the error message as a string.
    def __str__(self):
        return EmailInvalidError.message


class EmailNotFound(Exception):
    """
    Exception raised when an email is not found in the system.
    """

    # Error message indicating the email was not found.
    message = "Your Email has not been found"

    # Returns the error message as a string.
    def __str__(self):
        return EmailNotFound.message


class PasswordWeakError(Exception):
    """
    Exception raised when a password is considered weak.
    """

    # Error message indicating the password is weak.
    message = "Your password is weak"

    # Returns the error message as a string.
    def __str__(self):
        return PasswordWeakError.message


class UserNotFoundError(Exception):
    """
    Exception raised when a user is not found in the system.
    """

    # Error message indicating the user does not exist.
    message = "Your User doesnt exist"

    # Returns the error message as a string.
    def __str__(self):
        return UserNotFoundError.message