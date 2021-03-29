from typing import Optional

from pydantic import validator
from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class RegisterSchema(BaseModel):
    login: str
    firstname: str
    lastname: str
    email: EmailStr
    password: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "login": "povar99",
                "firstname": "Povar",
                "lastname": "Povarov",
                "email": "example@gmail.com",
                "password": "123456qwerty",
            }
        }


class LoginSchema(BaseModel):
    login: Optional[str]
    email: Optional[EmailStr]
    password: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "login": "povar99",
                "email": "example@gmail.com",
                "password": "123456qwerty",
            }
        }

    @validator('login', 'email')
    def check_sum(cls, v):
        if (v[0] and v[1]) is None:
            raise ValueError('Login or password is incorrect')
        return v


class RefreshSchema(BaseModel):
    auth_token: str
    refresh_token: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "auth_token": "your_auth_token",
                "refresh_token": "your_refresh_token",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str
