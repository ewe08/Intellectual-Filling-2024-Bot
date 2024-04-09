from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Старт',
            ),
        ]
    ],
    resize_keyboard=True,
)

vote_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Начать голосование',
            ),
        ]
    ],
    resize_keyboard=True,
)

end_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Следующий раунд',
            ),
            KeyboardButton(
                text='Закончить'
            )
        ]
    ],
    resize_keyboard=True,
)