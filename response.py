import abc

class Response(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getResponse():
        pass

