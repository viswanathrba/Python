class employ_details:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @classmethod
    def employ_one(cls, a, b):
        return cls(str(a), b)
    

inst = employ_details(14556, 'Viswa') # For Classs Variables
print(inst.name)

print(inst.employ_one('abc', 'def').id)
print(inst.employ_one('abc', 'def').name)