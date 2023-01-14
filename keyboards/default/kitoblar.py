from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kitoblar = ReplyKeyboardMarkup(
   keyboard=[
        [
            KeyboardButton("📚 Essential Books"),
            KeyboardButton('📚 Reading Books')
        ],
                [
            KeyboardButton("📚 English Tests")
        ] ,
        
        [
            KeyboardButton('📚 IELTS Books'),
            KeyboardButton("📚 Collocation Books")
        ],
        [
            KeyboardButton('🔙Orqaga')
        ]

    ], resize_keyboard=True


)





kitoblar_eng = ReplyKeyboardMarkup(
   keyboard=[
        [
            KeyboardButton("📚 Essential Books"),
            KeyboardButton('📚 Reading Books')
        ],
                [
            KeyboardButton("📚 English Tests")
        ] ,
        
        [
            KeyboardButton('📚 IELTS Books'),
            KeyboardButton("📚 Collocation Books")
        ],
        [
            KeyboardButton('🔙Back')
        ]

    ], resize_keyboard=True


)









