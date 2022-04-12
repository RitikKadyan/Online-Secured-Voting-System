#3 methods
#voterSerialize -> serializes voter object to external file
#registerVoter -> retrieve information from person, create new Voter
#authenticateVoter -> compare license number entered to saved license number to see if previously registered
#Tutorials Used: https://towardsdatascience.com/what-why-and-how-of-de-serialization-in-python-2d4c3b622f6b


#imports
import pickle
from Voter import Voter

#voterSerialize method - save voter object to external file
def voterSerialize(registeredVoter):
    filehandler = open('registeredVoters.obj', 'wb')
    pickle.dump(registeredVoter, filehandler)

#registerVoter method - get first and last name, license, party and create new registered voter
def registerVoter():
    objs = loadObjects()
    userLicense = int(input("What is your license number: "))
    if(authenticateVoter(userLicense, objs)):
        print("Already registered as voter!")
    else:
        userFirstName = (input("What is your first name: "))
        userLastName = (input("What is your last name: "))
        userParty = int(input("Which party do you support?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
        userIsAdmin = False
        newVoter = Voter(userFirstName, userLastName, userLicense, userParty, userIsAdmin)
        objs.append(newVoter)
        saveObjects(objs)
        #newVoter.set_firstName(userFirstName)
        #newVoter.set_lastName(userLastName)
        #newVoter.set_licenseNumber(userLicense)
        #newVoter.set_party(userParty)
        #newVoter.set_isAdmin(userIsAdmin)
        #print(newVoter._firstName)
        #print(newVoter._lastName)
        #print(newVoter._licenseNumber)
        #print(newVoter._party)
        #voterSerialize(newVoter)

#authenticateVoter method - check if license number in obj file
def authenticateVoter(license, objs):
    registeredUser = False
    for obj in objs:
        if (int(obj.get_licenseNumber()) == int(license)) and (obj.get_isAdmin() == False):
            registeredUser = True

    return registeredUser 

def loadObjects():
    with open('registeredVoters.obj', 'rb') as out:
        objs = pickle.load(out) 
    return objs
        
def saveObjects(objs):
    filehandler = open('registeredVoters.obj', 'wb')
    pickle.dump(objs, filehandler)

#test VoterRegistrationCenter methods
       
def unitTest():
    registerVoter()
    authenticateVoter(123456)


#unitTest()

def createDummyUser():
    userLicense = int(input("What is your license number: "))
    userFirstName = (input("What is your first name: "))
    userLastName = (input("What is your last name: "))
    userParty = int(input("Which party do you support?\n1. Democratic Party\n2. Republican Party\n3. Other\n\nEnter 1, 2, or 3: "))
    userIsAdmin = False
    newVoter = Voter(userFirstName, userLastName, userLicense, userParty, userIsAdmin)
    voterSerialize(newVoter)

#createDummyUser()