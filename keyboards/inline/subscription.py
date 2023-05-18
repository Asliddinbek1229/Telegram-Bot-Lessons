from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

chek_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obunani tekshirish", callback_data='check_subs'),
        ],
    ],
)