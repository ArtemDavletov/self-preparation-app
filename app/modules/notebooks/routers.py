from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.modules.notebooks.schemas import NotebookSchema
from app.repository import notebooks_repo

router = APIRouter()

__all__ = (
    router,
)


@router.get(
    '/{user_id}',
    response_description='List notebooks'
)
def notebooks(
        user_id: int,
        db: Session = Depends(get_db)
):
    return notebooks_repo.get_notebooks(db=db, user_id=user_id)


@router.post(
    '/',
)
def add_notebook(
        user_id: int,
        notebook: NotebookSchema,
        db: Session = Depends(get_db)
):
    check_notebook = notebooks_repo.get_notebook(db=db, user_id=user_id, notebook_name=notebook.name)
    if check_notebook:
        return Response(status_code=418)

    return notebooks_repo.add_notebook(db=db, user_id=user_id, notebook=notebook)


@router.put(
    '/',
)
async def update_notebook():
    return Response(content='success')


@router.delete(
    '/',
)
async def delete_notebook():
    return Response(content='success')

