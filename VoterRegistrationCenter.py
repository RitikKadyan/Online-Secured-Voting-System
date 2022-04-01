#3 methods
#voterSerialize -> serializes voter object to external file
#registerVoter -> retrieve information from person, create new Voter
#authenticateVoter -> compare license number entered to saved license number to see if previously registered
#Tutorials Used: https://towardsdatascience.com/what-why-and-how-of-de-serialization-in-python-2d4c3b622f6b


#imports
import pickle
from Voter import Voter
import csv

#define class
class VoterRegistrationCenter:
   #voterSerialize method - save voter object to external file
   def voterSerialize(self, registeredVoter):
     filehandler = open('registeredVoters.obj', 'wb')
     pickle.dump(registeredVoter, filehandler)
       
   #registerVoter method - get first and last name, license, party and create new registered voter
   def registerVoter(self):
        userFirstName = (input("What is your first name?"))
        userLastName = (input("What is your last name?"))
        userLicense = int(input("What is your license number?"))
        userParty = int(input("Which party do you support?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
        userIsAdmin = False
        newVoter = Voter()
        newVoter.set_firstname(userFirstName)
        newVoter.set_lastname(userLastName)
        newVoter.set_licensenumber(userLicense)
        newVoter.set_party(userParty)
        newVoter.set_isadmin(userIsAdmin)
        print(newVoter._firstname)
        print(newVoter._lastname)
        print(newVoter._licensenumber)
        print(newVoter._party)
        self.voterSerialize(newVoter)

   #authenticateVoter method - check if license number in obj file
   def authenticateVoter(self, license):
      with open('registeredVoters.obj', 'rb') as out:
        assert type(pickle.load(out)) == Voter
        if (Voter.get_licensenumber == license):
          print("True")
          registeredUser = True
        else:
          print("False")
          registeredUser = False
        return registeredUser

#test VoterRegistrationCenter methods
vrc = VoterRegistrationCenter()        
vrc.registerVoter()
vrc.authenticateVoter(123456)
