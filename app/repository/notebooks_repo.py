import logging
from typing import Optional, List

from sqlalchemy.orm import Session

from ..models.notebook import Notebook
from ..models.ticket import Ticket
from ..modules.notebooks.schemas import NotebookSchema
from ..modules.tickets.schemas import CreateTicketSchema

logger = logging.getLogger('notebooks_repository')


async def get_notebooks(
        db: Session,
        user_id: str
) -> Optional[List[Notebook]]:
    try:
        return db.query(Notebook).filter(Notebook.user_id == user_id).all()
    except Exception as e:
        logger.error(e)
        return None


async def get_notebook(
        db: Session,
        user_id: str,
        notebook_name: str
) -> Optional[Notebook]:
    try:
        return db.query(Notebook).filter(Notebook.name == notebook_name,
                                         Notebook.user_id == user_id).first()
    except Exception as e:
        logger.error(e)
        return None


async def add_notebook(
        db: Session,
        user_id: str,
        notebook: NotebookSchema
) -> Optional[Notebook]:
    try:
        db_notebook = Notebook(name=notebook.notebook_name, user_id=user_id)

        db.add(db_notebook)
        db.commit()
        db.refresh(db_notebook)

        return db_notebook
    except Exception as e:
        logger.error(e)
        return None


async def delete_notebook(
        db: Session,
        user_id: str,
        notebook_name: str
) -> bool:
    try:
        db.query(Notebook).delete(Notebook.name == notebook_name and
                                  Notebook.user_id == user_id)
        db.commit()

        return True
    except Exception as e:
        logger.error(e)
        return False


async def add_ticket_to_notebook(
        db: Session,
        notebook_id: int,
        ticket: CreateTicketSchema
) -> Optional[Ticket]:
    try:
        db_ticket = Ticket(question=ticket.question, answer=ticket.answer, notebook_id=notebook_id)

        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)

        return db_ticket
    except Exception as e:
        logger.error(e)
        return None


async def delete_ticket_from_notebook(
        db: Session,
        user_id: str,
        notebook_name: str,
        ticket_question: str
) -> bool:
    try:
        db.query(Ticket).delete(Ticket.question == ticket_question and
                                Ticket.notebook.name == notebook_name and
                                Ticket.notebook.user_id == user_id)
        db.commit()
        return True
    except Exception as e:
        logger.error(e)
        return False


async def get_tickets_from_notebook(
        db: Session,
        user_id: str,
        notebook_name: str
):
    try:
        return db.query(Notebook).filter(Notebook.name == notebook_name,
                                         Notebook.user_id == user_id).first().ticket
    except Exception as e:
        logger.error(e)
        return None


async def get_ticket(
        db: Session,
        user_id: str,
        notebook_name: str,
        ticket_question: str
):
    try:
        return db.query(Ticket).filter(Ticket.question == ticket_question and
                                       Ticket.notebook.name == notebook_name and
                                       Ticket.notebook.user_id == user_id).first()
    except Exception as e:
        logger.error(e)
        return None
