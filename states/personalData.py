from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullName = State()
    email = State()
    phoneNum = State()