import pickle
from VoterRegistrationCenter import saveObjects, loadObjects

def BallotCounter():
    objs = loadObjects()
    partyScore = [0, 0, 0, 0]
    for obj in objs:
        if obj.get_isAdmin() == False:
            if int(obj.get_party()) == 1:
                partyScore[0] += 1
            elif int(obj.get_party()) == 2:
                partyScore[1] += 1
            elif int(obj.get_party()) == 3:
                partyScore[2] += 1
            else:
                partyScore[3] += 1
    
    saveObjects(objs)

    return partyScore

def main():
    BallotCounter()
                
    
