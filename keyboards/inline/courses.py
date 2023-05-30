from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

aiogram_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursni boshlash", url="https://mohirdev.uz/kurslar/telegram/"),
            InlineKeyboardButton(text="Batafsil", callback_data='aiogram'),
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query='aiogram'),
        ],
    ],
)

python_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursni boshlash", url="https://mohirdev.uz/kurslar/telegram/"),
            InlineKeyboardButton(text="Batafsil", callback_data='batafsilpy'),
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query='python'),
        ],
    ],
)