from contexts.shared.mysql.base import SessionLocal
from contexts.user.domain.user_repository import UserRepository
from contexts.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from contexts.shared.timezone import Timezone
from contexts.user.infrastructure.user import DBUser
from sqlalchemy import delete
from contexts.user.domain.user import User
from contexts.user.infrastructure.user_query_repository import UserQueryRepositoryImpl


class UserCmdRepositoryImpl(UserRepository):
    def __init__(self):
        self.repo = SessionLocal()

    async def create(self, user: CreateUserSchema):
        today = Timezone.get_datetime()
        domain_user = User(
            id=None,
            name=user.name,
            email=user.email,
            password=user.password,
            created_at=today,
            updated_at=today,
            is_public=False
        )
        new_user = User.to_dbuser(domain_user)
        self.repo.add(new_user)
        self.repo.commit()
        self.repo.refresh(new_user)
        return User.from_dbuser(new_user)

    async def update(self, user_id: int, user: UpdateUserSchema):
        db_user = await UserQueryRepositoryImpl().search_by_id(user_id)

        if not db_user:
            return None

        if user.name:
            db_user.name = user.name
        if user.email:
            db_user.email = user.email
        if user.password:
            db_user.password = user.password

        db_user.updated_at = Timezone.get_datetime()
        self.repo.commit()

        return User.from_dbuser(db_user)

    async def remove_create_tests(self):
        test_domain = "@qa_unitestexample.com"
        stmt = delete(DBUser).where(DBUser.email.like(f"%{test_domain}"))
        self.repo.execute(stmt)
        self.repo.commit()

        return True
