from dddpy.shared.mysql.base import SessionLocal
from dddpy.user.domain.user_repository import UserRepository
from dddpy.user.usecase.user_query_schema import SearchByEmailSchema
from dddpy.user.infrastructure.user import DBUser
from dddpy.user.domain.user import User


class UserQueryRepositoryImpl(UserRepository):
    def __init__(self):
        self.repo = SessionLocal()

    async def search_by_email(self, email: SearchByEmailSchema):
        db_user = self.repo.query(DBUser).filter(DBUser.email == email.email).first()

        if db_user is None:
            return None

        return User.from_dbuser(db_user)

    async def search_by_id(self, user_id: int):
        user = self.repo.query(DBUser).filter(DBUser.id == user_id).first()

        if not user:
            return None

        return User.from_dbuser(user)
