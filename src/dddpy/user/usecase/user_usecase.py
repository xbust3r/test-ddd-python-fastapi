from dddpy.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema

from dddpy.shared.schemas.response_schema import ResponseSuccessSchema
from dddpy.shared.utils.validate_email import validate_email
from dddpy.shared.utils.password import password

from dddpy.user.domain.user_exception import EmailExistError, EmailInvalidError, PasswordWeakError, UserNotFoundError, EmailNotFound
from dddpy.user.domain.user_success import SuccessMessages
from dddpy.user.domain.user_validation import CreateUserValidationSchema, UpdateUserValidationSchema

from marshmallow.exceptions import ValidationError

from dddpy.user.usecase.usecase_factory import user_cmd_usecase, user_query_usecase


class UserUsecase:
    
    def __init__(self):
        self.user_cmd = user_cmd_usecase()
        self.user_query = user_query_usecase()
    
    async def create_user(self, user: CreateUserSchema):
        search_email = SearchByEmailSchema(email=user.email)
        check_email = await self.user_query.search_by_email(search_email)
        valid_email = validate_email(user.email)
        
        if not valid_email:
            raise EmailInvalidError()
        if check_email:
            raise EmailExistError()
        if password.check_policies(user.password):
            raise PasswordWeakError
        
        schema = CreateUserValidationSchema()
        
        try:
            schema.load(user.dict())
            new_password = password.generate(user.password)
            user.password = new_password
            new_user = await self.user_cmd.create(user)
            return ResponseSuccessSchema(message=SuccessMessages.USER_CREATED, data=new_user)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise e

    async def update_user(self, user_id: int, user: UpdateUserSchema):
        search_user = await self.user_query.search_by_id(user_id)
        
        if not search_user:
            raise UserNotFoundError()
        
        if user.email:
            valid_email = validate_email(user.email)
            
            if not valid_email:
                raise EmailInvalidError()
                
            search_email = SearchByEmailSchema(email=user.email)
            check_email = await self.user_query.search_by_email(search_email)
            
            if check_email and check_email.id != user_id:
                raise EmailExistError()
        
        if user.password:
            if password.check_policies(user.password):
                raise PasswordWeakError()
        
        schema = UpdateUserValidationSchema()
        
        try:
            schema.load(user.dict())
            
            if user.password:
                new_password = password.generate(user.password)
                user.password = new_password
            
            updated_user = await self.user_cmd.update(user_id, user)
            return ResponseSuccessSchema(message=SuccessMessages.USER_UPDATED, data=updated_user)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise e

    async def search_by_email(self, email: SearchByEmailSchema):
        check_email = await self.user_query.search_by_email(email)

        if not check_email:
            raise EmailNotFound
        
        return ResponseSuccessSchema(message=SuccessMessages.USER_CREATED, data=check_email)

    async def search_by_email_return_user(self, email: SearchByEmailSchema):
        check_email = await self.user_query.search_by_email(email)
        
        if not check_email:
            raise EmailNotFound
        
        return check_email
    
    async def erase_create_tests(self):
        delete = await self.user_cmd.remove_create_tests()
        return ResponseSuccessSchema(message=SuccessMessages.REMOVE_CREATED_TEST, data=delete)
