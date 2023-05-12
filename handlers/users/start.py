from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.personalData import PersonalData
from keyboards.default.startButtons import menuStart

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>", reply_markup=menuStart)

@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Sizning holatingiz None emas!!! ")
