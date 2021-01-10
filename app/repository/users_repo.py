import logging
from typing import Optional

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from ..models.user import User
from ..modules.users.schemas import UserSchema, UpdateUserSchema

logger = logging.getLogger('user_repository')

# TODO: Think about where better to place
pwd_context = CryptContext(schemes=['sha256_crypt', 'des_crypt'], deprecated='auto')


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(
        db: Session,
        login: str,
        email: str
) -> Optional[User]:
    try:
        # FIXME: Function should return User
        return db.query(*[c for c in User.__table__.c if c != 'password']).filter(
            User.email == email or User.login == login).first()
    except Exception as e:
        logger.error(e)
        return None


async def create_user(
        db: Session,
        user: UserSchema
) -> Optional[User]:
    # TODO: Necessary to add hashing password
    # TODO: Think about how to return User without password

    try:
        db_user = User(login=user.login,
                       firstname=user.firstname,
                       lastname=user.lastname,
                       email=user.email,
                       password=get_password_hash(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
    except Exception as e:
        logger.error(e)
        return None


async def update_user(
        db: Session,
        user_id: str,
        values: UpdateUserSchema
) -> Optional[User]:
    try:
        db_user = db.query(User).filter(User.id == user_id).update(values)
        db.commit()

        return db_user
    except Exception as e:
        logger.error(e)
        return None


async def delete_user(
        db: Session,
        user_id: str
) -> bool:
    try:
        db.query(User).delete(User.id == user_id)
        db.commit()
        return True
    except Exception as e:
        logger.error(e)
        return False
