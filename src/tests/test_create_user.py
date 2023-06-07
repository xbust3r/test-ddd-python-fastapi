import pytest
from dddpy.user.usecase.user_usecase import UserUsecase
from dddpy.user.usecase.user_cmd_schema import CreateUserSchema

from dddpy.user.domain.user_exception import PasswordWeakError, EmailExistError, EmailInvalidError
from dddpy.user.domain.user_success import SuccessMessages
from marshmallow.exceptions import ValidationError

@pytest.mark.asyncio
async def test_create_user_invalid_email():
    user_usecase = UserUsecase()
    new_user = CreateUserSchema(name="John Doe", email="invalid_email", password="SecureP@ssw0rd")
    
    with pytest.raises(EmailInvalidError):
        await user_usecase.create_user(new_user)

@pytest.mark.asyncio
async def test_create_user_weak_password():
    user_usecase = UserUsecase()
    new_user = CreateUserSchema(name="John Doe", email="john2@qa_unitestexample.com", password="123456")
    
    with pytest.raises(PasswordWeakError):
        await user_usecase.create_user(new_user)
        


@pytest.mark.asyncio
async def test_create_user_long_name():
    user_usecase = UserUsecase()
    long_name = "A" * 300
    new_user = CreateUserSchema(name=long_name, email="john4@qa_unitestexample.com", password="SecureP@ssw0rd")
    
    #response = await user_usecase.create_user(new_user)
    #assert response.success == True
    with pytest.raises(ValidationError):
        await user_usecase.create_user(new_user)


@pytest.mark.asyncio
async def test_create_user_strong_password():
    user_usecase = UserUsecase()
    new_user = CreateUserSchema(name="John Doe", email="john5@qa_unitestexample.com", password="SecureP@ssw0rd12345E!@")
    
    response = await user_usecase.create_user(new_user)
    assert response.success == True


@pytest.mark.asyncio
async def test_create_user_email_existr():
    user_usecase = UserUsecase()
    new_user = CreateUserSchema(name="John Doe", email="john5@qa_unitestexample.com", password="123456")
    
    with pytest.raises(EmailExistError):
        await user_usecase.create_user(new_user)

#@pytest.mark.asyncio
#async def test_erase_create_tests():
#    user_usecase = UserUsecase()

#    response = await user_usecase.erase_create_tests()

#    assert response.success == True
#    assert response.message == SuccessMessages.REMOVE_CREATED_TEST