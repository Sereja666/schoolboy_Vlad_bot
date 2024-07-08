import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.database.models import async_main
from app.handlers import router
from config import settings
import logging
from aiogram.client.default import DefaultBotProperties

async def main():
    await async_main()

    bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
        # тут ещё много других интересных настроек
    ))
    dp = Dispatcher()  # основной роутер, обрабатывающий входящие обновления (сообщения, колбеки)
    dp.include_router(router=router)  # передаю обработчику роутер из handler
    await dp.start_polling(bot, skip_updates=False)  # start_polling - отправляет Дурову запрос, и ждёт ответ


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # убрать на проде
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
