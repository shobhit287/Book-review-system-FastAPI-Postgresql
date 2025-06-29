import uuid
from sqlalchemy import Column, ForeignKey, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

from app.db import Base

class ReviewModel(Base):
    __tablename__ =  "books_reviews"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False, index=True)
    review = Column(Text, nullable=False)

    created_at = Column(DateTime, default= func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
       return f"Review : {self.review}"