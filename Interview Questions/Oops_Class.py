#How to get oops instent class static
class peddanna:
    def __init__(self, name, age, proper):
        self.name = name
        self.age = age
        self.proper = proper
    @classmethod
    def anjan(cls,name, age, proper):
        return cls(name, age, proper)
    @staticmethod
    def peddu(p):
        return p < 30
inst = peddanna("darling", 23, "anantapur")
inst1 = inst.anjan("nari", 20, "anantapur")

print (inst.name)
print (inst.age)
print (inst.proper)
print (inst1.name)
print (inst1.age)
print (inst1.proper)        

print (peddanna.peddu(20))