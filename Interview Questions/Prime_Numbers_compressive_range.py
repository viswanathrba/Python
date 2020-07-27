#How to get prime numbers in list comprehensive range 300
print [i for i in range(2,300) if all(i%j !=0 for j in range(2,i))]


for i in range(2,300):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            print "{} is a prime number".format(i)
    