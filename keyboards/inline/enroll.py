from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kursga_yozilish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Kursga yozilish 📝",callback_data="regis"),
        ]
    ]
)