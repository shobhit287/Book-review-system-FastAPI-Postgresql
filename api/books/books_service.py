import json

from .dto.response_book_dto import BookResponseDto
from app.redis_cache import redis_client
from .books_model import BooksModel
from app.db import SessionLocal

cache_all_books_key = "books:all"
class BookService:
    @staticmethod
    def create(data: dict):  
        session = SessionLocal()
        try:
            book = BooksModel(**data)
            session.add(book)
            session.commit()
            session.refresh(book)

            #delete cache if new book added
            redis_client.delete(cache_all_books_key)
            return book
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def get_all():
       
        # Try fetching from Redis
        cached_books = redis_client.get(cache_all_books_key)
        if cached_books:
            return json.loads(cached_books)
        
        session = SessionLocal()
        try:
            books = session.query(BooksModel).all()
            result = [
                BookResponseDto.model_validate(book).model_dump(mode="json")
                for book in books
            ]
            redis_client.setex(cache_all_books_key, 600, json.dumps(result))
            return books
        finally:
            session.close()

    

