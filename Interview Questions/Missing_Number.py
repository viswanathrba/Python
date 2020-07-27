#Which number are missing in the list?
missing_number = [1,2,3,4,5,6,7,8]
n = len(missing_number) + 1
print (n*(n+1))/2 - sum(missing_number)