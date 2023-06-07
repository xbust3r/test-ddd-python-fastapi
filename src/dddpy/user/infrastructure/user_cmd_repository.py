from dddpy.shared.mysql.base import SessionLocal
from dddpy.user.domain.user_repository import UserRepository
from dddpy.user.usecase.user_cmd_schema import CreateUserSchema, UpdateUserSchema
from dddpy.shared.timezone import Timezone
from dddpy.user.infrastructure.user import DBUser
from sqlalchemy import delete
from dddpy.user.domain.user import User
from dddpy.user.infrastructure.user_query_repository import UserQueryRepositoryImpl


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
            status=None,
            active_token="asd123",
            created_at=today,
            updated_at=today
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
