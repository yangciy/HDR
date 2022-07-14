import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
import re
import csv

filename="google_movie.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer=csv.writer(f)
title="제목 평점 가격 바로가기".split(" ")
writer.writerow(title)
# 화면 열리지않고 실행
options = webdriver.ChromeOptions()
options.headless =True
options.add_argument("window-size=1920x1080")

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver",options=options)
url="https://play.google.com/store/movies"
browser.maximize_window()
browser.get(url)

prev_height=browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 스크롤 내리기는 - 올리기는 +
    # pyautogui.moveTo(400,400)
    # pyautogui.scroll(-prev_height)
    time.sleep(2)
    curr_height=browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break

    prev_height = curr_height
    
browser.get_screenshot_as_file("googleMovie.jpg")
page_html =browser.page_source
soup= BeautifulSoup(page_html,"lxml")
lists= soup.find_all("div",{"class":"aoJE7e b0ZfVe lZ2Ckc"})
list=lists[8].find_all("div",{"class":"ULeU3b neq64b"})
# list_1=list.find_all("div",{"class":"hP61id"})
print(list)
# a=list_1.find("div",{"class":"Epkrse"}).get_text()


# print(lists[0].find("div",{"class":"hP61id"}))
for i,j in enumerate(list):
    movie=[]
    path=j.find("div",{"class":"hP61id"})
    a=path.find("div",{"class":"Epkrse"}).get_text()
    b=path.find("div",{"class":"LrNMN"}).get_text()
    c=path.find("span",{"class":"VfPpfd VixbEe"}).get_text()
    d=c
    image=j.find("div",{"class":"TjRVLb"}).find('img')["src"]
    link=j.find("a",{"class":"Si6A0c ZD8Cqc"})["href"]
    mvlink="https://play.google.com"+link
    c=re.sub(r"₩",'',c)
    c=int(re.sub(r',','',c))
    if c<=6000:
        movie.append(a)
        movie.append(b)
        movie.append(c)
        movie.append(mvlink)
        img_res=requests.get(image)
        img_res.raise_for_status()
        with open("{}.jpg".format(a),"wb") as f:
            f.write(img_res.content)    
        writer.writerow(movie)
        # print(image)
        print("제목: ",a)
        print("평점: ",b)
        print("가격 :",d)
        print("바로가기 :",mvlink)
        
        print("-"*40)
f.close()
# browser.close()
browser.quit()

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"\
#     ,"Accept-Language":"ko"}
# res =requests.get(url,headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# with open("movie.html","w",encoding="utf-8")as f:
#     f.write(soup.prettify())