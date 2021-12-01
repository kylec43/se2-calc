from controller import Controller
from calculator_handler import CalculatorHandler

class CalculatorController(Controller):

    def processRequest(self, request):
        return self.requestHandler.process(request)

    def addHandler(self, requestHandler):
        self.requestHandler = CalculatorHandler()
