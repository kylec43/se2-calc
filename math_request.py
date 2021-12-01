from request import Request

class MathRequest(Request):

    def __init__(self, name, param1, param2):
        self.name = name
        self.param1 = param1
        self.param2 = param2

    def getName(self):
        return self.name

    def getParam1(self):
        return self.param1

    def getParam2(self):
        return self.param2

