from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from . import schemas
from .schemas import Token
from ...settings.database import get_db
from ...lib import security
from ...settings.settings import settings

router = APIRouter()

__all__ = (
    router,
)


@router.post(
    '/register',
)
async def register(
        user: schemas.RegisterSchema,
        db: Session = Depends(get_db)
):
    return Response(content='success')


@router.post(
    '/login'
)
async def login(
        user: schemas.LoginSchema,
        db: Session = Depends(get_db)
):
    return Response(content='success')


@router.post(
    '/refresh'
)
async def refresh(
        user: schemas.RefreshSchema,
        db: Session = Depends(get_db)
):
    return Response(content='success')


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = security.authenticate_user(security.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
