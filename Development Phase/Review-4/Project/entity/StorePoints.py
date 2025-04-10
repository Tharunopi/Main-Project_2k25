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