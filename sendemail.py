import compileInfo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

compileInfo.getEmail()
print("DONE WITH EMAIL")

me = "shivamchowdhary15@gmail.com"
my_password = r"rqsoafrgytazgysi"
people = "shivamchowdhary15@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Your morning news for " + datetime.date.today().strftime("%m/%d")
msg['From'] = me
msg['To'] = people

with open("test.html","r") as f:
    html = f.read()
part2 = MIMEText(html, 'html')

msg.attach(part2)

# Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
s = smtplib.SMTP_SSL('smtp.gmail.com')
# uncomment if interested in the actual smtp conversation
# s.set_debuglevel(1)
# do the smtp auth; sends ehlo if it hasn't been sent already
s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()