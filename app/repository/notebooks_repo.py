import logging
from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.notebook import Notebook
from app.models.ticket import Ticket
from app.modules.notebooks.schemas import NotebookSchema
from app.modules.tickets.schemas import TicketSchema

logger = logging.getLogger('notebooks_repository')


def get_notebooks(
        db: Session,
        user_id: str
) -> Optional[List[Notebook]]:
    try:
        return db.query(Notebook).filter(Notebook.user_id == user_id).all()
    except Exception as e:
        logger.error(e)
        return None


def get_notebook(
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


def add_notebook(
        db: Session,
        user_id: str,
        notebook: NotebookSchema
) -> Optional[Notebook]:
    try:
        # check_notebook = get_notebook(db=db, user_id=user_id, notebook_name=notebook.name)
        # if check_notebook:
        #     return None

        db_notebook = Notebook(name=notebook.name, user_id=user_id)

        db.add(db_notebook)
        db.commit()
        db.refresh(db_notebook)

        return db_notebook
    except Exception as e:
        logger.error(e)
        return None


def add_ticket_to_notebook(
        db: Session,
        notebook_id: int,
        ticket: TicketSchema
) -> Optional[Ticket]:
    try:
        # notebook = get_notebook(db=db, user_id=user_id, notebook_name=ticket.notebook_name)
        # if notebook is None:
        #     return None

        db_ticket = Ticket(questions=ticket.question, answers=ticket.answer, notebook_id=notebook_id)

        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)

        return db_ticket
    except Exception as e:
        logger.error(e)
        return None


def delete_ticket_from_notebook(
        db: Session,
        user_id: str,
        notebook_name: str,
        ticket_question: str
) -> bool:
    try:
        db.query(Ticket).delete(Ticket.questions == ticket_question and
                                Ticket.notebook.name == notebook_name and
                                Ticket.notebook.user_id == user_id)
        db.commit()
        return True
    except Exception as e:
        logger.error(e)
        return False


def get_tickets_from_notebook(
        db: Session,
        user_id: str,
        notebook_name: str
):
    try:
        return get_notebook(db=db, user_id=user_id, notebook_name=notebook_name).ticket
    except Exception as e:
        logger.error(e)
        return None


def get_ticket(
        db: Session,
        user_id: str,
        ticket_question: str
):
    try:
        return db.query(Ticket).filter(Ticket.questions == ticket_question and
                                       Ticket.notebook.user_id == user_id).first()
    except Exception as e:
        logger.error(e)
        return None
