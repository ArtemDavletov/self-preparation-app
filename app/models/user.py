import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.settings.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid.uuid4)
    login = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)

    notebooks = relationship('Notebook', back_populates='user')
