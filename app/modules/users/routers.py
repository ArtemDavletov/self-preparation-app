from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.modules.users.schemas import UserSchema, UpdateUserSchema
from app.repository import users_repo


router = APIRouter()

__all__ = (
    router,
)


@router.get('/{user_id}')
async def get_user(
        email: str,
        login: str,
        db: Session = Depends(get_db)
):
    return users_repo.get_user(db=db, email=email, login=login)


@router.post('/')
def create_user(
    user: UserSchema,
    db: Session = Depends(get_db)
):
    # FIXME: Move checking to UserSchema

    user_db = users_repo.get_user(db=db, email=user.email, login=user.login)
    if user_db is not None:
        return Response(status_code=418)

    return users_repo.create_user(db=db, user=user)


@router.put('/')
async def update_user(
        user_id: str,
        values: UpdateUserSchema,
        db: Session = Depends(get_db)
):
    return users_repo.update_user(db=db, user_id=user_id, values=values)


@router.delete('/')
async def delete_user(
    user_id: str,
    db: Session = Depends(get_db)
):
    return users_repo.delete_user(db, user_id=user_id)

