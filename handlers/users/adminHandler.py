from aiogram import types
# import datetime
import asyncio

from data.config import ADMINS
from loader import db, dp, bot

@dp.message_handler(text="/all_users", user_id=ADMINS)
async def get_all_users(msg: types.Message):
    users = db.select_all_users()
    await msg.answer((users))

@dp.message_handler(text='/reklama', user_id=ADMINS)
async def send_ad_all_to(msg: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Rekalma")
        # datetime.time.sleep(1)
        asyncio.sleep(1)


@dp.message_handler(text='/cleandb', user_id=ADMINS)
async def get_all_users(msg: types.Message):
    db.delete_users()
    await msg.answer("Baza tozalandi")