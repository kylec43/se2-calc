from response import Response

class MathResponse(Response):

    def __init__(self, response):
        self.response = response

    def getResponse(self):
        return self.response

