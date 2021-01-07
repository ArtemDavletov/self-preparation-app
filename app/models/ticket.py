from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.settings.database import Base


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, unique=True, primary_key=True, index=True)
    questions = Column(String)
    answers = Column(String)
    notebook_id = Column(Integer, ForeignKey('notebooks.id'))

    notebook = relationship('Notebook', back_populates='ticket')
