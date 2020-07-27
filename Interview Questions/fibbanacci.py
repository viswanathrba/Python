number = input("enter your number : ")

first = 0
second = 1

for i in range(0,number):
    if (i <= 1):
        next = i
    else:
        next = first + second
        first = second
        second = next
    print next
    
a = 0
b = 1
for i in range(0,10):
    c = a + b
    a = b
    b = c
    print c
    
#using function
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print fib(10)