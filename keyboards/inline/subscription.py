from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

chek_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 1-kanalga obuna", url="https://t.me/biomaqsad"),
        ],
        [
            InlineKeyboardButton(text="🔗 2-kanalga obuna", url="https://t.me/easy_python_uzb"),
        ],
        [
            InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'),
        ],
    ],
)