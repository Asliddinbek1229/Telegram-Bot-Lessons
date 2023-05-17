from aiogram import types
from filters import IsGroup, AdminFilter
from aiogram.types.message_entity import MessageEntity

import logging
import json

from loader import dp, bot

@dp.message_handler(IsGroup(), content_types=types.ContentType.ANY)
async def remove_ads_(msg: types.Message):
    pass