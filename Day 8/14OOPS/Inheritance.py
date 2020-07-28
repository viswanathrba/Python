class parent:
    def __init__(self, acres, division):
        self.acres = acres
        self.division = division
    
    def Acres(self):
        return self.acres
    
    def Division(self):
        return self.division

class child(parent):    
    def NewAcres(self):
        return self.acres
    
    def NewDivision(self):
        return self.division

print(child(2, "jmd").NewAcres())
print(child(2, "jmd").NewDivision())
print(child(2, "jmd").Acres())
print(child(2, "jmd").Division())