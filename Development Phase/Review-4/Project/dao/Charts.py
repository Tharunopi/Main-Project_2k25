from abc import ABC, abstractmethod

class Charts(ABC):
    @abstractmethod
    def lineChart(self, pixelDistanceHistory, distanceHistory):
        pass

    @abstractmethod
    def subPlots(self, allXpoints, allYpoints):
        pass