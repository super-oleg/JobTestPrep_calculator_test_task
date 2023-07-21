from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from models import OperationModel

config = Config(".env")
TEMPLATES_DIR = config('TEMPLATES_DIR', cast=str, default='templates')
templates = Jinja2Templates(directory=TEMPLATES_DIR)


async def index(request):
    template = "index.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)


async def calculate(request):
    calculation_json = OperationModel(**await request.json())
    calculator_instance = request.app.state.calculator_instance

    sort_operations_raw = request.query_params.get('sort_operations', "0")
    sort_operations = sort_operations_raw in ['1', 'true', 'True']

    result = calculator_instance.execute(calculation_json.model_dump(), sort_operations=sort_operations)
    return JSONResponse({'result': result})
