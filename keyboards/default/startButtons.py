from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuStart = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                keyboard=[
                                    [
                                        KeyboardButton(text="Contact", request_contact=True),
                                        KeyboardButton(text="Location", request_location=True),
                                    ],
                                ],
                                )