from typing import Union, Type

from .operations import OPERATORS_MAPPING, AbstractOperation
from .sorters import AbstractOperationsSorter, DefaultOperationsSorter


class Calculator:
    __slots__ = ['_sorter']

    def __init__(self, sorter: Type[AbstractOperationsSorter] = DefaultOperationsSorter):
        self._sorter = sorter()

    def _sort_operations(self, expression: dict) -> dict:
        return self._sorter.sort_operators(**expression)

    def _make_expression(self, *,
                        left: Union[float, dict],
                        right: Union[float, dict],
                        operator: str) -> 'Expression':

        if isinstance(left, dict):
            left = self._make_expression(**left)
        if isinstance(right, dict):
            right = self._make_expression(**right)
        operation = OPERATORS_MAPPING.get(operator)
        return Expression(left=left, right=right, operation=operation)

    def execute(self, raw_expression: dict, sort_operations: bool = False) -> float:
        if sort_operations:
            raw_expression = self._sort_operations(raw_expression)
        expression = self._make_expression(**raw_expression)
        return expression.calculate()


class Expression:
    __slots__ = ['left', 'right', 'operation']

    def __init__(self, left: Union[float, 'Expression'], right: Union[float, 'Expression'], operation: AbstractOperation):
        self.left = left
        self.right = right
        self.operation = operation

    def calculate(self) -> float:
        if isinstance(self.left, Expression):
            self.left = self.left.calculate()
        if isinstance(self.right, Expression):
            self.right = self.right.calculate()
        return self.operation(self.left, self.right)
