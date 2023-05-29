# from loader import dp
# from aiogram.types import ContentType, Message
# from pathlib import Path

# dowload_path = Path().joinpath("dowloads", 'catergories')
# dowload_path.mkdir(parents=True, exist_ok=True)

# @dp.message_handler()
# async def text_handler(msg: Message):
#     await msg.reply("Siz matn yubordingiz")

# @dp.message_handler(content_types=ContentType.DOCUMENT)
# async def doc_handler(msg: Message):
#     await msg.document.download(destination=dowload_path)
#     file_id = msg.document.file_id
#     await msg.reply("Siz document yubordingiz"
#                     f"\nFile_id > {file_id}")
    
# # @dp.message_handler(content_types=ContentType.VIDEO)
# @dp.message_handler(content_types='video')
# async def video_handler(msg: Message):
#     await msg.video.download(destination=dowload_path)
#     await msg.reply("Video qabul qilindi\n"
#                     f"{msg.video.file_id}")
    
# @dp.message_handler(content_types='photo')
# async def photo_handler(msg: Message):
#     await msg.photo[-1].download(destination=dowload_path)
#     await msg.reply("Rasm qabul qilindi\n"
#                     f"File_id {msg.photo[-1].file_id}")
    

# @dp.message_handler(content_types=ContentType.ANY)
# async def any_handler(msg: Message):
#     await msg.reply(
#         f"{msg.content_type} qabul qilindi."
#     )