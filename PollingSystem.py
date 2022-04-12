"""
Author: Ritik Kadyan
Date Created: 3/9/2022
Last Modified: 3/9/2022
Modification History:
3/9/2022: File created and all function completed
"""

import pickle
from VoterRegistrationCenter import voterSerialize, saveObjects, loadObjects

def isRegistered(license):
	objs = loadObjects()	
	userFound = False
	for obj in objs:
		if (int(obj.get_licensenumber()) == int(license)):
			userFound = True

	saveObjects(objs)
	return userFound

def hasVoted(license):
	objs = loadObjects()	
	hasVoted = False
	for obj in objs:
		if (int(obj.get_licenseNumber()) == int(license)):
			if int(obj.get_party()) != 4:
				hasVoted = True

	saveObjects(objs)
	return hasVoted

def askParty(license):
	userVote = int(input("\n1. Democratic Party\n2. Republican Party\n3. Other\nWho would you like to vote for: "))
	setVote(license, userVote)								

def setVote(license, vote):
	objs = loadObjects()
	for obj in objs:
		if (int(obj.get_licenseNumber()) == int(license)):
			obj.set_party(vote)
	saveObjects(objs)

def main():
	askParty(123456789)

if( __name__ == "__main__"):
	main()
