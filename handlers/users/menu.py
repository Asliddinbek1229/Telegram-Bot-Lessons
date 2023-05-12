from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.PythonButtons import menuPython

from loader import dp

@dp.message_handler(Command('menu'))
async def menu_kb(msg: Message):
    await msg.answer(f"Kurslardan birini tanlang!", reply_markup=menu)


@dp.message_handler(Text(equals='Telegram bot kursi'))
async def tg_bot(msg: Message):
    await msg.answer("https://t.me/Asliddinbek_official", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text("Python kurslari"))
async def python(msg: Message):
    await msg.answer("O'zingizga kerakli darsni belgilang!", reply_markup=menuPython)


@dp.message_handler(text="0️⃣1️⃣ String")
async def string(msg: Message):
    await msg.answer("String (matnlar) darslari bizning telegram kanalimizda", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="0️⃣2️⃣ Integers")
async def string(msg: Message):
    await msg.answer("Integers (Butun sonlar) darslari bizning telegram kanalimizda", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="0️⃣3️⃣ List")
async def string(msg: Message):
    await msg.answer("List (Ro'yxatlar) darslari bizning telegram kanalimizda", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="⬅️ ortga")
async def back(msg: Message):
    await msg.answer(f"Kurslardan birini tanlang!", reply_markup=menu)