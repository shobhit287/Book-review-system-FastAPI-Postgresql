from fastapi import FastAPI
from pydantic import ValidationError

import app.redis_cache
from .map_modules import load_modules
from .exceptions import validation_error_handler, server_error_handler
from .db import connect_db

def initialize_app() -> FastAPI:
    app = FastAPI()
    connect_db() 

    app.add_exception_handler(ValidationError, validation_error_handler)
    app.add_exception_handler(Exception, server_error_handler)
    
    load_modules(app)
    @app.get("/")
    def server_status():
        return {"message": "Server is running"}

    return app
