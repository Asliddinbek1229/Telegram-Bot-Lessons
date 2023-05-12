from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                 keyboard=[
                                     [
                                         KeyboardButton(text="0️⃣1️⃣ Kirish"),
                                         KeyboardButton(text="0️⃣2️⃣ Kerakli darturlar"),
                                         KeyboardButton(text="0️⃣3️⃣ Hello world"),
                                     ],
                                     [
                                         KeyboardButton(text='⬅️ ortga'),
                                         KeyboardButton(text='⏪ boshiga'),
                                     ],
                                 ],
                                 )