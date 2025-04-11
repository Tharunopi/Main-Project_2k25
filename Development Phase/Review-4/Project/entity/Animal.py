from datetime import datetime

class Animal:
    def __init__(self, id, primaryName):
        self.id = id
        self.primaryName = primaryName
        self.lastSeen = None
        self.firstSeen = datetime.now()
        self.escaped = False
        self.escapedTime = None
        self.path = []

    def getAnimal(self):
        return [self.id, self.primaryName, self.lastSeen, self.breed]
    
    def updatelastSeen(self, value):
        self.lastSeen = value
        self.path.append(value)

    def markAsEscaped(self):
        if not self.escaped:
            self.escaped = True
            self.escapedTime = datetime.now()