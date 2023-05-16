from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandSettings
from states.personalData import PersonalData

from filters import IsPrivate

from loader import dp

@dp.message_handler(IsPrivate(), CommandSettings())
async def setting(msg: types.Message):
    text = "Sozlamalar"
    await msg.answer(text)