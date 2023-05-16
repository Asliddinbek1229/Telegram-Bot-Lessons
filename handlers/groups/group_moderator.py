import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot



# /ro yoki !ro (read-only) kommandalari uchun handler
# foydalanuvchini read-only yani faqat o'qish rejimiga o'tkazamiz
@dp.message_handler(IsGroup(), Command('ro', prefixes='!/'), AdminFilter())
async def read_only_mode(msg: types.Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    chat_id = msg.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(msg.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    

    """
    !ro
    !ro 5 # 5 sekundga
    !ro 5 test
    !ro test
    !ro test test test
    /ro
    /ro 5
    /ro 5 test
    /ro test
    """
    # 5 minutga izohsiz cheklash
    # !ro 5
    # command = '!ro' time = '50' comment = ['reklama', 'reklama', 'reklama']

    time = int(time)

    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await msg.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await msg.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await msg.answer(f"Xatolik! {err.args}")
        return
    
    await msg.answer(f"Foydalanuvchi <b>{msg.reply_to_message.from_user.full_name}</b> {time} minut yozish huquqidan mahrum etildi\n"
                     f"Sabab: <b>{comment}</b>"
                     )
    

@dp.message_handler(IsGroup(), Command('unro', prefixes='!/'), AdminFilter())
async def unro_read_only(msg: types.Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    chat_id = msg.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_send_polls=False,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )

    servise_message = await msg.reply("Xabar 5 sekunddan so'ng o'chib ketadi!")
    await asyncio.sleep(5)
    await msg.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await msg.reply(f"Foydalanuvchi <b>{member.full_name}</b> tiklandi!")



# foydalanuvchini ban qilish
@dp.message_handler(IsGroup(), Command('ban', prefixes="!/"), AdminFilter())
async def ban_user(msg: types.Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    chat_id = msg.chat.id
    await msg.chat.kick(user_id=member_id)

    await msg.answer(f"Foydalanuvchi <b>{member.full_name}</b> guruhdan haydaldi")
    service_message = await msg.reply("Xabar 5 sekunddan so'ng o'chadi!")

    await asyncio.sleep(5)
    await msg.delete()
    await service_message.delete()


# foydalanuvchini bandan ya'ni qora ro'yxatdan chiqarish (Foydalanuvchini bandan chiqara olmaymiz, o'zi qo'shilishi mumkin)
@dp.message_handler(IsGroup(), Command('unban', prefixes='!/'), AdminFilter())
async def unban_user(msg: types.Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    chat_id = msg.chat.id

    await msg.chat.unban(user_id=member_id)
    await msg.answer(f"Foydalanuvchi <b>{member.full_name}</b> bandan chiqarildi!")
    service_message = await msg.reply("Xabar 5 sekunddan so'ng o'chadi!")

    await asyncio.sleep(5)
    await msg.delete()
    await service_message.delete()
