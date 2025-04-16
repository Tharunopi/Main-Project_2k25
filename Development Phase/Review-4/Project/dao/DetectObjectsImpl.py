import math, time
import numpy as np

from dao.DetectObjects import DetectObjects

from util.ClassName import ClassNames
from util.ConfidenceLevel import ConfidenceLevel

class DetectObjectsImpl(DetectObjects):
    def forLoopResults(self, results, dets, curCls, lastDetectionTime):
        
        availableClassNames = ClassNames.getAvailableClassNames()
        wantedClassNames = ClassNames.getWantedClassNames()
        confLevel = ConfidenceLevel.getConfidenceLevel()

        conf = None
        x1, y1, x2, y2 = None, None, None, None
        w, h = None, None
        cx, cy = None, None

        for i in results:
            boxes = i.boxes
            for j in boxes:
                x1, y1, x2, y2 = j.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                cx, cy = x1 + w // 2, y1 + h // 2

                conf = math.ceil((j.conf[0] * 100)) / 100  #used to convert confidence level in readable format
                cls = availableClassNames[int(j.cls[0])]   #used to get the class name from index value

                if cls in wantedClassNames and conf >= confLevel:
                    cur_arr = np.array([x1, y1, x2, y2, conf])
                    dets = np.vstack((dets, cur_arr))
                    curCls = cls
                    lastDetectionTime = time.time()

        return conf, curCls, x1, y1, x2, y2, w, h, cx, cy, dets, lastDetectionTime


            