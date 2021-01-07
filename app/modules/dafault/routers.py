from fastapi import APIRouter
from fastapi.responses import Response


router = APIRouter()

__all__ = (
    router,
)


@router.get('/')
async def route():
    return Response(content='success')


@router.get('/health')
async def health():
    return Response(content='success')

