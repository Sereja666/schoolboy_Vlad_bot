from typing import List

from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import settings

engine = create_async_engine(url=settings.db_url)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    tg_name: Mapped[str] = mapped_column(String(120))


class Answers(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column()
    question: Mapped[str] = mapped_column()
    answer: Mapped[str] = mapped_column()






async def async_main(): # создаю все таблицы если их нет
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
