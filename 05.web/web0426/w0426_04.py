# 메일발송 라이브러리
import smtplib 
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

smtpName = "smtp.naver.com" # 메일 서버주소
smtpPort = 587              # 메일서버 포트번호

sendEmail="didghddnr@naver.com"     # 보내는 사람
password="1Q2W3E11!!"               # 패스워드
recvEmail="didghddnr@naver.com"    # 받는사람 주소

title="파이썬 이메일 보내기"
content="파이썬 수업이 진행중입니다. 현재 38일차입니다."


browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
url="https://www.google.co.kr"
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('한소희')
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

browser.find_element_by_xpath('//*[@id="rso"]/div[5]/div/div[1]/div[1]/div/a/h3').click()
page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
list=soup.find("div",{"class":"article_body fs3"})
gisa=list.find_all('p')
content=''
for i in gisa:
    content+=i.get_text()
# MIME 객체
msg =MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['Subject']=title

# 메일서버주소 정보 smtp.naver.com/587
s = smtplib.SMTP(smtpName,smtpPort)
# 메일 서버 접근
s.starttls()
# 메일 서버 로그인(id,password)
s.login(sendEmail,password)
# 메일 발송(보내는주소, 받는주소, 내용)
s.sendmail(sendEmail,recvEmail,msg.as_string())
# 메일 닫기
s.close()