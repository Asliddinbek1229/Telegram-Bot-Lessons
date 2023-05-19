import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.subscription import chek_button
from keyboards.default.startMenuKeyboard import menuStart
from utils.misc.subscription import chek
from data.config import CHANNELS

from filters import IsPrivate

from loader import dp, bot

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    subscription = int()
    result = str()
    for channel in CHANNELS:
        status = await chek(user_id=message.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            subscription += 1

    if subscription == 2:
        await message.answer("Quyidagilardan birini tanlang👇👇👇", reply_markup=menuStart)
    else:
        # channels_format = str()
        # for channel in CHANNELS:
            # chat = await bot.get_chat(channel)
            # invite_link = await chat.export_invite_link()
            # # logging.info(invite_link)
            # channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

        await message.answer(f"Quyidagi kanallarga obuna bo'ling: 👇",
                        reply_markup=chek_button,
                        disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    subscription = int()
    for channel in CHANNELS:
        status = await chek(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            subscription += 1

    if subscription == 2:
        await call.message.answer("Siz botdan foydalanishingiz mumkin", reply_markup=menuStart)
    else:
        await call.message.answer("Botdan foydalanish uchun barcha kanallarga obuna bo'ling!!!", disable_web_page_preview=True)
