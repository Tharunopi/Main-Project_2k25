class Animal:
    def __init__(self, id, primaryName, lastSeen, breed=None):
        self.id = id
        self.primaryName = primaryName
        self.lastSeen = lastSeen
        self.breed = breed

    def getAnimal(self):
        return [self.id, self.primaryName, self.lastSeen, self.breed]