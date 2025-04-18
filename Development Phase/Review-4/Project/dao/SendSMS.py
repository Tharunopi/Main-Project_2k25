from abc import ABC, abstractmethod

class SendSMS(ABC):
    @abstractmethod
    def sendMsg(self):
        pass

    @abstractmethod
    def addNumber(self, number):
        pass

    @abstractmethod
    def deleteNumber(self, number):
        pass