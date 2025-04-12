from abc import ABC, abstractmethod

class Charts(ABC):
    @abstractmethod
    def lineChart(self):
        pass

    @abstractmethod
    def subPlots(self):
        pass