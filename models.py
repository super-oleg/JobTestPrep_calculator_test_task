from enum import Enum
from typing import Union

from pydantic import BaseModel


class OperatorEnum(str, Enum):
    addition = '+'
    substraction = '-'
    multiplication = '*'
    division = '/'


class OperationModel(BaseModel):
    left: Union[float, 'OperationModel']
    right: Union[float, 'OperationModel']
    operator: OperatorEnum
