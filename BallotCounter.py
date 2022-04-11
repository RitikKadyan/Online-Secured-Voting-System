import csv, pickle

def BallotCounter(license):
    with open('registeredVoters.obj', 'rb') as out:
            currVoter = pickle.load(out)  #Loops through voter objects from the file
            if int(currVoter.get_party()) == 1:
                party1 += 1
            elif int(currVoter.get_party()) == 2:
                party2 += 1
            else:
                party3 += 1

def main():
    BallotCounter(license)
                
    
