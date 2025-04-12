class ProcessAllAnimal:
    @staticmethod
    def processallAnimal(allAnimal):
        newAllanimals = {"id": [], "primaryName": [], "lastSeen": [], "firstSeen": [], "escaped": [], "escapedTime": []}
        for i, j in allAnimal.items():
            newAllanimals["id"].append(int(j.id))
            if len(newAllanimals["id"]) > 5:
                newAllanimals["id"].pop(0)

            newAllanimals["primaryName"].append(j.primaryName)
            if len(newAllanimals["id"]) > 5:
                newAllanimals["primaryName"].pop(0)

            newAllanimals["lastSeen"].append(j.lastSeen)
            if len(newAllanimals["id"]) > 5:
                newAllanimals["lastSeen"].pop(0)

            newAllanimals["firstSeen"].append(j.firstSeen)
            if len(newAllanimals["id"]) > 5:
                newAllanimals["firstSeen"].pop(0)

            newAllanimals["escaped"].append(j.escaped)
            if len(newAllanimals["id"]) > 5:
                newAllanimals["escaped"].pop(0)

            newAllanimals["escapedTime"].append(j.escapedTime)
            if len(newAllanimals["id"]) > 5:
                newAllanimals["escapedTime"].pop(0)

        return newAllanimals