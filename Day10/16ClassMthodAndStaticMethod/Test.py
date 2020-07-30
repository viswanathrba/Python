class employ_details:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def employ_one(self, id, name):
        return (str(id) + ' ' + name)
    def employ_two(self, id, name):
        return str(id) + ' ' + name
    def manager(self):
        return str(self.id) + ' ' + self.name

inst = employ_details(14556, 'Viswa') # For Classs Variables

print(inst.employ_one(18415, 'anjan'))
print(inst.employ_two(18416, 'kumar'))
print(inst.manager())