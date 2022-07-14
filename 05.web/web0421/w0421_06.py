from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re
import csv

url="https://www.melon.com/chart/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

song= soup.find("tbody")
rank= song.find("span",{"class":"rank"}).get_text().strip()
title= song.find("div",{"class":"ellipsis rank01"}).get_text().strip()
singer= song.find("div",{"class":"ellipsis rank02"}).a.get_text().strip()
album= song.find("div",{"class":"ellipsis rank03"}).a.get_text().strip()
cnt= song.find("span",{"class":"none"}).next_sibling
print(cnt)
print(rank)
print(title)
print(singer)
print(album)
# filename="멜론탑100.csv"
# f=open(filename,"w",encoding="utf-8 sig")
# writer =csv.writer(f)
# data=[]
# title1="순위, 제목, 가수, 앨범, 좋아요"
# title1=title1.split(",")
# writer.writerow(title1)
# data.append(rank)
# data.append(title)
# data.append(singer)
# data.append(album)
# data.append(cnt)
# writer.writerow(data)
# f.close()