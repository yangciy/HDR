import requests
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
# webdriver 크롬부라우저 변수 할당
browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
browser.get("https://www.naver.com")
elem=browser.find_element_by_class_name("link_login")
print(elem)
elem.click()


elem.send_keys("aaa")
elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[2]/input")
elem.send_keys('1234')
elem= browser.find_element_by_id("log.login")
# elem.click()
# 엔터입력
elem.send_keys(Keys.ENTER)
# 뒤로가기
browser.back()
# 앞으로가기
browser.forward()
# 새로고침
browser.refresh()