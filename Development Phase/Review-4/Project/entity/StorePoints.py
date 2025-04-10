class StorePoints:
    def __init__(self, originalWidth=1280, originalHeight=720, targetWidth=180, targetHeight=180, boundaryLine = [0, 450, 1280, 450], cameraOption=0):
        self.allXpoints = []
        self.allYpoints = []
        self.originalWidth = int(originalWidth)
        self.originalHeight = int(originalHeight)
        self.targetWidth = int(targetWidth)
        self.targetHeight = int(targetHeight)
        self.boundaryLine = boundaryLine
        self.cameraOption = cameraOption

    @property
    def getAllXpoints(self):
        return self.allXpoints
    
    @property
    def getAllYpoints(self):
        return self.allYpoints
    
    @property
    def getoriginalWidth(self):
        return self.originalWidth
    
    @property
    def getoriginalHeight(self):
        return self.originalHeight
    
    @property
    def gettargetWidth(self):
        return self.targetWidth
    
    @property
    def gettargetHeight(self):
        return self.targetHeight
    
    @property
    def getboundaryLine(self):
        return self.boundaryLine
    
    @property
    def getcameraOption(self):
        return self.cameraOption
    
    def updateAllXpoints(self, value):
        self.allXpoints.append(value)

    def updateAllYpoints(self, value):
        self.allYpoints.append(value)