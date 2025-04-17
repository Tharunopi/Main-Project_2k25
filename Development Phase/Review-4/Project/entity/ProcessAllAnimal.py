class ProcessAllAnimal:
    @staticmethod
    def processallAnimal(allAnimal):
        newAllanimals = {"id": [], "primaryName": [], "lastSeen": [], "firstSeen": [], "escaped": [], "escapedTime": []}
        for i, j in allAnimal.items():
            newAllanimals["id"].append(int(j.id))
            newAllanimals["primaryName"].append(j.primaryName)
            newAllanimals["lastSeen"].append(j.lastSeen)
            newAllanimals["firstSeen"].append(j.firstSeen)
            newAllanimals["escaped"].append(j.escaped)
            newAllanimals["escapedTime"].append(j.escapedTime)
            
            if len(newAllanimals["id"]) > 5:
                newAllanimals["id"].pop(0)

            if len(newAllanimals["primaryName"]) > 5:
                newAllanimals["primaryName"].pop(0)

            if len(newAllanimals["lastSeen"]) > 5:
                newAllanimals["lastSeen"].pop(0)

            if len(newAllanimals["firstSeen"]) > 5:
                newAllanimals["firstSeen"].pop(0)

            if len(newAllanimals["escaped"]) > 5:
                newAllanimals["escaped"].pop(0)

            if len(newAllanimals["escapedTime"]) > 5:
                newAllanimals["escapedTime"].pop(0)

        return newAllanimals