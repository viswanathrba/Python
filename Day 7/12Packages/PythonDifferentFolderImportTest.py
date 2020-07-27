#Style1
from DifferentFolderImportTest import Subtraction

print(Subtraction.sub(4, 5))
print(Subtraction.sub(14, 5))
print(Subtraction.sub2(14, 15))
print(Subtraction.sub2(14))


#Style2
from DifferentFolderImportTest.Subtraction import *

print(sub(4, 5))
print(sub(14, 5))
print(sub2(14, 15))
print(sub2(14))

#Style2
from DifferentFolderImportTest.Subtraction import sub

print(sub(4, 5))
print(sub(14, 5))
print(sub2(14, 15))
print(sub2(14))