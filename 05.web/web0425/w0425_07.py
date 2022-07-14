from dataclasses import replace
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import re
import csv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
url="https://flight.naver.com"
browser.maximize_window()
browser.get(url)
browser.find_element_by_class_name("select_code__d6PLz").click()
time.sleep(2)
browser.find_element_by_class_name("autocomplete_Collapse__tP3pM").click()
time.sleep(2)
browser.find_element_by_class_name("autocomplete_Airport__3_dRP").click()

# 도착
browser.find_elements_by_class_name("select_code__d6PLz")[1].click()

time.sleep(2)
browser.find_element_by_class_name("autocomplete_Collapse__tP3pM").click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()

# 가는 날 오는 날
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[3]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button').click()
# 인원 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[3]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(2)
# 검색
browser.find_element_by_class_name("searchBox_search__2KFn3").click()
browser.find_element_by_class_name("searchBox_search__2KFn3").click()
# time.sleep(10)
# 브라우저 로딩 후 10초대기, 화면에서 선택한 요소가 있는지 체크
WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div/button')))

prev_height=browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(2)
    curr_height=browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break

    prev_height = curr_height
page_html =browser.page_source
soup = BeautifulSoup(page_html,'lxml')
flights =soup.find_all("div",{"class":"domestic_Flight__sK0eA result"})
filename="제주도저가.csv"
f=open(filename,"w",encoding="utf-8 sig")
writer = csv.writer(f)
title=["항공사","가격","출발시간","도착시간"]
writer.writerow(title)
for i, flight in enumerate(flights):
    
    goair=[]
    price=flight.find("i",{"class":"domestic_num__2roTW"}).get_text()
    price=int(re.sub(r',','',price))
    fname=flight.find("b",{"class":"name"}).get_text()
    st=flight.find_all("b",{"class":"route_time__-2Z1T"})[0].get_text()
    rt=flight.find_all("b",{"class":"route_time__-2Z1T"})[1].get_text()
    if price <50000:
        goair.append(fname)
        goair.append(price)
        goair.append(st)
        goair.append(rt)
        writer.writerow(goair)
f.close()




# browser.find_element_by_class_name('tabContent_option__2y4c6 select_Passenger__36sFM').click()
# browser.find_elements_by_link_text("27")[0].click()

# time.sleep(10)
# page_url= browser.page_source
# soup = BeautifulSoup(page_url,"lxml")
# print(soup)

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# url="https://m-flight.naver.com/flights/domestic/GMP-CJU-20220524/CJU-GMP-20220525?adult=2&fareType=YC"
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

# list = soup.find("div",{"class":"domestic_results__yNAgI"})
# print(list)
# air =soup.find_all("div",{"class":"domestic_Flight__sK0eA result"})
# print(len(air))
