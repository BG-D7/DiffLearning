from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.tasksmenu import tasksmenukeyboard, quizmenukeyboard, nextquizkeyboard
from modules.dbworker import DbWorker
from middlewares.admin import AdminCallbackMiddleware


router = Router()
DbWorker = DbWorker()
#router.callback_query.middleware(AdminCallbackMiddleware())

@router.callback_query(F.data == "tasks")
async def choose_your_task(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Привет!\n\nВыбери вид задачек", reply_markup=tasksmenukeyboard())


@router.callback_query(F.data == "quiz")
async def choose_your_task(callback: CallbackQuery):
    await callback.message.delete()
    msg = quizmenukeyboard()
    await callback.message.answer(msg[0], reply_markup=msg[1])

@router.callback_query(F.data == "right")
async def choose_your_task(callback: CallbackQuery):
    await callback.message.edit_text("Верно! ✅", reply_markup=nextquizkeyboard())

@router.callback_query(F.data == "wrong")
async def choose_your_task(callback: CallbackQuery):
    await callback.message.edit_text("❌ Неверно! Повтори теорию", reply_markup=nextquizkeyboard())

