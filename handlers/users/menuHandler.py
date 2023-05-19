from aiogram.types import Message
from aiogram.types import CallbackQuery
from keyboards.inline.productButtons import categoryMenu, courseMenu, pythonMenu, djangoMenu, botMenu, algoritmMenu, booksMenu, \
      buyPythonBook, buyDjangoBook, buyFrontBook, buyHtmlBook, buyJsBook
from keyboards.inline.callback_data import course_callback, book_callback, book_shop_callback

from filters import IsPrivate

import logging

from loader import dp 


@dp.message_handler(IsPrivate(), text_contains="Mahsulotlar")
async def select_category(msg: Message):
    await msg.answer(
        "Mahsulot tanlang", reply_markup=categoryMenu
        )
    await msg.delete()
    

@dp.message_handler(IsPrivate(), text="📃 Qo'llanma")
async def manual(msg: Message):
    text = "<b>Admin bilan bog'lanish:</b>👇\n"
    text += "https://t.me/Asliddinbek_official"
    await msg.answer(text)


    
@dp.callback_query_handler(text='courses')
async def buy_course(call: CallbackQuery):
    # callback_data = call.data
    # logging.info(f"{callback_data=}")
    # logging.info(f"{call.from_user.username=}")
    await call.message.edit_text("Kursni tanlang", reply_markup=courseMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name="python"))
async def buy_python(call: CallbackQuery):
    callback_data = call.data
    # logging.info(f"{callback_data=}")
    # logging.info(f"{call.from_user.username=}")
    await call.message.edit_text(
        "Siz Python dasturlash asoslari kursini tanladingiz", 
        reply_markup=pythonMenu
        )
    await call.answer(cache_time=60)



@dp.callback_query_handler(text='ortga')
async def back_menu(call: CallbackQuery):
    await call.message.edit_text("Mahsulot tanlang", reply_markup=categoryMenu)
    await call.answer(cache_time=60)



@dp.callback_query_handler(course_callback.filter(item_name='django'))
async def buy_django(call: CallbackQuery):
    await call.message.edit_text(
        "Siz Djangoda web dasturlash kursini tanladingiz", 
        reply_markup=djangoMenu
        )
    await call.answer(cache_time=60)

    

@dp.callback_query_handler(course_callback.filter(item_name='bot'))
async def buy_django(call: CallbackQuery):
    await call.message.edit_text(
        "Siz Djangoda web dasturlash kursini tanladingiz", 
        reply_markup=botMenu
        )
    await call.answer(cache_time=60)

    

@dp.callback_query_handler(course_callback.filter(item_name='mtva'))
async def buy_django(call: CallbackQuery):
    await call.message.edit_text(
        "Siz Ma'lumotlar tuzilmasi va algoritmlar kursini tanladingiz", 
        reply_markup=algoritmMenu
        )
    await call.answer(cache_time=60)

    

@dp.callback_query_handler(text="books")
async def select_books(call: CallbackQuery):
    await call.message.edit_text(
        "Kitoblardan birini tanlang",
        reply_markup=booksMenu
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="bookPython"))
async def buy_books(call: CallbackQuery):
    await call.message.edit_text(
        "Quyidagilardan birini tanlang",
        reply_markup=buyPythonBook
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="book_js"))
async def buy_books(call: CallbackQuery):
    await call.message.edit_text(
        "Quyidagilardan birini tanlang",
        reply_markup=buyJsBook
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="book_html"))
async def buy_books(call: CallbackQuery):
    await call.message.edit_text(
        "Quyidagilardan birini tanlang",
        reply_markup=buyHtmlBook
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="book_front"))
async def buy_books(call: CallbackQuery):
    await call.message.edit_text(
        "Quyidagilardan birini tanlang",
        reply_markup=buyFrontBook
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="book_django"))
async def buy_books(call: CallbackQuery):
    await call.message.edit_text(
        "Quyidagilardan birini tanlang",
        reply_markup=buyDjangoBook
    )
    await call.answer(cache_time=60)




users = {}

@dp.callback_query_handler(book_shop_callback.filter(item_name="buypython"))
async def buy_python(call: CallbackQuery, callback_data: dict):
    user_shop = callback_data['item_name']
    # logging.info(f"{user_shop}")
    user_id = call.from_user.id
    # logging.info(f"{user_id=}")
    users[user_shop] = user_id
    logging.info(users)
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_shop_callback.filter(item_name="buyjs"))
async def buy_python(call: CallbackQuery, callback_data: dict):
    user_shop = callback_data['item_name']
    # logging.info(f"{user_shop}")
    user_id = call.from_user.id
    # logging.info(f"{user_id=}")
    users[user_shop] = user_id
    logging.info(users)
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_shop_callback.filter(item_name="buyhtml"))
async def buy_python(call: CallbackQuery, callback_data: dict):
    user_shop = callback_data['item_name']
    # logging.info(f"{user_shop}")
    user_id = call.from_user.id
    # logging.info(f"{user_id=}")
    users[user_shop] = user_id
    logging.info(users)
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_shop_callback.filter(item_name="buyfront"))
async def buy_python(call: CallbackQuery, callback_data: dict):
    user_shop = callback_data['item_name']
    # logging.info(f"{user_shop}")
    user_id = call.from_user.id
    # logging.info(f"{user_id=}")
    users[user_shop] = user_id
    logging.info(users)
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(book_shop_callback.filter(item_name="buydjango"))
async def buy_python(call: CallbackQuery, callback_data: dict):
    user_shop = callback_data['item_name']
    # logging.info(f"{user_shop}")
    user_id = call.from_user.id
    # logging.info(f"{user_id=}")
    users[user_shop] = user_id
    logging.info(users)
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)