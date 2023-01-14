from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.til import language
from states.post import Post
from loader import dp, bot
from aiogram.dispatcher import FSMContext


from keyboards.default.boshlangich_button import boshlangich_button, boshlangich_button_eng


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}!", reply_markup=language)




#Language Selection

@dp.message_handler(text='UZ 🇺🇿')
async def uzbek_til(message: types.Message):
    await message.answer('🇺🇿')
    await message.answer('Siz o\'zbek tanlandingiz!', reply_markup=boshlangich_button)


@dp.message_handler(text='ENG 🇺🇸')
async def uzbek_til(message: types.Message):
    await message.answer('🇺🇸')
    await message.answer("You chose English!", reply_markup=boshlangich_button_eng) 




# _________________________________________________________________________________________________

# POST JOYLASH UCHUN

# _________________________________________________________________________________________________






































