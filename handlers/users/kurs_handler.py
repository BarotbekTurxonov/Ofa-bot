from loader import bot, dp
from aiogram import types
from keyboards.inline.fanlar import fanlar, fanlar_eng
from keyboards.default.kitoblar import kitoblar, kitoblar_eng


# UZBEK
# ___________________________________________________________________________________________
@dp.message_handler(text='✍️ Kursga yozilish')
async def register(msg: types.Message):
    await msg.answer("🔗 Marhamat yozilmoqchi bo\'lgan kursingizni tanlang : 👇👇", reply_markup=fanlar)


@dp.message_handler(text='📕 Kitoblar bo\'limi')
async def register(msg: types.Message):
    await msg.answer("🗞 O'zingizga kerakli bo'limni tanlang : 👇👇", reply_markup=kitoblar)
# _____________________________________________________________________________________________




#ENGISH
# ___________________________________________________________________________________________________
@dp.message_handler(text='✍️ Enroll course')
async def register(msg: types.Message):
    await msg.answer("🔗 Please select the course you want to enroll in: 👇👇", reply_markup=fanlar_eng)


@dp.message_handler(text='📕 Department of books')
async def register(msg: types.Message):
    await msg.answer("🗞 Choose the section you need : 👇👇", reply_markup=kitoblar_eng)
# ___________________________________________________________________________________________________


