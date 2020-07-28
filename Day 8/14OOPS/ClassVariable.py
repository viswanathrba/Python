class MyFirstClass():
    def __init__(self, name, proper):
        self.name = name
        self.proper = proper
        
    def add(self, a, b):
        return a + b, self.name
    
    def sub(self, c, d):
        return c - d, self.proper


print(MyFirstClass("anjan", "tdp").add(3, 6))
print(MyFirstClass("anjan", "tdp").sub(3, 6))