import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.middlewares.dbmiddleware import DbSession
from core.settings import settings
from core.utils.dbconnect import create_pool
from core.utils.statesform import RegisterForm
from core.handlers.basic import start_chat, get_command_name, set_command_name, get_members


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(name)s - '
               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    await bot.delete_webhook(drop_pending_updates=True)

    pull_connect = await create_pool()
    dp = Dispatcher()
    dp.update.middleware.register(DbSession(pull_connect))
    dp.message.register(start_chat, Command(commands=['start']))

    dp.message.register(get_command_name, F.text == 'Регистрация команды')

    dp.message.register(set_command_name, RegisterForm.GET_COMMAND_NAME)
    dp.message.register(get_members, RegisterForm.GET_MEMBERS)

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
