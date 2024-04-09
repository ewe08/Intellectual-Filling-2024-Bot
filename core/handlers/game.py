from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.methods.send_message import SendMessage
from pyatspi import state

from core.settings import settings
from core.utils.dbconnect import Request
from core.utils.statesform import AnswerForm
from core.keyboards.register import register_keyboard
from core.keyboards.admin_keyboard import start_keyboard, vote_keyboard, end_keyboard
from core.keyboards.user_keyboard import user_keyboard


async def start_game_admin(message: Message, state: FSMContext):
    await message.answer("Вводи cлово:")
    await state.set_state(AnswerForm.GET_QUESTION)


async def new_game_admin(message: Message, state: FSMContext):
    await start_game_admin(message, state)


async def get_question(message: Message, request: Request, state: FSMContext):
    await message.answer(f'Вы задали слово "{message.text}"')
    commands = (await request.get_all_commands())[0]
    for command in commands:
        await SendMessage(text=f"Задали слово {message.text}", chat_id=command, reply_markup=user_keyboard)
    await state.clear()


async def get_answer(message: Message, state: FSMContext):
    await message.answer('Вводите слово:')
    await state.set_state(AnswerForm.GET_ANSWER)


async def set_answer(message: Message, request: Request, state: FSMContext):
    await message.answer(f'Вы ответили "{message.text}"')
    # await request.set_answer(message.from_user.id, message.text)
    for admin in settings.admins:
        await SendMessage(text=f'Команда "{message.from_user.first_name}"\n'
                               f'их ответ: {message.text}', chat_id=admin, reply_markup=end_keyboard)
    await state.clear()


async def end_game(message: Message, state: FSMContext):
    await message.answer("сча новая будет")
    await start_game_admin(message, state)

