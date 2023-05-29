from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍 Eng yaqin do'konni topish", callback_data='mylocation'),
        ],
        [
            InlineKeyboardButton(text="📱 Kontaktni ulashish", callback_data='mycontact'),
        ],
    ],
)