import io

from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import AdminFilter, IsGroup
from loader import dp, bot



@dp.message_handler(IsGroup(), Command('set_photo', prefixes='!/'), AdminFilter())
async def set_group_photo(msg: types.Message):
    source_message = msg.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    # 1-usul
    await msg.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command('set_title', prefixes='!/'), AdminFilter())
async def set_group_title(msg: types.Message):
    source_message = msg.reply_to_message
    title = source_message.text
    # 2-usul
    await bot.set_chat_title(msg.chat.id, title=title)

@dp.message_handler(IsGroup(), Command('set_description', prefixes='!/'), AdminFilter())
async def set_group_description(msg: types.Message):
    source_message = msg.reply_to_message
    description = source_message.text
    await msg.chat.set_description(description=description)