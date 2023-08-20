from aiogram import Bot
from aiogram.types import Message
from datetime import datetime


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет <b>{message.from_user.first_name}</b>! Рад тебя видеть')
    await message.answer(f'Привет<s> {message.from_user.first_name}!</s> Рад тебя видеть')
    await message.reply(f'Привет <tg-spoiler>{message.from_user.first_name}</tg-spoiler>! Рад тебя видеть')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично! Ты отправил картинку')
    file = await bot.get_file(message.photo[-1].file_id)
    date = datetime.now()
    now = date.strftime("%Y-%m-%d_%H:%M:%S")
    user_name = message.from_user.id
    await bot.download_file(file.file_path, 'photo.jpg')
