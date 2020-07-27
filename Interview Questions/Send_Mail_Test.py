import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart()
message["From"] = "pythonlogontest2@gmail.com"
message["TO"] = "pattikondapeddanna697@gmail.com"
message["Subject"] = "peddanna peddu"
message["Body"] = "Hi peddanna Good morning"
message.attach(MIMEText(message["Body"]))

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login('pythonlogontest2@gmail.com', '7569732323')
server.sendmail(message("From"), message("To"), message.as_string())