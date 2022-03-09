"""
Author: Ritik Kadyan
Date Created: 3/9/2022
Last Modified: 3/9/2022
Modification History:
3/9/2022: File created and all function completed
"""

import csv

def isRegistered(license):
	userFound = False
	with open('userData.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			if(int(row[2]) == license):
				userFound = True
	if userFound == True:
		return True
	else:
		return False
	

def hasVoted(license):	
	with open('userData.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			if(int(row[2]) == license):
				if(bool(row[4]) == True):
					return True
				else:
					return False

def askParty(license):
	userVote = int(input("Who would you like to vote for?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
	setVote(license, userVote)								

def setVote(license, vote):
	#  got bottom two lines from https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
	r = csv.reader(open('userData.csv')) 
	lines = list(r)
	print(lines)
	counter = -1
	rowToSet = 0
	with open('userData.csv') as csv_file:
		counter += 1
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			rowToSet = counter
			if(int(row[2]) == license):
				print("Setting Vote")
				lines[rowToSet][3] = vote

	writer = csv.writer(open('userData.csv', 'w'))
	writer.writerows(lines)

def main():
	askParty(123456789)

if( __name__ == "__main__"):
	main()
