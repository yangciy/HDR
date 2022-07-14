import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui


browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
url="https://new.land.naver.com/complexes/2992?ms=37.543599,126.95604,17&a=APT:ABYG:JGC&e=RETAIL"
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('//*[@id="complexOverviewList"]/div[2]/div[1]/div[2]/div/div[1]/button/span').click()
browser.find_element_by_xpath('//*[@id="complexOverviewList"]/div[2]/div[1]/div[2]/div/div[1]/div/div/ul/li[2]/label').click()
browser.find_element_by_xpath('//*[@id="complexOverviewList"]/div[2]/div[1]/div[2]/div/div[1]/div/button/i').click()

time.sleep(2)
prev_height=browser.execute_script("return articleListArea.scrollHeight")



while True:

    pyautogui.moveTo(200,600)
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    curr_height=browser.execute_script("return articleListArea.scrollHeight")
    if prev_height == curr_height:
        break

    prev_height = curr_height
page_html =browser.page_source
soup=BeautifulSoup(page_html,'lxml')
list=soup.find("div",{"class":"infinite_scroll"})
aa=list.find_all("div",{"class":"item false"})

print(aa[49].find("div",{"class":"item_title"}).get_text())
print(aa[49].find("div",{"class":"price_line"}).get_text())
b=aa[49].find("div",{"class":"info_area"}).find('p',{"class":"line"})
print(b.get_text())
 