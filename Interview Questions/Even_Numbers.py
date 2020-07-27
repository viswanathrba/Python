#even numbers

for i in range(0,30):
    if i%2 == 0:
        print i
        
for j in range(0,100):
    if j%2 == 0:
        print j
    
print [k for k in range(0,30) if k%2 == 0]