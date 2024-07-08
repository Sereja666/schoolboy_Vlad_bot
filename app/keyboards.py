from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from app.database.requests import get_categories, get_category_item, get_throws

kb_main = ReplyKeyboardMarkup(keyboard=[
    # [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='давай примеры!')],
    # [KeyboardButton(text='Контакты')],
    # [KeyboardButton(text='О нас')],
    # [KeyboardButton(text='Броски')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def to_start():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='давай примеры!', callback_data='давай примеры!'))
    return keyboard.adjust(2).as_markup()


async def throw_list():
    all_throws = await get_throws()
    print(all_throws)
    keyboard = InlineKeyboardBuilder()
    for throw in all_throws:
        print(throw)
        keyboard.add(InlineKeyboardButton(text=throw.name, callback_data=f"throw_{throw.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()