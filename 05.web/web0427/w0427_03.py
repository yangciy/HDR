# 네이버 증권 주요뉴스 제목 링크주소 6개
# 금융 검색 : 삼성전자 삼성전자 종목명,현재가 전일대비 등락율 매도호가 매수호가 거래량 거래대금
# 네이버 날씨 주간예보 오늘오전오후 10;21 내일 오전 오후 11:22
# 파일첨부 멜론 1~100위까지 csv파일 저장 순위,곡정보,엘범,좋아요


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
import re
import csv
import os

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
url="https://www.naver.com"
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[3]/a').click()
page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
apath=soup.find("div",{"class":"section_strategy"})
list=apath.find_all('li')
content_a=''
content_b=''
content_c=''
content_d=''
for i in list:
    link=i.a["href"]
    link="https://finance.naver.com"+link
    # print(link)
    title=i.get_text()
    content=title+link+'\n'    
    content_a+=content
print(content_a)

browser.find_element_by_xpath('//*[@id="stock_items"]').send_keys("삼성전자")
browser.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/button').click()
time.sleep(2)
page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
bpath=soup.find_all('tr')
title=''
tpath=bpath[0].find_all('th')
a1=tpath[0].get_text()
a2=tpath[1].get_text()
a3=tpath[2].get_text()
a4=tpath[3].get_text()
a5=tpath[4].get_text()
a6=tpath[5].get_text()
a7=tpath[6].get_text()
a8=tpath[7].get_text()
ba="{:6s} {:6s} {:6s} {:6s} {:6s} {:6s} {:6s} {:6s}".format(a1,a2,a3,a4,a5,a6,a7,a8)
tpath=bpath[1].find_all('td')
a1=tpath[0].a.get_text()
a2=tpath[1].get_text()
a3=tpath[2].get_text()
a4=tpath[3].get_text()
a5=tpath[4].get_text()
a6=tpath[5].get_text()
a7=tpath[6].get_text()
a8=tpath[7].get_text()
bb="{:8s} {:8s} {:8s} {:8s} {:8s} {:8s} {:8s} {:8s}".format(a1,a2,a3,a4,a5,a6,a7,a8)
content_b=ba+'\n'+bb+'\n'
print(content_b)



browser.get(url)
browser.find_element_by_xpath('//*[@id="query"]').send_keys('날씨')
browser.find_element_by_xpath('//*[@id="search_btn"]').click()

page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
cpath=soup.find('div',{"class":"list_box"})
list=cpath.find_all('li',{"class":"week_item today"})

for i in list:
    when=i.find('strong',{"class":"day"}).get_text()
    path=i.find_all('span',{"class":"blind"})
    before=path[0].get_text()                           # 오전
    after=path[1].get_text()                            # 오후
    low=i.find('span',{"class":"lowest"}).get_text()        # 최저
    high=i.find('span',{"class":"highest"}).get_text()       # 최고
    cC="{} 오전:{} 오후:{} {} {}".format(when,before,after,low,high)
    cContent=cC+'\n'
    content_c+=cContent
    # print(when)
    # print('오전 :',before)
    # print('오후 :',after)
    # print('최저 :',low)
    # print('최고 :',high)
print(content_c)


filename="멜론 탑100.csv"
f=open(filename,"w",encoding="utf-8-sig",newline='')
writer = csv.writer(f)
Mtitle=["순위","제목","가수","앨범","좋아요"]
writer.writerow(Mtitle)
url="https://www.melon.com"
browser.get(url)
browser.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]').click()
time.sleep(2)
page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
dpath=soup.find('tbody').find_all('tr')
for x,i in enumerate(dpath):
    Mcontent=[ ]
    rank=x+1
    title=i.find('div',{"class":"ellipsis rank01"}).a.get_text()
    singer=i.find('div',{"class":"ellipsis rank02"}).a.get_text()
    album=i.find('div',{"class":"ellipsis rank03"}).a.get_text()
    like=i.find('span',{"class":"cnt"}).get_text()
    like= re.sub(r'[^0-9,]','',like)
    like=re.sub(r',','',like)
    Mcontent.append(rank)
    Mcontent.append(title)
    Mcontent.append(singer)
    Mcontent.append(album)
    Mcontent.append(like)
    writer.writerow(Mcontent)
    # print('제목: ',title)
    # print('가수: ',singer)
    # print('앨범: ',album)
    # print('좋아요: ',like)
f.close()

import smtplib
from email.mime.text import MIMEText                
from email.mime.multipart import MIMEMultipart      
from email.mime.base import MIMEBase                
from email import encoders        

smtpName= "smtp.gmail.com"
smtpPort= 587
sendEmail= "didghddnr@gmail.com"
password="ogrqmicrztinfeln"
recvEmail = "onulee@naver.com"


title="220427_양홍욱"
msg = MIMEMultipart('alternative')
part2 = MIMEText(content_a)
part3 = MIMEText(content_b)
part4 = MIMEText(content_c)
msg.attach(part2)
msg.attach(part3)
msg.attach(part4)
msg['From'] = sendEmail
msg['To']= recvEmail
msg["Subject"]= title
filename='멜론 탑100.csv'
part = MIMEBase('application','octet-stream')
attachment =open(filename,'rb')

part.set_payload((attachment).read())

encoders.encode_base64(part)

part.add_header('Content-Disposition',"attachment", filename= os.path.basename(filename))

msg.attach(part)
s=smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.close()
browser.quit()
