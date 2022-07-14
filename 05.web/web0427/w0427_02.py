import smtplib
from email.mime.text import MIMEText                # MIME 객체- 보내는사람, 받는사람, 내용
from email.mime.multipart import MIMEMultipart      # 객체 - 보내는사람, 받는사람, 내용, 파일첨부
from email.mime.base import MIMEBase                # 파일첨부 라이브러리
from email import encoders                          # 파일첨부할수 있는 형태로 인코딩

smtpName= "smtp.gmail.com"
smtpPort= 587
sendEmail= "didghddnr@gmail.com"
password="ogrqmicrztinfeln"
recvEmail = "didghddnr@naver.com"

title="주식시세 1~200위까지 첨부"
content= "시가총액 1위에서 200위까지 주식시세를 파일 첨부해서 보냅니다."

msg = MIMEMultipart('alternative')
part2 = MIMEText(content)
part3 = MIMEText('abcdef')
msg.attach(part2)
msg.attach(part3)
msg['From'] = sendEmail
msg['To']= recvEmail
msg["Subject"]= title

part = MIMEBase('application','octet-stream')
with open("시가총액1-200.csv","rb")as f:
    part.set_payload(f.read())
    
encoders.encode_base64(part)

part.add_header("Content-Dispostion","attachment",filename="시가총액1-200.csv")

msg.attach(part)
s=smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.close()