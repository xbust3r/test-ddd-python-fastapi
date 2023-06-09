from dddpy.user.usecase.user_cmd_usecase import UserCmdUsecase
from dddpy.user.usecase.user_query_usecase import UserQueryUsecase
from dddpy.user.infrastructure.user_cmd_repository import UserCmdRepositoryImpl
from dddpy.user.infrastructure.user_query_repository import UserQueryRepositoryImpl

def user_cmd_usecase():
    user_cmd_repository = UserCmdRepositoryImpl()
    return UserCmdUsecase(user_cmd_repository)

def user_query_usecase():
    user_query_repository = UserQueryRepositoryImpl()
    return UserQueryUsecase(user_query_repository)