import pickle

def BallotCounter():
    partyScore = [0, 0, 0, 0]
    with open('registeredVoters.obj', 'rb') as out:
            currVoter = pickle.load(out)  #Loops through voter objects from the file
            if int(currVoter.get_party()) == 1:
                partyScore[0] += 1
            elif int(currVoter.get_party()) == 2:
                partyScore[1] += 1
            elif int(currVoter.get_party()) == 3:
                partyScore[2] += 1
            else:
                partyScore[3] += 1

    return partyScore

def main():
    BallotCounter()
                
    
