
class Voter:
    def __init__(self, firstName = "", lastName = "", licenseNum = 0, party = 4, isAdmin = False):
        self._firstName = firstName
        self._lastName = lastName
        self._licenseNumber = licenseNum
        self._party = party   #0 is democrat , 1 is republican, 2 is other
        self._isAdmin = isAdmin
    
    def get_firstName(self):
        return self._firstName
    
    def set_firstName(self, x):
        self._firstName = x

    def get_lastName(self):
        return self._lastName
    
    def set_lastName(self, x):
        self._lastName = x

    def get_licenseNumber(self):
        return self._licenseNumber
    
    def set_licenseNumber(self, x):
        self._licenseNumber = x

    def get_party(self):
        return self._party
    
    def set_party(self, x):
        self._party = x

    def get_isAdmin(self):
        return self._isAdmin
    
    def set_isAdmin(self, x):
        self._isAdmin = x

    def set_social(self, x):
        self.__social = x

    def get_social(self):
        return self.__social



def unitTest():
    john = Voter()

    john.set_firstName("John")
    john.set_lastName("Doe")
    john.set_licenseNumber(123456789)
    john.set_party(0)
    john.set_isAdmin(True)

    print(john._firstName)
    print(john._lastName)
    print(john._licenseNumber)
    print(john._party)
    print(john._isAdmin)

#unitTest()