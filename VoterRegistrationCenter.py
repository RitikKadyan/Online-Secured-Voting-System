#3 methods
#voterSerialize -> serializes voter object to external file
#registerVoter -> retrieve information from person, create new Voter
#authenticateVoter -> compare license number entered to saved license number to see if previously registered

#imports
from logging import FileHandler
import pickle
import voter.py
import csv

#define class
class VoterRegistrationCenter:
   #voterSerialize method - save voter object to external file
   def voterSerialize(registeredVoter):
     registeredVoter = voter()
     filehandler = open('registeredVoters.obj', 'w')
     pickle.dump(registeredVoter, filehandler)
       
   #registerVoter method - get first and last name, license, party and create new registered voter
   def registerVoter(self):
        userFirstName = (input("What is your first name?"))
        userLastName = (input("What is your last name?"))
        userLicense = int(input("What is your license number?"))
        userParty = int(input("Which party do you support?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
        userIsAdmin = False
        newVoter = voter(userFirstName, userLastName, userLicense, userParty, userIsAdmin)
        self.voterSerialize(newVoter)

   #authenticateVoter method - check if license number in csv file
   def authenticateVoter(license):
      registeredUser = False
      with open('userData.csv') as userDataFile:
        csv_reader = csv.reader(userDataFile, delimiter=',')
        for row in csv_reader:
          if(int(row[2]) == license):
            registeredUser = True
      if(registeredUser == True):
        return True
      else:
        return False