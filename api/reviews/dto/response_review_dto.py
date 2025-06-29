from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class ReviewResponseDto(BaseModel):
    id: UUID = Field(..., alias="id")
    book_id: UUID = Field(..., alias="bookId")
    review: str = Field(..., alias="review")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")

    class Config:
        from_attributes = True
        validate_by_name = True
