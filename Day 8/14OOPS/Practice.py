class mySecondClass:
    def __init__(self, PhoneNumber, Address):
        self.PhoneNumber = PhoneNumber
        self.Address = Address
    
    def number(self):
        return self.PhoneNumber
    
    def address(self):
        return self.Address

class myThirdClass:
    def __init__(self, native, district):
        self.native = native
        self.district = district
    
    def Native(self):
        return self.native
    
    def District(self):
        return self.district

print(mySecondClass(9848456585, "bangalore").address())
print(myThirdClass('jmd', "kadapa").Native())
print(myThirdClass('jmd', "kadapa").District())