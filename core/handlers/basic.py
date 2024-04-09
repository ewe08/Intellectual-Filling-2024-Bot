from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.methods.send_message import SendMessage

from core.settings import settings
from core.utils.dbconnect import Request
from core.utils.statesform import RegisterForm
from core.keyboards.register import register_keyboard
from core.keyboards.admin_keyboard import start_keyboard
from core.keyboards.user_keyboard import user_keyboard


async def start_chat(message: Message):
    if message.from_user.id in settings.admins:
        await message.reply(
            'Решай когда начнем',
            reply_markup=start_keyboard,
        )
    else:
        await message.reply(
            'Добро пожаловать на интеллектуальный конкурс! Пройдите регистрацию команды.',
            reply_markup=register_keyboard,
        )


async def get_command_name(message: Message, state: FSMContext):
    await message.answer(f"Введите название команды:")
    await state.set_state(RegisterForm.GET_COMMAND_NAME)


async def set_command_name(message: Message, state: FSMContext):
    await message.answer(f'Вы успешно назвали команду "{message.text}"')
    await state.update_data(command_name=message.text)
    await message.answer(f'Теперь введите участников через пробел:')
    await state.set_state(RegisterForm.GET_MEMBERS)


async def get_members(message: Message, request: Request, state: FSMContext):
    context_data = await state.get_data()
    command_name = context_data.get('command_name')
    members = message.text
    await message.answer(f'Вы успешно зарегистрировали команду "{command_name}"\n'
                         f'Участники: {members}')
    await request.set_command(message.from_user.id, command_name, members)
    await state.clear()
    for admin in settings.admins:
        await SendMessage(text=f'Команда "{command_name}"\n'
                               f'Участники: {members}', chat_id=admin)
    await waiting_organizer(message)


async def waiting_organizer(message: Message):
    await message.answer('Ждем начала...')
