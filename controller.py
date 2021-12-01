import abc

class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def processRequest(self, request):
        pass

    @abc.abstractmethod
    def addHandler(self, requestHandler):
        pass