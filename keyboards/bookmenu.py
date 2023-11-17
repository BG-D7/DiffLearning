from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def bookmenukeyboard_tb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🏠",
        callback_data="start")
    )
    builder.add(InlineKeyboardButton(
        text="Уроки 📕",
        callback_data="lessons")
    )
    return builder.as_markup()


def lessonkeyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="⬅️",
        callback_data="lessons")
    )
    return builder.as_markup()


def lessons_first_page():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="1. Ввод и вывод данных",
        callback_data="l1")
    )
    builder.row(InlineKeyboardButton(
        text="2. Условия",
        callback_data="l2")
    )
    builder.row(InlineKeyboardButton(
        text="3. Вычисления",
        callback_data="l3")
    )
    builder.row(InlineKeyboardButton(
        text="⬅️",
        callback_data="book"),
        InlineKeyboardButton(
            text="➡️",
            callback_data="second_page"),
    )
    builder.row(InlineKeyboardButton(
        text="🏠",
        callback_data="start")
    )

    return builder.as_markup()

def lessons_second_page():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="4. Цикл for",
        callback_data="l4")
    )
    # builder.row(InlineKeyboardButton(
    #     text="5. Строки",
    #     callback_data="l5")
    # )
    # builder.row(InlineKeyboardButton(
    #     text="6. Цикл while",
    #     callback_data="l6")
    # )
    builder.row(InlineKeyboardButton(
        text="⬅️",
        callback_data="lessons")
    # InlineKeyboardButton(
    #     text="➡️",
    #     callback_data="third_page"),
    )
    builder.row(InlineKeyboardButton(
        text="🏠",
        callback_data="start")
    )


    return builder.as_markup()

def lessons_third_page():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="7. Списки",
        callback_data="l7")
    )
    builder.row(InlineKeyboardButton(
        text="8. Функции и рекурсия",
        callback_data="l8")
    )
    builder.row(InlineKeyboardButton(
        text="9. Двумерные массивы",
        callback_data="l9")
    )
    builder.row(InlineKeyboardButton(
        text="⬅️",
        callback_data="second_page"),
        InlineKeyboardButton(
            text="➡️",
            callback_data="fourth_page"),
    )
    builder.row(InlineKeyboardButton(
        text="🏠",
        callback_data="start")
    )

    return builder.as_markup()

def lessons_fourth_page():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="10. Множества",
        callback_data="l10")
    )
    builder.row(InlineKeyboardButton(
        text="11. Словари",
        callback_data="l11")
    )
    builder.row(InlineKeyboardButton(
        text="⬅️",
        callback_data="third_page")
    )
    builder.row(InlineKeyboardButton(
        text="🏠",
        callback_data="start")
    )

    return builder.as_markup()