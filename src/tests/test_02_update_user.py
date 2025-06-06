import pytest
from dddpy.user.usecase.user_usecase import UserUsecase
# from contexts.user.domain.model import UpdateUserSchema
from dddpy.user.usecase.user_cmd_schema import UpdateUserSchema
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema
from dddpy.user.domain.user_exception import EmailInvalidError, PasswordWeakError
from dddpy.user.domain.user_success import SuccessMessages
from marshmallow.exceptions import ValidationError
import asyncio


user_usecase = UserUsecase()


@pytest.fixture
def user_id():
    find_email = "john5@qa_unitestexample.com"
    user = asyncio.run(user_usecase.search_by_email_return_user(
        SearchByEmailSchema(email=find_email)))
    print("USER ID", user.id)
    return user.id

def test_update_user_invalid_email(user_id):

    with pytest.raises(EmailInvalidError):
        asyncio.run(user_usecase.update_user(
            user_id,
            UpdateUserSchema(email="invalid_email", name="John Doe"),
        ))

@pytest.mark.asyncio
async def test_update_user_name_with_numbers(user_id):
    with pytest.raises(ValidationError):
        await user_usecase.update_user(
            user_id,
            UpdateUserSchema(email="john.doe@example.com",
                             name="John Doe 123"),
        )

@pytest.mark.asyncio
async def test_update_user_name_with_weak_password(user_id):
    with pytest.raises(PasswordWeakError):
        await user_usecase.update_user(
            user_id,
            UpdateUserSchema(email="john.doe@example.com",
                             name="John Doe 123", password="123456"),
        )


@pytest.mark.asyncio
async def test_update_user_correct_email(user_id):
    new_email = "johnupdate@qa_unitestexample.com"
    updated_user = await user_usecase.update_user(
        user_id,
        UpdateUserSchema(email=new_email, name="John Doe"),
    )
    print(updated_user)
    assert updated_user.success == True
    assert updated_user.data.email == new_email

