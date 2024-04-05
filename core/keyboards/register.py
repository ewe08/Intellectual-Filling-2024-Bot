from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Регистрация команды',
            ),
        ]
    ],
    resize_keyboard=True,
)