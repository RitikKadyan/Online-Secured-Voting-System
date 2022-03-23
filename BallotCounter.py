import csv

def BallotCounter(license):
    party1 = 0
    party2 = 0
    party3 = 0
    licenseNum = int(input("What is your license number?"))
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
            if(int(row[2]) == licenseNum):
                if(askParty(licenseNum) == 1):
                    party1 += 1
                elif(askParty(licenseNum) == 2):
                    party2 += 1
                elif(askParty(licenseNum) == 3):
                    party3 += 1
                else:
                    print("Please enter right value for party chosen.")

int main():
    BallotCounter(license)
                
    
