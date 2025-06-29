import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, DateTime, Column, Text, func

from app.db import Base
class BooksModel(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(150), nullable= False)
    author = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)

    created_at = Column(DateTime, default= func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
       return f"Book : {self.title}"