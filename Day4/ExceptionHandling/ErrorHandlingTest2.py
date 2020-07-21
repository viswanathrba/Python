try:
    a = open("anjan.txt", "r")
except Exception as e:
    print("Error Message", e)
finally:
    print("test")