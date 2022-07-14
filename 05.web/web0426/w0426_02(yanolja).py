# 초특가 야놀자 제주 리조트 검색 5/27~5/28 스크롤 내려서 
# 제목, 평점, 금액, 링크 (평점 4.0이상) 출력하고 csv파일 저장, 사진 저장

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
import re
import csv

filename="제주 숙소.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer=csv.writer(f)
title="숙소명 바로가기 평점 가격".split(" ")
writer.writerow(title)

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
url="https://www.yanolja.com"
browser.maximize_window()
browser.get(url)

browser.find_element_by_class_name("HomeSearchBar_search__3R15k").click()
browser.find_element_by_class_name("SearchInput_input__342U2").send_keys("제주 리조트")
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[2]/button[1]').click()
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[6]').click()
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[7]').click()
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[4]/button').click()
browser.find_element_by_class_name("SearchInput_input__342U2").send_keys(Keys.ENTER)

    # 스크롤 내리기는 - 올리기는 +
    # pyautogui.moveTo(400,400)
    # pyautogui.scroll(-prev_height)

prev_height=browser.execute_script("return document.body.scrollHeight")
while True:
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 스크롤 내리기는 - 올리기는 +
    pyautogui.moveTo(400,400)
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    curr_height=browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break

    prev_height = curr_height
page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
list=soup.find_all('div',{"class":"PlaceListItemText_container__fUIgA text-unit"})

for i in list:
    data=[]
    title=i.find('a')['title']
    link=i.find('a')['href']
    urlink="https://www.yanolja.com/"+link
    rank=i.find('span',{"class":"PlaceListScore_rating__3Glxf"}) 
    if not rank:
        continue
    rank=rank.get_text() 
    price=i.find('span',{"class":"PlacePriceInfo_salePrice__28VZD"}).get_text()

    if price=="예약마감":
        continue
    rank=float(rank)
    if rank>=4.0:
        img=i.find('div',{"class":"PlaceListImage_imageText__2XEMn"})['style']
        imgurl=img[img.find('https'):-3]
        img_res=requests.get(imgurl)
        img_res.raise_for_status()
        with open("{}.jpg".format(title),"wb") as f:
         f.write(img_res.content)        
        data.append(title)
        data.append(urlink)
        data.append(rank)
        data.append(price)
        writer.writerow(data)
        print("숙소명 :",title)
        print("바로가기 :",urlink)
        print("평점 :",rank)
        print("가격 :",price)
        print("-"*30)

f.close()