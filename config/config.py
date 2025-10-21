from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token:str


@dataclass
class LogsSettings:
        level:str
        format:str


@dataclass
class Config:
      bot:TgBot
      log:LogsSettings


def load_config(path:str| None=None):
      env=Env()
      env.read_env(".env")
      return Config(
            bot=TgBot(token=env("BOT_TOKEN")),
            log=LogsSettings(level=env("LOG_LEVEL"),format=env("LOG_FORMAT")),
      )
      