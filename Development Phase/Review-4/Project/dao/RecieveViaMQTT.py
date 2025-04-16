from abc import ABC, abstractmethod

class RecieveViaMQTT(ABC):
    @abstractmethod
    def recieveForLineChart(self):
        pass

    @abstractmethod
    def recieveForSubPlot(self):
        pass