class StorePoints:
    def __init__(self, originalWidth=1280, originalHeight=720, targetWidth=180, targetHeight=180):
        self.allXpoints = []
        self.allYpoints = []
        self.originalWidth = int(originalWidth)
        self.originalHeight = int(originalHeight)
        self.targetWidth = int(targetWidth)
        self.targetHeight = int(targetHeight)

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