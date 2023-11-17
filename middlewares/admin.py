from datetime import datetime
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from modules.dbworker import DbWorker

DbWorker = DbWorker()

def _is_admin(uid) -> bool:
    return DbWorker.is_admin(uid)


# Это будет inner-мидлварь на задачи
class AdminCallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # Если сегодня не суббота и не воскресенье,
        # то продолжаем обработку.
        if _is_admin(event.from_user.id):
            return await handler(event, data)
        # В противном случае отвечаем на колбэк самостоятельно
        # и прекращаем дальнейшую обработку
        await event.answer(
            "Функция отключена для обычных пользователей",
            show_alert=True
        )
        return