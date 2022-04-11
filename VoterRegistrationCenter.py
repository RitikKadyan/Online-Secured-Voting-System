#3 methods
#voterSerialize -> serializes voter object to external file
#registerVoter -> retrieve information from person, create new Voter
#authenticateVoter -> compare license number entered to saved license number to see if previously registered
#Tutorials Used: https://towardsdatascience.com/what-why-and-how-of-de-serialization-in-python-2d4c3b622f6b


#imports
import pickle
from Voter import Voter
import csv

#voterSerialize method - save voter object to external file
def voterSerialize(registeredVoter):
    filehandler = open('registeredVoters.obj', 'wb')
    pickle.dump(registeredVoter, filehandler)
    
#registerVoter method - get first and last name, license, party and create new registered voter
def registerVoter():
    userFirstName = (input("What is your first name?"))
    userLastName = (input("What is your last name?"))
    userLicense = int(input("What is your license number?"))
    userParty = int(input("Which party do you support?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
    userIsAdmin = False
    newVoter = Voter()
    newVoter.set_firstName(userFirstName)
    newVoter.set_lastName(userLastName)
    newVoter.set_licenseNumber(userLicense)
    newVoter.set_party(userParty)
    newVoter.set_isAdmin(userIsAdmin)
    print(newVoter._firstName)
    print(newVoter._lastName)
    print(newVoter._licenseNumber)
    print(newVoter._party)
    voterSerialize(newVoter)

#authenticateVoter method - check if license number in obj file
def authenticateVoter(license):
    with open('registeredVoters.obj', 'rb') as out:
        currVoter = pickle.load(out)  #Loops through voter objects from the file
        if (int(currVoter.get_licenseNumber()) == int(license)):
            print("Registered")
            registeredUser = True
            return registeredUser
        else:
            registeredUser = False
            
    if(registeredUser == False):
        print("Not registered")
        

#test VoterRegistrationCenter methods
       
def unitTest():
    registerVoter()
    authenticateVoter(123456)
