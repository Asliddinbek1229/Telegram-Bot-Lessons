from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback, book_shop_callback

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
            InlineKeyboardButton(text='🐍 Python dasturlash asoslari', callback_data=course_callback.new(item_name='python')),
        ],
        [
            InlineKeyboardButton(text='🌐 Django Web dasturlash', callback_data=course_callback.new(item_name='django')),
        ],
        [
            InlineKeyboardButton(text='🤖 Mukammal telegram bot', callback_data=course_callback.new(item_name='bot')),
        ],
        [
            InlineKeyboardButton(text="📈 Ma'lumotlar tuzilmasi va algoritmlar", callback_data=course_callback.new(item_name='mtva')),
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
            InlineKeyboardButton(text='👁 Kursni ko\'rish', url="https://old.mohirdev.uz"),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)


# django uchun
djangoMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👁 Kursni ko\'rish', url="https://old.mohirdev.uz"),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)

# bot uchun
botMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🛒 Xarid qilish', url="https://old.mohirdev.uz"),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)

# algoritm uchun
algoritmMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👁 Kursni ko\'rish', url="https://old.mohirdev.uz"),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)



# Kitoblar uchun
kitoblar = {
    "Python Dasturlash asoslari":"bookPython",
    "JavaScript asoslari":"book_js",
    "HTML da Dasturlash":"book_html",
    "Frontend Dasturlash":'book_front',
    "Web Dasturlash asoslari. Django":"book_django"
}


booksMenu = InlineKeyboardMarkup(row_width=1)
for key, valuae in kitoblar.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(valuae)))
booksMenu.insert(InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'))


buyPythonBook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Sotib olish", callback_data=book_shop_callback.new(item_name='buypython')),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)

buyJsBook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Sotib olish", callback_data=book_shop_callback.new(item_name='buyjs')),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)

buyHtmlBook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Sotib olish", callback_data=book_shop_callback.new(item_name='buyhtml')),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)

buyFrontBook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Sotib olish", callback_data=book_shop_callback.new(item_name='buyfront')),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)

buyDjangoBook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Sotib olish", callback_data=book_shop_callback.new(item_name='buydjango')),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)