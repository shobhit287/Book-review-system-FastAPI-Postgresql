from fastapi import APIRouter
from typing import List

from .books_service import BookService
from .dto.create_book_dto import BookCreateDto
from .dto.response_book_dto import BookResponseDto

book_router = APIRouter(prefix="/books", tags=["Books"])

class BookController():
    @staticmethod
    @book_router.post("/", response_model=BookResponseDto)
    def create(book: BookCreateDto):
       book = BookService.create(book.model_dump())
       return book 
    
    @staticmethod
    @book_router.get("/", response_model=List[BookResponseDto])
    def get_all():
       books = BookService.get_all()
       return books
     
  

