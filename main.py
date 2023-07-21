import uvicorn as uvicorn
from starlette.applications import Starlette
from routes import routes, exception_handlers
from starlette.config import Config
from utils import lifespan

config = Config(".env")

DEBUG = config('DEBUG', cast=bool, default=False)
HOST = config('ALLOWED_HOSTS', cast=str, default='0.0.0.0')
PORT = config('PORT', cast=int, default=8000)


app = Starlette(debug=DEBUG, routes=routes, exception_handlers=exception_handlers, lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
