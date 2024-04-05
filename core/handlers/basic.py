from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.utils.dbconnect import Request
from core.utils.statesform import RegisterForm
from core.keyboards.register import register_keyboard


async def start_chat(message: Message):
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
    await message.answer(f'Теперь введите участников:')
    await state.set_state(RegisterForm.GET_MEMBERS)


async def get_members(message: Message, request: Request, state: FSMContext):
    context_data = await state.get_data()
    command_name = context_data.get('command_name')
    members = message.text
    await message.answer(f'Вы успешно зарегистрировали команду "{command_name}"\n'
                         f'Участники: {members}')
    await request.set_command(message.from_user.id, command_name, members)
    await state.clear()
    await waiting_organizer(message)


async def waiting_organizer(message: Message):
    await message.answer('Ждем начала...')
