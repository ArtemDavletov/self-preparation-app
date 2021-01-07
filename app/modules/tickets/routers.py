from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.modules.tickets.schemas import TicketSchema
from app.repository import notebooks_repo

router = APIRouter()

__all__ = (
    router,
)


@router.get('/{notebook_name}',
            description='Return all tickets from notebook',
            response_description='List of tickets')
def tickets(
        user_id: str,
        notebook_name: str,
        db: Session = Depends(get_db)
):
    """Return all tickets from notebook"""
    return notebooks_repo.get_tickets_from_notebook(db=db, user_id=user_id, notebook_name=notebook_name)


@router.get('/{ticket_question}',
            description='Get ticket',
            response_description='Return ticket')
def get_ticket(
        user_id: str,
        ticket_question: str,
        db: Session = Depends(get_db)
):
    """Search ticket by name"""
    return notebooks_repo.get_ticket(db=db, user_id=user_id, ticket_question=ticket_question)


@router.post(
    '/',
    description='Add ticket to notebook',
    response_description='Return created ticket'
)
def add_ticket(
        user_id: str,
        ticket: TicketSchema,
        db: Session = Depends(get_db)
):
    """Add ticket to notebook"""
    notebook = notebooks_repo.get_notebook(db=db, user_id=user_id, notebook_name=ticket.notebook_name)
    if notebook is None:
        return Response(status_code=418)

    return notebooks_repo.add_ticket_to_notebook(db=db, notebook_id=notebook.id, ticket=ticket)


@router.put(
    '/',
    description='Update ticket in notebook',
    response_description='Return updated ticket'
)
def update_ticket():
    """Update ticket in notebook"""
    return Response(content='success')


@router.delete(
    '/',
    description='Delete ticket from notebook',
    response_description='Return status of operation'
)
def delete_ticket(
        user_id: str,
        notebook_name: str,
        ticket_question: str,
        db: Session = Depends(get_db)
):
    """Delete ticket from notebook"""
    return notebooks_repo.delete_ticket_from_notebook(db=db, user_id=user_id,
                                                      notebook_name=notebook_name, ticket_question=ticket_question)
