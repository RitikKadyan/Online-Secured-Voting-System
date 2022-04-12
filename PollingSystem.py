"""
Author: Ritik Kadyan
Date Created: 3/9/2022
Last Modified: 3/9/2022
Modification History:
3/9/2022: File created and all function completed
"""

import csv, pickle
from VoterRegistrationCenter import voterSerialize

def isRegistered(license):
	userFound = False
	with open('registeredVoters.obj', 'rb') as out:
		currVoter = pickle.load(out)  #Loops through voter objects from the file
		if (int(currVoter.get_licensenumber()) == int(license)):
			userFound = True

	return userFound

def hasVoted(license):	
	hasVoted = False
	with open('registeredVoters.obj', 'rb') as out:
		currVoter = pickle.load(out)  #Loops through voter objects from the file
		if (int(currVoter.get_licenseNumber()) == int(license)):
			if currVoter.get_party() != 4:
				hasVoted = True

	return hasVoted

def askParty(license):
	userVote = int(input("Who would you like to vote for?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
	setVote(license, userVote)								

def setVote(license, vote):
	with open('registeredVoters.obj', 'rb') as out:
		currVoter = pickle.load(out)  #Loops through voter objects from the file
		if (int(currVoter.get_licenseNumber()) == int(license)):
			currVoter.set_party(vote)
			voterSerialize(currVoter)
			file = open('registeredVoters.obj', 'wb')
			pickle.dump(currVoter, file)
			file.close()

def main():
	askParty(123456789)

if( __name__ == "__main__"):
	main()
