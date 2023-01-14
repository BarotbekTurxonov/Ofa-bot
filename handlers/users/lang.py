from aiogram import types
from loader import bot, dp
from keyboards.default.til import language


@dp.message_handler(commands='lang')
async def lang(msg: types.Message):
    await msg.answer('Tilni tanlang!.', reply_markup=language)