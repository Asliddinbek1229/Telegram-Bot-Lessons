from aiogram import types
from loader import dp
from keyboards.inline.courses import aiogram_keys, python_keys
from data.courses_python import inline_result_python
from data.courses_telegram import inline_results_telegram



@dp.inline_handler(text='python')
async def empty_query(query: types.InlineQuery):
    await query.answer(
        inline_result_python
    )

@dp.inline_handler(text="telegram")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_telegram)


@dp.inline_handler(text='kurs')
async def started(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
        id='photo001',
        photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                caption="<b>Mukammal Telegram bot</b> kursi.",
                reply_markup=aiogram_keys
            ),
            types.InlineQueryResultPhoto(
                id="006",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                caption="<b>Python Dasturlash Asoslari</b> kursi.",
                reply_markup=python_keys
            ),
            types.InlineQueryResultVideo(
                id="007",
                video_url="https://streamable.com/ryeff4",
                caption="Million dolarlik g'oya",
                description="Go'yalarning asl bahosi",
                title="Million 💲 g'oya ",
                thumb_url="https://i.imgur.com/bY2XasE.png",
                mime_type="video/mp4",
            ),
        ],
    )

@dp.inline_handler()
async def empty_msg(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
        id="kurs001",
        title="Dasturlash asoslari",
        input_message_content=types.InputTextMessageContent(
        message_text="Dars uchun link: https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/"
        ),
        url="https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/",
        thumb_url="https://mohirdev.uz/images/hero.webp",
        description="Python eng zamonaviy dasturlash tili hisoblanadi."
            ),
            types.InlineQueryResultArticle(
        id="kurs002",
        title="Photoshop2023 darslari",
        input_message_content=types.InputTextMessageContent(
        message_text="Dars uchun link: https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/"
        ),
        url="https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/",
        thumb_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.adobe.com%2Fcontent%2Fdam%2Fcc%2Fus%2Fen%2Fproducts%2Fphotoshop%2Fphotoshop-1200x630.jpg",
        description="Photoshop biz bilan oson"
            ),
            types.InlineQueryResultArticle(
        id="kurs003",
        title="Te;egram bot kursi",
        input_message_content=types.InputTextMessageContent(
        message_text="Dars uchun link: https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/"
        ),
        url="https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/",
        thumb_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.techopedia.com%2Fwp-content%2Fuploads%2F2023%2F03%2F6e13a6b3-28b6-454a-bef3-92d3d5529007.jpeg",
        description="Telegram bot yaratishni o'rganing"
            ),
            types.InlineQueryResultArticle(
        id="kurs004",
        title="IQ darslari",
        input_message_content=types.InputTextMessageContent(
        message_text="Dars uchun link: https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/"
        ),
        url="https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/",
        thumb_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.adobe.com%2Fcontent%2Fdam%2Fcc%2Fus%2Fen%2Fproducts%2Fphotoshop%2Fphotoshop-1200x630.jpg",
        description="Photoshop biz bilan oson"
            ),
            types.InlineQueryResultArticle(
        id="kurs005",
        title="Photoshop2023 darslari",
        input_message_content=types.InputTextMessageContent(
        message_text="Dars uchun link: https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/"
        ),
        url="https://old.mohirdev.uz/courses/telegram/lesson/matn-rasm-video-keyboard-qaytaramiz/",
        thumb_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.adobe.com%2Fcontent%2Fdam%2Fcc%2Fus%2Fen%2Fproducts%2Fphotoshop%2Fphotoshop-1200x630.jpg",
        description="Photoshop biz bilan oson"
            ),
        ],
    )