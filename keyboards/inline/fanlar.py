from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


fanlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Ingliz tili",callback_data="ingliz"),
         InlineKeyboardButton("Ona tili",callback_data="ona")],
        [InlineKeyboardButton("Kimyo",callback_data="kimyo"),
         InlineKeyboardButton("Bilogiya",callback_data="biol")],
        [InlineKeyboardButton("Mental Arifmetika",callback_data="mental"),
         InlineKeyboardButton("Tarix",callback_data="tarix")],
        [InlineKeyboardButton("Rus tili",callback_data="rus"),
        InlineKeyboardButton('Fizika', callback_data='fiz'),]
    ]
)



fanlar_eng = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("English",callback_data="eng"),
         InlineKeyboardButton("Mother tongue",callback_data="moth")],
        [InlineKeyboardButton("Chemistry",callback_data="chem"),
         InlineKeyboardButton("Biology",callback_data="bio")],
        [InlineKeyboardButton("Mental Arithmetic",callback_data="men"),
         InlineKeyboardButton("History",callback_data="his")],
        [InlineKeyboardButton("Russian language",callback_data="russ"),
        InlineKeyboardButton("Physics", callback_data='fizz')]
    ]
)

