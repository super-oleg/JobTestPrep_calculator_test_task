from starlette.applications import Starlette
from calculator import Calculator


async def lifespan(app: Starlette) -> None:
    calculator_instance = Calculator()
    app.state.calculator_instance = calculator_instance
    yield
