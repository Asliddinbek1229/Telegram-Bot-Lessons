from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def build_keyboard(product_name):
    keys = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Xarid qilish', callback_data=f"product:{product_name}",)
            ],
        ],
    )
    return keys