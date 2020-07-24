from datetime import datetime

a = "20, July, Friday, Fri, Jul"

b = datetime.strptime(a, "%y, %B, %A, %a, %b")

print(type(b.strftime("%d-%m-%Y")))

