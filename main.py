import pickle
from BallotCounter import BallotCounter
from VoterRegistrationCenter import registerVoter, loadObjects, saveObjects

def adminMenu():
    adminInput = int(input("\n1: Ballot Counter\n2: Print all users and info\n3: Exit\nWhat would you like to do: "))
    if adminInput == 1:
        votingScores = BallotCounter()
        print(f"\nScores\nParty 1: {votingScores[0]}\nParty 2: {votingScores[1]}\nParty 3: {votingScores[2]}\nHasn't Voted: {votingScores[3]}")
    elif adminInput == 2:
        printAll()
    elif adminInput == 3:
        print("Exiting...")

def userMenu():
    userInput = int(input("\n1: Voter Registration Center\n2: Polling Center\n3: Exit\nWhat would you like to do: "))
    if userInput == 1:
        userInputForVoterRegistration = int(input("\n1: Register as voter\n2: Exit\nWhat would you like to do: "))
        if userInputForVoterRegistration == 1:
            registerVoter()
        elif userInputForVoterRegistration == 2:
            print("Exiting...")
    elif userInput == 2:
        print("Exiting...")

def authenticateAdmin(license):
    isAdmin = False
    with open('registeredVoters.obj', 'rb') as out:
        currVoter = pickle.load(out)  #Loops through voter objects from the file
        if (int(currVoter.get_licenseNumber()) == int(license)):
            if currVoter.get_isAdmin() == True:
                isAdmin = True

    return isAdmin
    

def main():
    adminOrUser = int(input("1: Admin\n2: Voter\n3: Exit\nWhat would you like to do: "))
    if adminOrUser == 1:
        try:
            adminLicenseToCheck = int(input("Enter you license number: "))
        except ValueError:
            print("Please enter a number.")
        
        #Indiana license numbers are 10 digits long 
        if  len(str(adminLicenseToCheck)) != 10:
            raise Exception("Sorry, license number must only be 10 digits long")

        isAdmin = authenticateAdmin(adminLicenseToCheck)
        if isAdmin:
            adminMenu()
        else:
            print("Not an admin.\n")
    elif adminOrUser == 2:
        userMenu()
    elif adminOrUser == 3:
        print("Exiting...")

#main()

def printAll():
    objects = loadObjects()
    for object in objects:
        print(object.get_firstName())
        print(object.get_lastName())
        print(object.get_licenseNumber())
        print(object.get_isAdmin())
        print("\n")

    saveObjects(objects)
printAll()