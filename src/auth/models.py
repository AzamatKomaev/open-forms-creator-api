from sqlalchemy import String, DateTime, Integer, Text, Boolean
from sqlalchemy.sql import func

from core.database import Base
from core.utils import Column


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(Text, unique=True)
    name = Column(String(255), unique=True)
    type = Column(String(255), default='base')
    is_active = Column(Boolean, default=False, server_default="0")
    password = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User(email={self.email} name={self.name}>'

