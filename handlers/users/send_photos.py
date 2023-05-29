from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

from keyboards.inline.buy_color import buy_btn


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id(msg: types.Message):
    await msg.answer(msg.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_video(msg: types.Message):
    await msg.answer(msg.video.file_id)


@dp.message_handler(Command('logo'))
async def send_photo(msg: types.Message):
    album = types.MediaGroup()

    photo_id = "AgACAgIAAxkBAAIH6GR0ekSY0DJpKtMY9cybt25JwLc-AAJlyDEbeGmgS4D2bx2LybcnAQADAgADeQADLwQ"
    photo_file = InputFile(path_or_bytesio="photos/gepard.jpg")
    photo_url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.squarespace-cdn.com%2Fcontent%2Fv1%2F58d7e114725e25ffc9b24b5f%2F1513012471239-CBJXDA7MTWSKH1QSEZ21%2FPeeing%2Bcat.jpeg"
    video1 = "BAACAgIAAxkBAAIH5mR0ejmQbfrDntMWVG6-_kK69wr5AAJKLAACGfWgS5N4-kfufteTLwQ"

    album.attach_photo(photo=photo_file)
    album.attach_photo(photo=photo_id)
    album.attach_photo(photo=photo_url)
    album.attach_video(video=video1, caption="Bu MediaGroup klassi orqali yuborildi!")

    await msg.answer_media_group(album)


@dp.message_handler(Command('rang'))
async def send_photos(msg: types.Message):
    photo_id = "AgACAgIAAxkBAAIH_2R0jInrAeuC7tjHPIg1I7tDmF_VAAPJMRt4aaBLIfVMw0N_LxkBAAMCAANtAAMvBA"
    text = "<b>Uyingiz uchun sifatli va arzon bo'yoqlar</b>\n\n"
    text += "<i>Bo'yoqlarimiz orqali uyingizga joziba baxsh eting</i>\n"
    text += "📍 Manzillarimiz\n👉Sarqamish\n👉Chust tumani\n👉Toshkent shahri"
    await msg.reply_photo(photo_id, caption=text, reply_markup=buy_btn)
