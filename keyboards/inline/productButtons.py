from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Kurslar", callback_data='courses'),
            InlineKeyboardButton(text='📚 Kitoblar', callback_data='books'),
        ],
        [
            InlineKeyboardButton(text="🔗 Mohirdev sahifasiga o'tish", url="https://praktikum.mohirdev.uz")
        ],
        [
            InlineKeyboardButton(text='🔍 Qidirish', switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text='♻️ Ulashish', switch_inline_query="Zo'r bot ekan"),
        ],
    ],
)

# Kurslar uchun Inline keyboard
# courseMenu = InlineKeyboardMarkup(row_width=1)
# python = InlineKeyboardButton(text='🐍 Python dasturlash asoslari', callback_data='python')
# courseMenu.insert(python)
# django = 

courseMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🐍 Python dasturlash asoslari', callback_data='python'),
        ],
        [
            InlineKeyboardButton(text='🌐 Django Web dasturlash', callback_data='django'),
        ],
        [
            InlineKeyboardButton(text='🤖 Mukammal telegram bot', callback_data='bot'),
        ],
        [
            InlineKeyboardButton(text="📈 Ma'lumotlar tuzilmasi va algoritmlar", callback_data='mtva'),
        ],
        [
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)


# xarid tugmasi
# python uchun
pythonMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xarid qilish', url="https://old.mohirdev.uz"),
        ],
    ],
)


# django uchun
djangoMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xarid qilish', url="https://old.mohirdev.uz"),
        ],
    ],
)

# bot uchun
botMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xarid qilish', url="https://old.mohirdev.uz"),
        ],
    ],
)

# algoritm uchun
algoritmMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xarid qilish', url="https://old.mohirdev.uz"),
        ],
    ],
)


# Kitoblar uchun

booksMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📔 Python dasturlash asoslari', callback_data="bookPython"),
        ],
    ],
)


buyPythonBook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data='buy_bookPython'),
            InlineKeyboardButton(text='ortga', callback_data='ortga')
        ],
    ],
)

buyPythonBook2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sahifaga o'tish", url="https://old.mohirdev.uz")
        ]
    ]
)