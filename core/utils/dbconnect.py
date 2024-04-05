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
        query = '''
        insert into commands (id_captain, command_name, members) values ('{0}', '{1}', '{2}')
        '''
        await self.connector.execute(query.format(user_id, command, members))
