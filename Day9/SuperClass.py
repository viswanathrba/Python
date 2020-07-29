class Microland:
    def Bangalore(self, Number, Location):
        return (Number, Location)
    def Pune(self, Number, Location):
        return (Number, Location)
# print(Microland().Bangalore(3000,'Ecospace'))

class Cognizant(Microland):
    def Bangalore(self, Number, Location, Dept):
        return (Number, Location, Dept)
    def Pune(self, Number, Location, Dept):
        return (Number, Location, Dept)
    def loc_1(self):
        return super(Cognizant, self).Bangalore(200,"Micropolis")
    def loc_2(self):
        return Microland().Pune(3434,"Hinjewadi")
   

# print(Cognizant().loc_1())    
# print(Cognizant().Bangalore(454,'Micropolis', "Automation"))  
# print(Cognizant().loc_2()) 
# print(Cognizant().Pune(24524,'Hinjewadi', "CIS")) 