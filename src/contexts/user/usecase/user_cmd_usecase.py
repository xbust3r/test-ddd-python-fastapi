
from contexts.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from contexts.user.domain.user_repository import UserRepository


class UserCmdUsecase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create(self, new_user: CreateUserSchema):
        user = await self.user_repository.create(new_user)
        return user

    async def update(self, user_id:int, update_user: UpdateUserSchema):
        user = await self.user_repository.update(user_id, update_user)
        return user

    async def remove_create_tests(self):
        await self.user_repository.remove_create_tests()
        return True
