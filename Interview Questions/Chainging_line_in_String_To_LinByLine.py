#How to chaing lines in string to line by line?
from collections import OrderedDict

line = "peddanna \n nandu \n anjan \n adi \n nari"
print line

print "\n".join(list(OrderedDict.fromkeys(line.split("\n"))))