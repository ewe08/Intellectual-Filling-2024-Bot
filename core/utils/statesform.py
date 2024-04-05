from aiogram.fsm.state import StatesGroup, State


class RegisterForm(StatesGroup):
    GET_COMMAND_NAME = State()
    GET_MEMBERS = State()


class AnswerForm(StatesGroup):
    GET_ANSWER = State()

