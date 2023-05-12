from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu

from loader import dp

@dp.message_handler(Command('menu'))
async def menu_kb(msg: Message):
    await msg.answer(f"Kurslardan birini tanlang!", reply_markup=menu)


@dp.message_handler(Text(equals='Telegram bot kursi'))
async def tg_bot(msg: Message):
    await msg.answer("https://t.me/Asliddinbek_official")


