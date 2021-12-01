import abc

class Request(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getName(self):
        pass

    @abc.abstractmethod
    def getParam1(self):
        pass

    @abc.abstractmethod
    def getParam2(self):
        pass


