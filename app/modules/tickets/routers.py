from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session

from ...settings.database import get_db
from .schemas import CreateTicketSchema
from ...repository import notebooks_repo
from . import schemas

router = APIRouter()

__all__ = (
    router,
)


@router.get('/{user_id}/{notebook_name}',
            description='Return all tickets from notebook',
            response_description='List of tickets')
async def get_tickets(
        user_id: str,
        notebook_name: str,
        db: Session = Depends(get_db)
):
    """Return all tickets from notebook"""
    return await notebooks_repo.get_tickets_from_notebook(db=db, user_id=user_id, notebook_name=notebook_name)


@router.get('/{user_id}/{notebook_name}/{ticket_question}',
            description='Get ticket',
            response_description='Return ticket')
async def get_ticket(
        user_id: str,
        notebook_name: str,
        ticket_question: str,
        db: Session = Depends(get_db)
):
    """Search ticket by name"""
    return await notebooks_repo.get_ticket(db=db, user_id=user_id, notebook_name=notebook_name,
                                           ticket_question=ticket_question)


@router.post(
    '/{user_id}',
    description='Add ticket to notebook',
    response_description='Return created ticket'
)
async def add_ticket(
        user_id: str,
        request: CreateTicketSchema,
        db: Session = Depends(get_db)
):
    """Add ticket to notebook"""
    notebook = await notebooks_repo.get_notebook(db=db, user_id=user_id, notebook_name=request.notebook_name)
    if notebook is None:
        return Response(status_code=418)

    return await notebooks_repo.add_ticket_to_notebook(db=db, notebook_id=notebook.id, ticket=request)


@router.put(
    '/{user_id}',
    description='Update ticket in notebook',
    response_description='Return updated ticket'
)
async def update_ticket(
        user_id: str,
        request: schemas.UpdateTicketSchema,
        db: Session = Depends(get_db)
):
    """Update ticket in notebook"""
    # TODO: Create update function

    return Response(content='success')


@router.delete(
    '/{user_id}',
    description='Delete ticket from notebook',
    response_description='Return status of operation'
)
async def delete_ticket(
        user_id: str,
        request: schemas.DeleteTicketSchema,
        db: Session = Depends(get_db)
):
    """Delete ticket from notebook"""
    return await notebooks_repo.delete_ticket_from_notebook(db=db, user_id=user_id,
                                                            notebook_name=request.notebook_name,
                                                            ticket_question=request.ticket_question)
