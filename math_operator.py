import abc

class MathOperator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, p1, p2):
        pass