import logging
from typing import Optional

from sqlalchemy.orm import Session

from app.models.user import User
from app.modules.users.schemas import UserSchema, UpdateUserSchema

logger = logging.getLogger('user_repository')


def get_user(
        db: Session,
        login: str,
        email: str
) -> Optional[User]:
    try:
        return db.query(User).filter(User.email == email or
                                     User.login == login).first()
    except Exception as e:
        logger.error(e)
        return None


def create_user(
        db: Session,
        user: UserSchema
) -> Optional[User]:
    # TODO: Necessary to add hashing password

    try:
        db_user = User(login=user.login,
                       firstname=user.firstname,
                       lastname=user.lastname,
                       email=user.email,
                       password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
    except Exception as e:
        logger.error(e)
        return None


def update_user(
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


def delete_user(
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
