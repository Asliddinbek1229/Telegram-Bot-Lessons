from loader import dp, bot

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default.contact import kb_con


@dp.callback_query_handler(text="mycontact")
async def get_con(call: CallbackQuery):
    await call.message.answer("Marhamat kontaktingizni yuboring.", reply_markup=kb_con)

@dp.message_handler(content_types='contact')
async def contdact(msg: Message):
    contact = msg.contact
    await msg.answer(f"Rahmat, <b>{contact.full_name}</b>\n"
                     f"Sizning {contact.phone_number} raqamingiz qabul qilindi\nAdminimiz siz bilan bog'lanadi", reply_markup=ReplyKeyboardRemove())