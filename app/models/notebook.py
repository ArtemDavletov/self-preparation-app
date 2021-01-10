from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..settings.database import Base


class Notebook(Base):
    __tablename__ = 'notebooks'

    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    user = relationship('User', back_populates='notebooks')
    ticket = relationship('Ticket', back_populates='notebook')
