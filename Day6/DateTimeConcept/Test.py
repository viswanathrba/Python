import datetime

#print(datetime.datetime.now())

a = '24-07-2020'
      # d  m   y/y
      # a/A  b/B   y/Y

b = datetime.datetime.strptime(a, "%d-%m-%Y")

print(b.strftime("%y, %B, %A, %a, %b"))