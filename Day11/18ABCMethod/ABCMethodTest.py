#from abc import ABC, abstractmethod

class Animal():
    def move(self):
        return "any...."

class Human(Animal):
    def move(self):
        return "i can walk & run"

class Lion(Animal):
    def move(self):
        return "i can roar"


inst1 = Human()
inst2 = Lion()

print(inst1.move())
print(inst2.move())
