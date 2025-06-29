from api.books.books_controller import book_router
from api.reviews.reviews_controller import review_router
URL_PREFIX = "/api"

def load_modules(app):
    app.include_router(book_router, prefix=URL_PREFIX)
    app.include_router(review_router, prefix=URL_PREFIX)
