from abc import abstractmethod, ABC


class AbstractOperation(ABC):
    weight: int = 0

    @staticmethod
    @abstractmethod
    def __call__(a: float, b: float):
        pass


class Addition(AbstractOperation):
    weight = 1

    @staticmethod
    def __call__(a: float, b: float):
        return a + b


class Subtraction(AbstractOperation):
    weight = 1

    @staticmethod
    def __call__(a: float, b: float):
        return a - b


class Division(AbstractOperation):
    weight = 2

    @staticmethod
    def __call__(a: float, b: float):
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed.")


class Multiplication(AbstractOperation):
    weight = 2

    @staticmethod
    def __call__(a: float, b: float):
        return a * b


OPERATORS_MAPPING = {
    '+': Addition(),
    '-': Subtraction(),
    '*': Multiplication(),
    '/': Division(),
}