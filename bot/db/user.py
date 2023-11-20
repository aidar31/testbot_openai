import datetime
from sqlalchemy import Column, Integer, VARCHAR, DATE, select
from sqlalchemy.orm import sessionmaker

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    
    user_id = Column(
        Integer, unique=True, nullable=False,
        primary_key=True
    )
    username = Column(
        VARCHAR(32), unique=False, nullable=True
    )
    reg_date = Column(
        DATE, default=datetime.date.today()
    )
    upd_date = Column(
        DATE, onupdate=datetime.date.today()
    )
    
    def __str__(self):
        return f"<User:{self.user_id}>"
    


async def get_user(user_id: int, session: sessionmaker) -> User:
    async with session() as session:
        async with session.begin():
            return await session.execute(select(User).where(User.user_id == user_id)).one_or_none()