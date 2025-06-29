from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

def bad_request_handler(exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Bad Request",
            "errors": exc.errors(),
        },
    )

def not_found_handler(exc: Exception):
    return JSONResponse(
        status_code=404,
        content={
            "message": "Not found",
            "errors": exc,
        },
    )

# Handles Pydantic validation errors
async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Validation Error",
            "errors": exc.errors(),
        },
    )

# Handles all other unhandled exceptions
async def server_error_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal Server Error",
            "details": str(exc),
        },
    )