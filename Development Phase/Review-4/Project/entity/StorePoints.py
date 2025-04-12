import sys
sys.path.append(r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4\Project")

from entity.Animal import Animal

class StorePoints:
    def __init__(self, originalWidth=1280, originalHeight=720, targetWidth=180, targetHeight=180, boundaryLine = [0, 450, 1280, 450], cameraOption=0):
        self.allXpoints = []
        self.allYpoints = []
        self.distanceHisory = []
        self.pixelDistanceHistory = []
        self.originalWidth = int(originalWidth)
        self.originalHeight = int(originalHeight)
        self.targetWidth = int(targetWidth)
        self.targetHeight = int(targetHeight)
        self.boundaryLine = boundaryLine
        self.cameraOption = cameraOption
        self.animals = {}

    def getAllXpoints(self):
        return self.allXpoints
    
    def getAllYpoints(self):
        return self.allYpoints
    
    def getoriginalWidth(self):
        return self.originalWidth
    
    def getoriginalHeight(self):
        return self.originalHeight
    
    def gettargetWidth(self):
        return self.targetWidth
    
    def gettargetHeight(self):
        return self.targetHeight
    
    def getboundaryLine(self):
        return self.boundaryLine
    
    def getcameraOption(self):
        return self.cameraOption
    
    def getpixelDistanceHistory(self):
        return self.pixelDistanceHistory
    
    def getdistanceHisory(self):
        return self.distanceHisory
    
    def updateAllXpoints(self, value):
        self.allXpoints.append(value)

    def updateAllYpoints(self, value):
        self.allYpoints.append(value)

    def updatedistanceHisory(self, value):
        self.distanceHisory.append(value)

    def updatepixelDistanceHistory(self, value):
        self.pixelDistanceHistory.append(value)

    def processAnimal(self, id, className, cx, cy):
        if id not in self.animals:
            self.animals[id] = Animal(id=id, primaryName=className)

        self.animals[id].updatelastSeen((cx, cy))

        if (self.boundaryLine[1] - 20 < cy < self.boundaryLine[1] + 20) and not self.animals[id].escaped:
            self.animals[id].markAsEscaped()
            return True
        return False

    def getEscapeCount(self):
        count = sum([1 for i in self.animals.values() if i.escaped])
        return count
    
    def getEscapedAnimals(self):
        escaped = [i for i in self.animals.values() if i.escaped]
        return escaped
    
    def allAnimals(self):
        return self.animals