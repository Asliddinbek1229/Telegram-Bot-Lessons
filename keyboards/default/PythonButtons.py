from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 keyboard=[
                                     [
                                         KeyboardButton(text="0️⃣1️⃣ String"),
                                         KeyboardButton(text="0️⃣2️⃣ Integers"),
                                         KeyboardButton(text="0️⃣3️⃣ List"),
                                     ],
                                     [
                                         KeyboardButton(text='⬅️ ortga'),
                                     ],
                                 ],
                                 )