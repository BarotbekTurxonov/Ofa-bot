from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

boshlangich_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Kursga yozilish"),
            KeyboardButton(text="📕 Kitoblar bo\'limi"),
        ]
    ], resize_keyboard=True
)




boshlangich_button_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Enroll course"),
            KeyboardButton(text="📕 Department of books"),
        ]
    ], resize_keyboard=True
)





kontakt = ReplyKeyboardMarkup(
    keyboard=[
        KeyboardButton("☎️ Kontakt Ulashish", request_contact=True)
    ]
)