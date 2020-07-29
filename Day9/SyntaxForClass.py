'''    Without Class Variables    '''
class class_name:
    def function1_name(self, arg1, arg2):
        return arg1 + arg2
    def function2_name(self, arg1, arg2):
        return arg1 + arg2

inst = class_name()
print(inst.function1_name(val1, val2))
print(inst.function2_name(val1, val2))

print(class_name().function1_name(val1, val2))
print(class_name().function2_name(val1, val2))

'''    With Class Variables    '''

class class_name:
    def __init__(self, name, proper):
        self.name = name
        self.proper = proper
    def function1_name(self, arg1, arg2):
        return arg1 + arg2, self.name
    def function2_name(self, arg1, arg2):
        return arg1 + arg2, self.proper

inst = class_name('xyz', 'abc')
print(inst.function1_name(val1, val2))
print(inst.function2_name(val1, val2))

print(class_name('xyz', 'abc').function1_name(val1, val2))
print(class_name('xyz', 'abc').function2_name(val1, val2))