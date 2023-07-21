from abc import ABC, abstractmethod
from collections import deque
from enum import Enum

from calculator.operations import OPERATORS_MAPPING
from models import OperatorEnum


class AbstractOperationsSorter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def sort_operators(self, *, left, right, operator):
        pass


class DefaultOperationsSorter(AbstractOperationsSorter):
    def sort_operators(self, *, left: float | dict, right: float | dict, operator: OperatorEnum):
        sorted_rpn = self.infix_to_sorted_rpn(left, right, operator)
        return self.rpn_to_infix(sorted_rpn)

    @staticmethod
    def precedence(operator: Enum) -> int:
        weight = OPERATORS_MAPPING.get(operator).weight
        return weight

    # Converting sorted reverse polish notation to infix notation
    @staticmethod
    def rpn_to_infix(rpn_expression: deque) -> dict:
        stack = []

        for token in rpn_expression:
            if isinstance(token, OperatorEnum):
                right = stack.pop()
                left = stack.pop()

                infix_expression = {'left': left, 'operator': token, 'right': right}

                stack.append(infix_expression)
            else:
                stack.append(token)
        return stack[0]

    # Converting infix notation to reverse polish notation sorting operators in a queue
    def infix_to_sorted_rpn(self, left: float | dict, right: float | dict, operator: Enum) -> deque:
        output_queue = deque()
        operator_stack = []

        def flatten_expression(ileft: float | dict, iright: float | dict, ioperator: Enum):
            if isinstance(ileft, float):
                output_queue.append(ileft)
            else:
                flatten_expression(ileft.get('left'), ileft.get('right'), ileft.get('operator'))

            if operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(ioperator):
                output_queue.append(operator_stack.pop())
            operator_stack.append(ioperator)

            if isinstance(iright, float):
                output_queue.append(iright)
            else:
                flatten_expression(iright.get('left'), iright.get('right'), iright.get('operator'))

        flatten_expression(left, right, operator)

        while operator_stack:
            output_queue.append(operator_stack.pop())
        return output_queue
