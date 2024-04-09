import asyncpg

from core.settings import settings


async def create_pool():
    return await asyncpg.create_pool(
        user=settings.databases.user,
        password=settings.databases.password,
        database=settings.databases.database,
        host=settings.databases.host,
        port=settings.databases.port,
        command_timeout=settings.databases.command_timeout,
    )


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def set_command(self, user_id: int, command: str, members: str) -> None:
        query = "insert into commands (id_captain, command_name, members)" \
                f"values ('{user_id}', '{command}', '{members}')" \

        await self.connector.execute(query)

    async def get_all_commands(self):
        query = "SELECT (id_captain) FROM commands"
        return await self.connector.fetch(query)

    async def set_answer(self, user_id: int, answer: str) -> None:
        query = (f"INSERT INTO game (commands_id_captain, answer)"
                 f"VALUES ('{user_id}', '{answer}')")
        await self.connector.execute(query)

    async def get_all_answers(self):
        query = "SELECT id_captain FROM game"
