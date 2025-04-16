from abc import ABC, abstractmethod

class SendViaMQTT(ABC):
    @abstractmethod
    def sendForLineChart(self):
        pass

    @abstractmethod
    def sendForSubplot(self):
        pass