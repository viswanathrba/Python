import sys

try:
    a = open("anjan.txt", "r")
except ZeroDivisionError:
    print("Unable to Devide 3 with zero")
except FileNotFoundError:
    print("File Not Found Error, Please check...!")
    sys.exit()
except:
    print("Different Error")
    



print("test")