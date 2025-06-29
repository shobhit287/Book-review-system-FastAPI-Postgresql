import json

from app.db import SessionLocal
from app.redis_cache import redis_client
from .reviews_model import ReviewModel
from .dto.response_review_dto import ReviewResponseDto

class ReviewService:
    @staticmethod
    def create(data: dict):  
        session = SessionLocal()
        try:
            review = ReviewModel(**data)
            session.add(review)
            session.commit()
            session.refresh(review)

            # delete cache for the book
            book_id = str(review.book_id)
            cache_key = f"book_reviews_{book_id}"
            redis_client.delete(cache_key)

            return review
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

   
    @staticmethod
    def get_all_book_reviews(book_id):
        cache_key = f"book_reviews_{book_id}"
        cached_data = redis_client.get(cache_key)
        if cached_data:
            return json.loads(cached_data)
        
        session = SessionLocal()        
        try:
            reviews = session.query(ReviewModel).filter(ReviewModel.book_id == book_id).all()
            result = [
                       ReviewResponseDto.model_validate(review).model_dump(mode="json")
                       for review in reviews
                    ]
            redis_client.setex(cache_key, 600, json.dumps(result))
            return reviews
        finally:
            session.close()

