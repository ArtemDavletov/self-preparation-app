from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session

from ...lib.security import get_current_active_user
from ...models.user import User
from ...settings.database import get_db
from ...repository import notebooks_repo
from . import schemas

router = APIRouter()

__all__ = (
    router,
)


@router.get(
    '/{user_id}',
    response_description='List notebooks'
)
async def notebooks(
        user_id: str,
        db: Session = Depends(get_db)
):
    return await notebooks_repo.get_notebooks(db=db, user_id=user_id)


@router.post(
    '/{user_id}',
)
async def add_notebook(
        request: schemas.NotebookSchema,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    check_notebook = await notebooks_repo.get_notebook(db=db, user_id=str(User.id), notebook_name=request.notebook_name)
    if check_notebook:
        return Response(status_code=418)

    return await notebooks_repo.add_notebook(db=db, user_id=str(User.id), notebook=request)


@router.put(
    '/{user_id}',
)
async def update_notebook(
        user_id: str,
        request: schemas.UpdateNotebookSchema
):
    # TODO: Realize endpoint
    return Response(content='success')


@router.delete(
    '/{user_id}',
)
async def delete_notebook(
        user_id: str,
        request: schemas.NotebookSchema
):
    # TODO: Realize endpoint
    return Response(content='success')
