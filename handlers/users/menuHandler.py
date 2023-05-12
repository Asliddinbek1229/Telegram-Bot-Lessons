from aiogram.types import Message
from aiogram.types import CallbackQuery
from keyboards.inline.productButtons import categoryMenu, courseMenu, pythonMenu, djangoMenu, botMenu, algoritmMenu, booksMenu,\
      buyPythonBook, buyPythonBook2

import logging

from loader import dp 


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(msg: Message):
    await msg.answer(
        "Mahsulot tanlang", reply_markup=categoryMenu
        )
    
@dp.callback_query_handler(text='courses')
async def buy_course(call: CallbackQuery):
    # callback_data = call.data
    # logging.info(f"{callback_data=}")
    # logging.info(f"{call.from_user.username=}")
    await call.message.answer("Kursni tanlang", reply_markup=courseMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='python')
async def buy_python(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.answer(
        "Siz Python dasturlash asoslari kursini tanladingiz", 
        reply_markup=pythonMenu
        )
    await call.answer(cache_time=60)



@dp.callback_query_handler(text='ortga')
async def back_menu(call: CallbackQuery):
    await call.message.answer(
        "Mahsulot tanlang",
        reply_markup=categoryMenu
    )
    await call.answer(cache_time=60)



@dp.callback_query_handler(text='django')
async def buy_django(call: CallbackQuery):
    await call.message.answer(
        "Siz Djangoda web dasturlash kursini tanladingiz", 
        reply_markup=djangoMenu
        )
    await call.answer(cache_time=60)

    

@dp.callback_query_handler(text='bot')
async def buy_django(call: CallbackQuery):
    await call.message.answer(
        "Siz Djangoda web dasturlash kursini tanladingiz", 
        reply_markup=botMenu
        )
    await call.answer(cache_time=60)

    

@dp.callback_query_handler(text='mtva')
async def buy_django(call: CallbackQuery):
    await call.message.answer(
        "Siz Ma'lumotlar tuzilmasi va algoritmlar kursini tanladingiz", 
        reply_markup=algoritmMenu
        )
    await call.answer(cache_time=60)

    

@dp.callback_query_handler(text="books")
async def select_books(call: CallbackQuery):
    await call.message.answer(
        "Kitoblardan birini tanlang",
        reply_markup=booksMenu
    )
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="bookPython")
async def buy_books(call: CallbackQuery):
    await call.message.answer(
        "Quyidagilardan birini tanlang",
        reply_markup=buyPythonBook
    )
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="buy_bookPython")
async def Link(call: CallbackQuery):
    await call.message.answer(
        "Kitobni quyidagi sahifadan topishingiz mumkin",
        reply_markup=buyPythonBook2
    )
    await call.answer(cache_time=60)