from pydantic import BaseSettings
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = str(os.environ.get('DB_URL'))
    DB_NAME: str = str(os.environ.get('DB_NAME'))


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
