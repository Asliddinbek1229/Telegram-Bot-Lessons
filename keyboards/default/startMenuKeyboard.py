from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🛒 Mahsulotlar"),
            KeyboardButton(text="🛒 Qo'llanma"),
        ],
    ],
)