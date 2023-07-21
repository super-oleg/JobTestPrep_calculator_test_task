from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from views import templates


async def value_error_handler(request, exc):
    """
    Handles ValueError exceptions like division by zero.
    """
    if isinstance(exc, ValueError):
        return JSONResponse({"error": str(exc)}, status_code=400)


async def not_found(request: Request, exc: HTTPException):
    """
    Return an HTTP 404 page.
    """
    template = "404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


async def server_error(request: Request, exc: HTTPException):
    """
    Return an HTTP 500 page.
    """
    template = "500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)