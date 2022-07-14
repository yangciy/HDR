# naver
# 지마켓을 검색해서 지마켓 페이지 이동
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
browser.get("https://www.daum.net")
elem = browser.find_element_by_id("q")
elem.send_keys("부동산")
elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_link_text("G마켓 - 쇼핑을 바꾸는 쇼핑")
# elem.click()