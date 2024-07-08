import io

import aiohttp
from aiogram import F, Router, types

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

import app.database.requests as rq
import app.keyboards as kb
from app.module.module_mathematics import matematics

router = Router()  # этот роутер обращается к dp = Dispatcher()


# router.message.middleware(TestMiddleware())


@router.message(CommandStart())
async def cmd_start(message: Message):
    # await message.reply(f'Привет. \nТвой ID: {message.from_user.id} \nИмя: {message.from_user.first_name}', reply_markup=kb.main) # reply - Ответ на сообщение , answer - отправка сообщения
    await rq.set_user(message.from_user.id, message.from_user.first_name)
    await message.reply(f'Привет. \nТвой ID: {message.from_user.id} \nИмя: {message.from_user.first_name}',
                        reply_markup=kb.kb_main)  # reply - Ответ на сообщение , answer - отправка сообщения


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=await kb.categories())


@router.message(F.text == 'давай примеры!')
async def school_task(message: Message):
    query, result = await matematics()
    print(message.from_user.id, query, result)
    await rq.set_user_answer(tg_id=message.from_user.id,
                             question=query,
                             answer=result)
    await message.answer(f'{message.from_user.first_name}, реши пример:\n\n <b> {query}  </b>')


# Обработчик для получения ответа от пользователя
# Обработчик для получения ответа от пользователя
@router.message(F.text != 'давай примеры!')
async def check_answer(message: Message):
    user_answer = message.text
    answer, question = await rq.get_answer_by_tg_id(message.from_user.id)
    print("ОТВЕТ: ", answer)
    # await message.answer(answer)

    if user_answer != answer:
        await message.answer(f'❌ Неверно, попробуйте ещё раз. \n <b> {question} </b>')
    else:
        # await message.answer_photo(photo=types.InputFile(r'C:\Python\examiner\image_files\ura.bmp'), caption=f'{answer} - верно!', reply_markup=kb.kb_main)

        # Отправка файла из файловой системы
        image_from_pc = FSInputFile(r"C:\Python\examiner\image_files\ura.jpg")
        await message.answer_photo(
            image_from_pc,
            caption=f'✅  <b> {answer}  </b> - верно! ', reply_markup=kb.kb_main
        )

        # await message.answer(f'✅  {answer} - верно! ', reply_markup=kb.kb_main)
