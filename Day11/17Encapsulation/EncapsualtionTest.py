class employ_details:
    def __init__(self, name):
        self._id = 100
        self.__name = name
    
    def employ_one(self):
        return self._id, self.__name
    
    def __employ_two(self):
        return self._id, self.__name
    

inst = employ_details('Viswa')

print(inst._id)
print(inst._employ_details__name)

#Employ One Call
print(inst.employ_one())

print(inst._employ_details__employ_two())