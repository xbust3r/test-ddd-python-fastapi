class EmailExistError(Exception):
    message = "Your Email has exist, please try with other email"
    def __str__(self):
        return EmailExistError.message
class EmailInvalidError(Exception):
    message = "Your Email is invalid"

    def __str__(self):
        return EmailInvalidError.message
    
class EmailNotFound(Exception):
    message = "Your Email has not been found"

    def __str__(self):
        return EmailNotFound.message
class PasswordWeakError(Exception):
    message = "Your password is weak"

    def __str__(self):
        return PasswordWeakError.message
        
class UserNotFoundError(Exception):
    message = "Your User doesnt exist"

    def __str__(self):
        return UserNotFoundError.message