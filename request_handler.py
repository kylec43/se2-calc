import abc

class RequestHandler(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def process(self, request):
        pass