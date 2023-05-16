from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personalData import PersonalData

from filters import IsPrivate

from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp(), state=None)
async def bot_help(message: types.Message):
    text = ("Qanday yordam kerak?",
            "Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/anketa - Shaxsiy anketani to'ldirish"
            )
    
    await message.answer("\n".join(text))

@dp.message_handler(IsPrivate(), CommandHelp(), state="*")
async def help_state(msg: types.Message):
    text = "Ism va familiyangizni kiriting! Iltmos"
    await msg.answer(text)
