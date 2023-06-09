from dddpy.shared.mysql.base import SessionLocal
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema
from dddpy.user.domain.user_repository import UserRepository
from dddpy.user.infrastructure.user_query_repository import UserQueryRepositoryImpl


class UserQueryUsecase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def search_by_email(self, email: SearchByEmailSchema):
        return await self.user_repository.search_by_email(email)

    async def search_by_id(self, user_id: int):
        return await self.user_repository.search_by_id(user_id)
