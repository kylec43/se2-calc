from request_handler import RequestHandler
from operators import Add, Subtract, Multiply, Divide
from math_response import MathResponse
from request_handler import RequestHandler

class CalculatorHandler(RequestHandler):
    def __init__(self):
        self.mathOperator = None

    def process(self, request):
        if request.getName() == "+":
            self.mathOperator = Add()
        elif request.getName() == "-":
            self.mathOperator = Subtract()
        elif request.getName() == "*":
            self.mathOperator = Multiply()
        elif request.getName() == "/":
            self.mathOperator = Divide()
        else:
            raise Exception("No such operator is supported")
	
        response = MathResponse(self.mathOperator.execute(request.getParam1(), request.getParam2()))
        return response

