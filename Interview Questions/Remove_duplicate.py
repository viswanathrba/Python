#How to remove duplicate delecation from list ?
a = ['ab', 'cd', 'ef', 'gh', 'ab', 'cd', 'ef', 'gh']

list = []
for i in a:
    if not i in list:
        list.append(i)
print list