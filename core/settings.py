from dataclasses import dataclass

from environs import Env


@dataclass
class Bots:
    bot_token: str


@dataclass
class DataBase:
    user: str
    password: str
    database: str
    host: str
    port: int
    command_timeout: int


@dataclass
class Settings:
    bots: Bots
    databases: DataBase
    admins: list


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str('TOKEN'),
        ),
        databases=DataBase(
            user=env.str('DBNAME'),
            password=env.str('PASSWORD'),
            database=env.str('DATABASE'),
            host=env.str('HOST'),
            port=env.int('PORT'),
            command_timeout=env.int('TIMEOUT'),
        ),
        admins=[int(i) for i in env.str('ADMINS').split()]
    )


settings = get_settings('.env')
