import logging

from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import CHANNELS, ADMINS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from states.newpost import NewPost

users = {}
@dp.message_handler(Command('create_post'))
async def create_post(msg: Message):
    users['user'] = msg.from_user.id
    await msg.answer("Chop etish uchun post yuboring!!!")
    await NewPost.NewMessage.set()


@dp.message_handler(state=NewPost.NewMessage, content_types=types.ContentType.ANY)
async def enter_message(msg: Message, state: FSMContext):
    await state.update_data(text=msg.html_text, mention=msg.from_user.get_mention())
    await msg.answer("Postni tekshirish uchun adminga yuboraymi???", reply_markup=confirmation_keyboard)
    # await msg.delete()
    await NewPost.next()



@dp.callback_query_handler(post_callback.filter(action='post'), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
        # print(text, "\n", mention)
    
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("🚀 Post tekshirish uchun yuborildi. Tez orada javob olasiz")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi postni chop etmoqchi")
    await bot.send_message(ADMINS[0], text, parse_mode='HTML', reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action='cencel'), state=NewPost.Confirm)
async def cencel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post rad etildi.\n\n"
                              "<b>Yangi post yaratish uchun /create_post buyrug'ini ishga tushiring!!!</b>")
    

@dp.message_handler(state=NewPost.Confirm)
async def post_unkown(msg: Message):
    await msg.answer("Chop etish yoki Rad etish tugmalaridan birini tanlang!!!")


@dp.callback_query_handler(post_callback.filter(action='post'), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("✅ Chop etishga ruxsat berdingiz", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    chat = await bot.get_chat(CHANNELS[0])
    invite_link = await chat.export_invite_link()
    await bot.send_message(users["user"], text="<b>Postingiz tasdiqlandi</b>\n\n"
                           f"Postingiz kanalimizda ko'rishingiz mumkin <a href='{invite_link}'>{chat.title}</a>")
    # print(message)
    await message.send_copy(chat_id=target_channel)



@dp.callback_query_handler(post_callback.filter(action='cencel'), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("Post rad etildi", show_alert=True,)
    await call.message.edit_reply_markup()
    await bot.send_message(users["user"], "Postingiz yaroqsiz deb topildi")
