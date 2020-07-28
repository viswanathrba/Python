class parent:
    def __init__(self, acres, division):
        self.acres = acres
        self.division = division
    
    def Acres(self):
        return self.acres
    
    def Division(self):
        return self.division

class child1(parent):    
    def NewAcres(self):
        return self.acres
    
    def NewDivision(self):
        return self.division

class child2(child1):    
    def NewAcres2(self):
        return self.acres
    
    def NewDivision2(self):
        return self.division
        
print(child2(10, "new").NewAcres2())
print(child2(10, "new").NewAcres())