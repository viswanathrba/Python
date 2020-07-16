a = {'name': 'anjan', 'proper': 'ananthapur', 'name': "viswa"}
    # key  :  value,   key     : value

print(type(a))
print(len(a))

print(dir(a))

#How to get all keys form dict varaible
print(a.keys())
print(a.values())

#Styel One
print(type(a.get('name')))

print((a.get('name')).upper())
print(a.get('proper'))

#Styel Two
print(type(a['name']))

print((a['name']).upper())
print(a['proper'])