
class Voter:
    def __init__(self, firstname = "", lastname = "", licensenum = 0, party = 4, isadmin = False):
        self._firstname = firstname
        self._lastname = lastname
        self._licensenumber = licensenum
        self._party = party   #0 is republican, 1 is democrat, 2 is other
        self._isadmin = isadmin
    
    def get_firstname(self):
        return self._firstname
    
    def set_firstname(self, x):
        self._firstname = x

    def get_lastname(self):
        return self._lastname
    
    def set_lastname(self, x):
        self._lastname = x

    def get_licensenumber(self):
        return self._licensenumber
    
    def set_licencenumber(self, x):
        self._licensenumber = x

    def get_party(self):
        return self._party
    
    def set_party(self, x):
        self._party = x

    def get_isadmin(self):
        return self._firstname
    
    def set_isadmin(self, x):
        self._isadmin = x


john = Voter()

john.set_firstname("John")
john.set_lastname("Doe")
john.set_licencenumber(123456789)
john.set_party(0)
john.set_isadmin(True)

print(john._firstname)
print(john._lastname)
print(john._licensenumber)
print(john._party)
print(john._isadmin)
