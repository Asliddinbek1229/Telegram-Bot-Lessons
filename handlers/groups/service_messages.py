from aiogram import types
from filters import IsGroup
from loader import dp, bot



@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(msg: types.Message):
    # members = ", ".join([m.get_mention(as_html=True) for m in msg.new_chat_members])
    for m in msg.new_chat_members:
        members = ", ".join([m.get_mention(as_html=True)])
    text = "<b>Guruhimizda yangi foydalanuvchi bor</b>\n"
    text += f"Assalomu alaykum <b>{members}!</b> guruhga xush kelibsiz.\n\n"
    text += "<i>Eslatib o'taman guruhda haqoratli so'zlar ishlatish ta'qiqlanadi!!!</i>"
    await msg.answer(text)

@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def lef_member(msg: types.Message):
    if msg.left_chat_member.id == msg.from_user.id:
        await msg.answer(f"<b>{msg.left_chat_member.get_mention(as_html=True)} guruhni tark etdi</b>")
    elif msg.from_user.id == (await bot.me).id:
        return
    else:
        await msg.answer(f"{msg.from_user.get_mention(as_html=True)} {msg.left_chat_member.full_name}ni guruhdan haydadi.")