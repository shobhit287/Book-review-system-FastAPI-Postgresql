from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class BookResponseDto(BaseModel):
    id: UUID = Field(..., alias="id")
    title: str = Field(..., alias="title")
    author: str = Field(..., alias="author")
    description: str = Field(..., alias="description")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")

    class Config:
        from_attributes = True
        validate_by_name = True
