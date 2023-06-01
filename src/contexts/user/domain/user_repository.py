from typing import Optional
from contexts.user.infrastructure.user import DBUser
from contexts.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from contexts.user.usecase.user_query_schema import SearchByEmailSchema, SearchByIdSchema


class UserRepository:

    async def create(self, user: CreateUserSchema) -> DBUser:
        raise NotImplementedError

    async def update(self, user_id: int, user: UpdateUserSchema) -> DBUser:
        raise NotImplementedError

    async def remove_create_tests(self) -> bool:
        raise NotImplementedError
    
    async def search_by_email(self, email: SearchByEmailSchema):
        raise NotImplementedError

    async def search_by_id(self, user_id: int):
        raise NotImplementedError
