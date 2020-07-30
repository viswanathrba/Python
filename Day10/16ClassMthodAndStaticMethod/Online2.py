from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
      
    # a class method to create a  
    # Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name2, year): 
        return cls(name2, date.today().year - year) 
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('anjan', 21) 
person2 = Person.fromBirthYear('kumar', 1996) 
  
print (person1.age) 
print (person1.name) 

print (person2.age) 
print (person2.name) 