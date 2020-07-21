File = open("Information.txt", "r")

#print(File.read())
#print(File.readline())
data = File.readlines()

for i in data:
    print(i)