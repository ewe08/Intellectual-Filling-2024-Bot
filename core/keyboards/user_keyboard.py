from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Дать ответ',
            ),
        ]
    ],
    resize_keyboard=True,
)


