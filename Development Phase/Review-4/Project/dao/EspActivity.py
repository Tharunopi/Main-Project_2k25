from abc import ABC, abstractmethod

class EspActivity(ABC):
    @abstractmethod
    def espManipulation(self, shortestObjId, closestCoords, lastDetectionTime):
        pass