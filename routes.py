from starlette.config import Config
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

import handlers
import views

config = Config(".env")
STATIC_DIR = config('STATIC_DIR', cast=str, default='templates')

routes = [
    Route('/', views.index),
    Route('/calculate', views.calculate, methods=['POST']),
    Mount('/static', app=StaticFiles(directory=STATIC_DIR), name="static")
]

exception_handlers = {
    404: handlers.not_found,
    500: handlers.server_error,
    Exception: handlers.value_error_handler
}