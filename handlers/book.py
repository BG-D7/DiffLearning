from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.bookmenu import bookmenukeyboard_tb, lessons_first_page, lessonkeyboard, lessons_second_page, \
    lessons_third_page,lessons_fourth_page
from modules.dbworker import DbWorker

router = Router()
DbWorker = DbWorker()

@router.callback_query(F.data == "book")
async def list_of_lessons(callback: CallbackQuery):
    await callback.message.delete()
    msg = DbWorker.read_user_lessons(callback.from_user.id)
    await callback.message.answer(msg, reply_markup=bookmenukeyboard_tb())


@router.callback_query(F.data == "lessons")
async def list_of_lessons(callback: CallbackQuery):
    await callback.message.edit_text("Выберите урок", reply_markup=lessons_first_page())

@router.callback_query(F.data == "second_page")
async def list_of_lessons(callback: CallbackQuery):
    await callback.message.edit_text("Выберите урок", reply_markup=lessons_second_page())

@router.callback_query(F.data == "third_page")
async def list_of_lessons(callback: CallbackQuery):
    await callback.message.edit_text("Выберите урок", reply_markup=lessons_third_page())

@router.callback_query(F.data == "fourth_page")
async def list_of_lessons(callback: CallbackQuery):
    await callback.message.edit_text("Выберите урок", reply_markup=lessons_fourth_page())
