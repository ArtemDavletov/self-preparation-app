from passlib.context import CryptContext
from pydantic import BaseSettings
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class CommonSettings(BaseSettings):
    APP_NAME: str = str(os.environ.get('APP_NAME'))
    DEBUG_MODE: bool = str(os.environ.get('DEBUG_MODE'))

    PWD_CONTEXT = CryptContext(schemes=['sha256_crypt', 'des_crypt'], deprecated='auto')
    SECRET_KEY = "fdcf93380b3ce32b084e9c2d483224ad395c3219fb7fd250932e3d339870069a4a3a41b1932a2864418a7065b3f72b5d"
    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 43200


class ServerSettings(BaseSettings):
    APP_HOST: str = str(os.environ.get('APP_HOST'))
    APP_PORT: int = int(os.environ.get('APP_PORT'))


class DatabaseSettings(BaseSettings):
    DB_URL: str = str(os.environ.get('DB_URL'))
    DB_NAME: str = str(os.environ.get('DB_NAME'))


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
