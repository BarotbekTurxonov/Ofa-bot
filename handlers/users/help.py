from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam olish",
            "/lang - Tilni o'zgartirish")
    
    await message.answer("\n".join(text))
