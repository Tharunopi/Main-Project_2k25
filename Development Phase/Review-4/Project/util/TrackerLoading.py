from sort import *

class TrackerLoading:
    @staticmethod 
    def loadTracker(max_age=40, min_hits=3, iou_threshold=0.3):
        tracker = Sort(max_age=40, min_hits=3, iou_threshold=0.3)
        return tracker