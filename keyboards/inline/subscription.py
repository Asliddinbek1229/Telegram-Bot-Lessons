from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

chek_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 1-kanalga obuna", callback_data='one_channel', url="https://t.me/biomaqsad"),
        ],
        [
            InlineKeyboardButton(text="🔗 2-kanalga obuna", callback_data='two_channel', url="https://t.me/easy_python_uzb"),
        ],
        [
            InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'),
        ],
    ],
)

one_chanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 1-kanalga obuna", url="https://t.me/biomaqsad"),
        ],
        [
            InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'),
        ],
    ],
)

two_chanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 2-kanalga obuna", url="https://t.me/easy_python_uzb"),
        ],
        [
            InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data='check_subs'),
        ],
    ],
)