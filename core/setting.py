from environs import Env
from dataclasses import dataclass


@dataclass
class Bot:
    bot_token: str
    admin_id: int


@dataclass
class Setting:
    bot: Bot


def get_settings(path: str) -> object:
    env = Env()
    env.read_env(path)

    return Setting(
        bot=Bot(
            bot_token=env.str('API_TOKEN'),
            admin_id=env.int('ADMIN_ID')
        )
    )


settings = get_settings('input.txt')
