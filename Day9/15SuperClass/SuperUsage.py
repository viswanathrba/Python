class person:
    def details(self, name, age):
        return 'person one details : ' + name + ' ' + str(age)
    
    def education(self, course, duration):
        return 'person one education details : ' + course + ' ' + str(duration) + ' days'

class person2(person):
    def details(self, name, age):
        return 'person2 one details : ' + name + ' ' + str(age)
    
    def education(self, course, duration):
        return 'person2 one education details : ' + course + ' ' + str(duration) + ' days'
    
    def p1_d(self):
        #return super(person2, self).details('kumar', 25)
        return person().details('new', 40)
    def p1_e(self):
        return super(person2, self).education('Ansible', 45)

print(person2().details('akr', 30))
print(person2().education('python', 40))

print(person2().p1_d())
print(person2().p1_e())

