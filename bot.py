import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from config_reader import config
from handlers import basic, book, lessons, tasks
import modules.dbworker as db



# Запуск процесса поллинга новых апдейтов
async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token=config.bot_token.get_secret_value())
    # Диспетчер
    dp = Dispatcher()
    dp.include_routers(basic.router, book.router, lessons.router, tasks.router)
    DbWorker = db.DbWorker()
    DbWorker.create_db()


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
