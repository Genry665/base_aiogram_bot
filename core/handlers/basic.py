from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет <b>{message.from_user.first_name}</b>! Рад тебя видеть')
    await message.answer(f'Привет<s> {message.from_user.first_name}!</s> Рад тебя видеть')
    await message.reply(f'Привет <tg-spoiler>{message.from_user.first_name}</tg-spoiler>! Рад тебя видеть')
