import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.misc.subscription import chek
from loader import bot

from keyboards.inline.subscription import chek_button


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):        
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        result = "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling: 👇"
        final_status = True
        for channel in CHANNELS:
            status = await chek(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            

        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True, reply_markup=chek_button)
            raise CancelHandler()

