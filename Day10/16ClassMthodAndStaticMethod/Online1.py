class Person:
    age = 25
    
    @classmethod
    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = (Person.printAge)

Person.printAge()