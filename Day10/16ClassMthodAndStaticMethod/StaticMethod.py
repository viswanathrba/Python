class employ_details:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @staticmethod
    def employ_one(a, b):
        return (a+b)
    
    @staticmethod
    def employ_two(c, d):
        return (c + d)
    

inst = employ_details(14556, 'Viswa') # For Classs Variables
print(inst.name)

print(inst.employ_one(55, 45))
print(inst.employ_two(155, 145))