import re
number = "peddanna310@gmail.com"
a = re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", number)
print a.group()

number1 = "pattikondapeddanna697@gmail.com"
a = re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", number1)
print a.group()