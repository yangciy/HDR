import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
import re

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
print(content)