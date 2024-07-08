from sqlalchemy import select, literal

from app.database.models import async_session, User, Answers


async def set_user(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, tg_name=name))
            await session.commit()


async def set_user_answer(tg_id, question, answer):
    async with async_session() as session:
        # async with session.begin():
        result = await session.execute(select(Answers).filter(Answers.tg_id == tg_id))
        existing_answer = result.scalars().first()

        if existing_answer:
            existing_answer.question = str(question)
            existing_answer.answer = str(answer)
            await session.commit()
        else:
            new_answer = Answers(tg_id=int(tg_id), question=str(question), answer=str(answer))
            session.add(new_answer)
            await session.commit()


async def get_answer(tg_id):
    async with async_session() as session:
        return await session.scalars(select(Answers.answer).where(Answers.tg_id == int(tg_id)).limit(1))


async def get_answer_by_tg_id(tg_id: int):
    async with async_session() as session:
        result = await session.execute(select(Answers.answer, Answers.question).filter(Answers.tg_id == tg_id))
        answer, question = result.first()
        return answer, question
