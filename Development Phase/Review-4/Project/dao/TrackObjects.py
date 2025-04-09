from abc import ABC, abstractmethod

class TrackObjects(ABC):
    @abstractmethod
    def forLoopResults(self, resultTracker):
        pass