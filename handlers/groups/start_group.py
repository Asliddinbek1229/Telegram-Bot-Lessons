from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup

from loader import dp


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    text = "<b>Guruhimizda yangi foydalanuvchi bir</b>\n"
    text += f"Assalomu alaykum <b>{message.from_user.full_name}!</b> guruhga xush kelibsiz.\n\n"
    text += "<i>Eslatib o'taman guruhda haqoratli so'zlar ishlatish ta'qiqlanadi!!!</b>"
    await message.answer(text)