import sys
sys.path.append(r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4\Project")

from util.sort import *

class TrackerLoading:
    @staticmethod 
    def loadTracker(max_age=40, min_hits=3, iou_threshold=0.3):
        tracker = Sort(max_age=40, min_hits=3, iou_threshold=0.3)
        return tracker