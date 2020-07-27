import re
a = "88888 bangalAAAAorejjjjjjjjjj 31 98789898899 chennai pune"

#Syntax module_name.option(pattern, string_variable).group()
#b = re.search("[a-z]+", a).group()

#Search Option
#b = re.search("[0-9]+", a).group()

b = re.findall("[0-9]+", a)
print(b)