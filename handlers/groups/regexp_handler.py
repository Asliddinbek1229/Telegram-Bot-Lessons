# import logging
# from aiogram.dispatcher.filters import Regexp, Text, Command
# from filters import IsGroup, IsPrivate
# from aiogram import types

# from loader import dp


# url_regexp = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
# user_name = r"^[@-z0-9_.]{3,50}$"
# user_name2 = r"^[👉@-z0-9_-]{3,50}$"


# @dp.message_handler(IsGroup(), Regexp(url_regexp))
# async def remove_url(msg: types.Message):
#     await msg.delete()
#     await msg.answer(
#         f"Hurmatli <b>{msg.from_user.full_name}</b>\n\n"
#         f"Guruhda reklama tarqatish mumkin emas!!!"
#     )

# @dp.message_handler(IsGroup(), Regexp(user_name))
# async def remove_user_name(msg: types.Message):
#     await msg.delete()
#     await msg.answer(
#         f"Hurmatli <b>{msg.from_user.full_name}</b>\n\n"
#         f"Guruhda reklama tarqatish mumkin emas!!!"
#     )


# @dp.message_handler(IsGroup(), Regexp(user_name2))
# async def remove_user_name(msg: types.Message):
#     await msg.delete()
#     await msg.answer(
#         f"Hurmatli <b>{msg.from_user.full_name}</b>\n\n"
#         f"Guruhda reklama tarqatish mumkin emas!!!"
#     )