from pydantic import BaseModel, Field

class BookCreateDto(BaseModel):
    title: str = Field(..., alias="title")
    author: str = Field(..., alias="author")  
    description: str = Field(..., alias="description")

    class Config:
        validate_by_name = True
