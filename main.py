from calculator_controller import CalculatorController
from calculator_handler import CalculatorHandler
from math_request import MathRequest

#Create Calculator Controller
calculatorController = CalculatorController()

#Create and Add calculator handler to calculator controller
calculatorHandler = CalculatorHandler()
calculatorController.addHandler(calculatorHandler)

#Create requests for add, subtract, multiply, divide
addRequest = MathRequest("+", 10, 2)
subtRequest = MathRequest("-", 10, 2)
multRequest = MathRequest("*", 10, 2)
divRequest = MathRequest("/", 10, 2)

try:
    #Process all math requests
    addResponse = calculatorController.processRequest(addRequest)
    subtResponse = calculatorController.processRequest(subtRequest)
    multResponse = calculatorController.processRequest(multRequest)
    divResponse = calculatorController.processRequest(divRequest)

    #Print all of the math responses
    print("Add response is: " + str(addResponse.getResponse()))
    print("Subtract response is: " + str(subtResponse.getResponse()))
    print("Multiply response is: " + str(multResponse.getResponse()))
    print("Divide response is: " + str(divResponse.getResponse()))


except Exception as e:
    print(e)


