from aiogram import types
from data.config import CHANNEL
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states.register import EnrollEnglish
from states.register_eng import EnrollEnglishEng
from keyboards.default.boshlangich_button import boshlangich_button, boshlangich_button_eng
from aiogram.types import ReplyKeyboardRemove


# Uzbekcha


@dp.callback_query_handler(text='ingliz')
async def english(call: types.CallbackQuery):
    await call.message.answer("📌<u>Ingliz tili</u> \n\n Ajoyib, Endi sizdan so'ralgan malumotlarni xatosiz kiriting !", reply_markup=ReplyKeyboardRemove())
    await call.message.reply('🔖 To\'liq ism faliyangizni kiriting....\n Misol uchun :  Barotbek Turxonov\n\n<b>Bekor qilish uchun /cancel buyrug\'ini bering</b>')
    await EnrollEnglish.full_name.set()
    await call.message.delete()



@dp.message_handler(state=EnrollEnglish.full_name)
async def step1(msg: types.Message, state : FSMContext):
    full_name = msg.text

    if full_name == '/cancel':
        await msg.answer('Amal bekor qilindi!', reply_markup=boshlangich_button)
        await state.finish()
    else:
        await state.update_data(
            {'full_name':full_name}
        )

        await msg.answer('Telefon raqamingizni yuboring..')
        await EnrollEnglish.next()




@dp.message_handler(state=EnrollEnglish.phone)
async def step1(msg: types.Message, state : FSMContext):
    phone = msg.text

    if phone == '/cancel':
        await msg.answer('Amal bekor qilindi!', reply_markup=boshlangich_button)
        await state.finish()
    else:

        await state.update_data(
            {'phone':phone}
        )

        data = await state.get_data()

        admin_msg = f"👥 O'quvchining to'liq ismi :  {data['full_name']}\n\n\
    📞 Telefon raqami : <code>{data['phone']}</code>\n\n\
    ✅ Telegram : @{msg.from_user.username}\n\n\
    🔗 Tanlagan Fan : <tg-spoiler> <u><b>Ingliz tili</b></u></tg-spoiler>"

        await msg.answer('✅ Xabaringiz Muvaffaqiyatli Yuborildi!\n📞 Tez orada Admin siz bilan aloqaga chiqadi!', reply_markup=boshlangich_button)
        
        await dp.bot.send_message(CHANNEL[0], text=admin_msg)
        await state.finish()


# _________________________________________________





#  ENGLISH 


@dp.callback_query_handler(text='eng', state=None)
async def english(call: types.CallbackQuery):
    await call.message.answer("📌<u>English</u> \n\n Great, Now enter the requested information without error!", reply_markup=ReplyKeyboardRemove())
    await call.message.reply('<u>🔖 Enter your full name....</u>\n\n For example: Barotbek Turxonov\n\n<b>To cancel, give the /cancel command</b>')
    await EnrollEnglishEng.full_name.set()
    await call.message.delete() 


@dp.message_handler(state=EnrollEnglishEng.full_name)
async def step1(msg: types.Message, state : FSMContext):
    full_name = msg.text
    
    if full_name == '/cancel':
        await msg.answer('Action canceled!', reply_markup=boshlangich_button_eng)
        await state.finish()

    else:
        await state.update_data(
            {'full_name':full_name}
        )

        await msg.answer('Send your phone number....')
        await EnrollEnglishEng.next()





@dp.message_handler(state=EnrollEnglishEng.phone)
async def step1(msg: types.Message, state : FSMContext):
    phone = msg.text

    if phone == '/cancel':
        await msg.answer('Action canceled!', reply_markup=boshlangich_button_eng)
        await state.finish()

    else:
        await state.update_data(
            {'phone':phone}
        )

        data = await state.get_data()
        admin_msg = f"👥 Student's full name :  {data['full_name']}\n\n\
    📞 Phone Number : <code>{data['phone']}</code>\n\n\
    ✅ Telegram : @{msg.from_user.username}\n\n\
    🔗 Selected Subject : <tg-spoiler> <u><b>English</b></u></tg-spoiler>"
        if data['full_name'] == '/start':
            await msg.answer('Xato!')

        await msg.answer('✅  Your message has been successfully sent!\n📞 Admin will contact you soon!', reply_markup=boshlangich_button_eng)
        
        await dp.bot.send_message(CHANNEL[0], text=admin_msg)
        await state.finish()

