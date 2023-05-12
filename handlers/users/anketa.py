from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData
from handlers.users import help, start


@dp.message_handler(Command("anketa"), state=None)
async def enter_test(msg: types.Message):
    await msg.answer("To'liq ismingizni kiriting")
    await PersonalData.fullName.set()

@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    await state.update_data(
        {'name':fullname}
    )
    await msg.answer("Emailingizni kiriting")
    await PersonalData.email.set()

@dp.message_handler(state=PersonalData.email)
async def answer_email(msg: types.Message, state: FSMContext):
    email = msg.text

    await state.update_data(
        {"email":email}
    )

    await msg.answer("Telefon raqamingizni kiriting")
    await PersonalData.phoneNum.set()

@dp.message_handler(state=PersonalData.phoneNum)
async def answer_number(msg: types.Message, state: FSMContext):
    phoneNum = msg.text

    await state.update_data(
        {'phone':phoneNum}
    )

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    message = "Quyidagi ma'lumotlar qabul qilindi\n"
    message += f"Ismingiz: {name}\n"
    message += f"Email manzilingiz: {email}\n"
    message += f"Telefon raqamingiz: {phone}"
    await msg.answer(message)

    await state.finish()
