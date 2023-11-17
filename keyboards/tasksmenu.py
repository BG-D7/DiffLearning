from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from random import shuffle
from resources.quizlines import quizzes

def tasksmenukeyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Викторина 🔮",
        callback_data="quiz")
    )
    #builder.add(InlineKeyboardButton(
        #text="Задачи 📝",
        #callback_data="brainfuck")) #Brainfuck — один из эзотерических языков программирования
    builder.add(InlineKeyboardButton(
        text="🏠",
        callback_data="start")
    )
    return builder.as_markup()

def quizmenukeyboard():
    builder = InlineKeyboardBuilder()

    shuffle(quizzes)
    quiz = quizzes[0]
    quiz = quiz.split("_")
    question = quiz[0]
    correct = quiz[1]
    quiz = quiz[2:]
    shuffle(quiz)
    btns = list()
    btns.append(InlineKeyboardButton(text=correct, callback_data="right"))
    for i in quiz:
        btns.append(InlineKeyboardButton(text=i,callback_data="wrong"))
    shuffle(btns)
    for i in btns:
        builder.row(i)
    return [question,builder.as_markup()]

def nextquizkeyboard():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="Следующий ➡️",
        callback_data="quiz")
    )
    builder.row(InlineKeyboardButton(
        text="🏠",
        callback_data="start"),
    InlineKeyboardButton(
        text="⬅️",
        callback_data="tasks"),

    )

    return builder.as_markup()
