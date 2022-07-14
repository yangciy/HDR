import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.gmail.com"
smtpPort = 587

sendEmail = "didghddnr@gmail.com"
password="ogrqmicrztinfeln"
recvEmail = "didghddnr@naver.com"
# 글자
title="gmail발송제목"
content="gmail 발송"

msg = MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']= title
s = smtplib.SMTP(smtpName,smtpPort)
s.ehlo()
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.close()