from aiogram import types
from states.personalData import PersonalData

from filters import IsPrivate

from loader import dp

@dp.message_handler(IsPrivate(), commands='info_html')
async def bot_help(message: types.Message):
    text = (
        f"<b>Assalomu alaykum {message.from_user.full_name}</b>\n"
    )
    text += ("<i>Bu egri matn</i>\n")
    text += ("<u>Bu ostiga chizilgan matn</u>\n")
    text += ("<s>Bu o'chirilgan matn</s>\n")
    text += ("<code>print (\'Hello world\')</code> Bu kod format\n")
    text += ("<a href=\'https://t.me/Asliddinbek_official\'> Asliddinbek Dagaraliyev</a>")
    
    await message.answer(text)