from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_con = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📱", request_contact=True),
        ],
    ],
)