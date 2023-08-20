from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start

from core.setting import settings

import asyncio
import logging


async def start_bot(bot: Bot):
    await bot.send_message(settings.bot.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bot.admin_id, text='Бот остновлен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
                        )
    bot = Bot(token=settings.bot.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    # dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)

    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
