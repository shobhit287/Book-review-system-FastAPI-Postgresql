from pydantic import BaseModel, Field

class CreateReviewDto(BaseModel):
    review: str = Field(..., alias="review")

    class Config:
        validate_by_name = True
