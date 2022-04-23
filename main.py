import pickle
from BallotCounter import BallotCounter
from VoterRegistrationCenter import authenticateVoter, registerVoter, loadObjects, saveObjects
from PollingSystem import askParty, hasVoted

def printAll():
    objects = loadObjects()
    for obj in objects:
        print(obj.get_firstName())
        print(obj.get_lastName())
        print(obj.get_licenseNumber())
        print(obj.get_party())
        print(obj.get_isAdmin())
        print("\n")

    saveObjects(objects)

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
        userInputForPollingCenter =  int(input("\n1: Vote\n2: Exit\nWhat would you like to do: "))
        if userInputForPollingCenter == 1:
            try:
                userLicense = int(input("\nEnter license: "))
            except ValueError:
                print("Please enter a number.")
        
        #Indiana license numbers are 10 digits long 
            if  len(str(userLicense)) != 10:
                raise Exception("Sorry, license number must only be 10 digits long")
            
            try:
                social = int(input("\nEnter last four digits of your social: "))
            except ValueError:
                print("Please enter a number.")

            if  len(str(social)) != 4:
                raise Exception("Sorry, social must only be 4 digits long")


            userExists = authenticateVoter(userLicense, social)
            if userExists == True:
                voted = hasVoted(userLicense)
                if voted == True:
                    print("You have already voted.")
                else:
                    askParty(userLicense)
            else:
                print("Information is wrong! You must register as a voter first.")

            
        elif userInputForPollingCenter == 2:
            print("Exiting...")
    elif userInput == 3:
        print("Exiting...")


def authenticateAdmin(license):
    isAdmin = False
    objs = loadObjects()
    for obj in objs:
        if (int(obj.get_licenseNumber()) == int(license)):
            if obj.get_isAdmin() == True:
                isAdmin = True

    saveObjects(objs)
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

main()


#printAll()

