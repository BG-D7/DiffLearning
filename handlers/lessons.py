from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.bookmenu import lessonkeyboard
from modules.dbworker import DbWorker

DbWorker = DbWorker()
router = Router()


@router.callback_query(F.data == "l1")
async def list_of_lessons(callback: CallbackQuery):
    DbWorker.append_to_lessons(callback.from_user.id,1)
    await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>

В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
                                  reply_markup=lessonkeyboard(),parse_mode="HTML")


@router.callback_query(F.data == "l2")
async def list_of_lessons(callback: CallbackQuery):
    DbWorker.append_to_lessons(callback.from_user.id,2)
    await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-2-Usloviya-11-10">Условия</a>

В этом уроке ты узнаешь как работают условия в языке Python""",
                                  reply_markup=lessonkeyboard(),parse_mode="HTML")


@router.callback_query(F.data == "l3")
async def list_of_lessons(callback: CallbackQuery):
    DbWorker.append_to_lessons(callback.from_user.id,3)
    await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-3-Vychisleniya-11-10">Вычисления</a>

Этот урок научит тебя работать с арифметикой""",
                                  reply_markup=lessonkeyboard(),parse_mode="HTML")


@router.callback_query(F.data == "l4")
async def list_of_lessons(callback: CallbackQuery):
    DbWorker.append_to_lessons(callback.from_user.id,4)
    await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-4-Cikl-for-11-10">Цикл For</a>

Цикл For - позволяет выполнить действие n раз, этот урок обьяснит как его использовать""",
                                  reply_markup=lessonkeyboard(),parse_mode="HTML")


# @router.callback_query(F.data == "l5")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id,5)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(),parse_mode="HTML")
#
#
# @router.callback_query(F.data == "l6")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id, 6)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(), parse_mode="HTML")
#
#
# @router.callback_query(F.data == "l7")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id, 7)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(), parse_mode="HTML")
#
#
# @router.callback_query(F.data == "l8")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id, 8)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(), parse_mode="HTML")
#
#
# @router.callback_query(F.data == "l9")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id, 9)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(), parse_mode="HTML")
#
#
# @router.callback_query(F.data == "l10")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id, 10)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(), parse_mode="HTML")
#
#
# @router.callback_query(F.data == "l11")
# async def list_of_lessons(callback: CallbackQuery):
#     DbWorker.append_to_lessons(callback.from_user.id, 11)
#     await callback.message.edit_text("""<a href="https://telegra.ph/Zanyatie-1-Vvod-i-vyvod-dannyh-11-02">Ввод и вывод данных</a>
#
# В этом уроке ты узнаешь основы ввода и вывода данных, а также познакомишься с синтаксисом и арифметикой""",
#                                   reply_markup=lessonkeyboard(), parse_mode="HTML")




