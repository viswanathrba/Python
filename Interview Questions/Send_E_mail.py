import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart()
msg['From']='pythonlogontest2@gmail.com'
msg['To']='peddanna310@gmail.com'
msg['Subject']='peddanna'
msg['Body']='Test Test Test'
# add in the message body
msg.attach(MIMEText(msg['Body']))

s = smtplib.SMTP('smtp.gmail.com', port=587)
s.starttls()
s.login('pythonlogontest2@gmail.com', '7569732323')
s.sendmail(msg['From'], msg['To'], msg.as_string())