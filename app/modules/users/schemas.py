from typing import Optional

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
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


class UpdateUserSchema(BaseModel):
    login: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    password: Optional[str]

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
