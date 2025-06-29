from fastapi import APIRouter
from typing import List

from .dto.create_review_dto import CreateReviewDto
from .dto.response_review_dto import ReviewResponseDto
from .reviews_service import ReviewService

review_router = APIRouter(prefix="/books", tags=["Reviews"])

class ReviewController:
    @staticmethod
    @review_router.post("/{book_id}/reviews", response_model=ReviewResponseDto)
    def create(book_id: str, review: CreateReviewDto) -> ReviewResponseDto:
        review_data = review.model_dump()
        review_data["book_id"] = book_id
        return ReviewService.create(review_data)
    
    @staticmethod
    @review_router.get("/{book_id}/reviews", response_model=List[ReviewResponseDto])
    def get_all_book_reviews(book_id: str) -> List[ReviewResponseDto]:      
        return ReviewService.get_all_book_reviews(book_id)
