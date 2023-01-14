from aiogram import Bot, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


language = ReplyKeyboardMarkup(
    [
        [KeyboardButton('UZ 🇺🇿'),
        KeyboardButton('ENG 🇺🇸')]

    ], resize_keyboard=True
)


