from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from aiogram.filters.command import Command

from keyboards.startmenu import startmenukeyboard
from modules.dbworker import DbWorker


router = Router()
DbWorker = DbWorker()

# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    logo = FSInputFile("resources/logo.jpg")
    DbWorker.add_user_to_db(message.from_user.id)
    await message.answer_photo(caption="""Привет! Добро пожаловать в DiffLearning
\nЭтот бот позволит тебе изучить python прямо в телеграм
\nВыбери нужный пункт меню""", photo=logo, reply_markup=startmenukeyboard())

@router.callback_query(F.data == "start")
async def inline_start(callback: CallbackQuery):
    logo = FSInputFile("resources/logo.jpg")
    await callback.message.delete()
    await callback.message.answer_photo(caption="""Привет! Добро пожаловать в DiffLearning
\nЭтот бот позволит тебе изучить python прямо в телеграм
\nВыбери нужный пункт меню""", photo=logo, reply_markup=startmenukeyboard())