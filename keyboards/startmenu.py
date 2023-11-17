from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def startmenukeyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Учебник 📕",
        callback_data="book")
    )
    builder.add(InlineKeyboardButton(
        text="Задачки 🧠",
        callback_data="tasks")
    )
    return builder.as_markup()