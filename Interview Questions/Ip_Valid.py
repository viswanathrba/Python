#How to identifay Ip valid number
a = ['1.2.3.4', '5.6.7.9999', '0.0.0.-1', '12.13.14.25']
for ip in a:
    if [0 <= int(i) <= 255 for i in ip.split(".")].count(True) == 4:
        print "{} it is valid ip".format(ip)
    else:
        print "{} it is not valid ip".format(ip)
        
