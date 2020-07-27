#How to find numbers and strings
# import pdb

a = ['akr', 1, 2, 'anjan', 'kumar']

for i in a:
    if type(i) == int:
        print "integer:", i
    else:
        print "string:", i
        
print [j for j in a if type(j) == int]
print [j for j in a if type(j) == str]