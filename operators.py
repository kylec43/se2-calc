from math_operator import MathOperator
import math

class Add(MathOperator):

    def execute(self, p1, p2):
        return p1 + p2


class Subtract(MathOperator):

    def execute(self, p1, p2):
        return p1 - p2


class Multiply(MathOperator):

    def execute(self, p1, p2):
        return p1 * p2


class Divide(MathOperator):

    def execute(self, p1, p2):
        return p1/p2


