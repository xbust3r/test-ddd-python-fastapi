import pytest
from dddpy.user.usecase.user_usecase import UserUsecase
# from contexts.user.domain.model import UpdateUserSchema
from dddpy.user.usecase.user_cmd_schema import UpdateUserSchema
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema
from dddpy.user.domain.user_exception import EmailInvalidError, PasswordWeakError
from dddpy.user.domain.user_success import SuccessMessages
from marshmallow.exceptions import ValidationError
import asynciopytest

@pytest.mark.asyncio
def test_erase_create_tests():
    user_usecase = UserUsecase()

    response = user_usecase.erase_create_tests()

    assert response.success == True
    assert response.message == SuccessMessages.REMOVE_CREATED_TEST