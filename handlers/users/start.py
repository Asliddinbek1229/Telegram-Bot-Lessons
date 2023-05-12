import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.personalData import PersonalData
from keyboards.default.startMenuKeyboard import menuStart

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>", reply_markup=menuStart)
