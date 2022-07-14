import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
browser.get("https://www.naver.com")
# 자바스크립트 소스 코드 추가
browser.find_element_by_class_name("link_login").click()
input_js ="document.getElementById('id').value='{id}';\
    document.getElementById('pw').value='{pw}'\
        ".format(id='didghddnr',pw='1Q2W3E11!!')
time.sleep(random.uniform(1,3))
browser.execute_script(input_js)

time.sleep(random.uniform(1,3))


browser.find_element_by_id("log.login").click()
browser.find_element_by_link_text("메일").click()
browser.find_element_by_link_text("메일쓰기").click()


# mail_js="document.getElementById('toUL').value='{mail}';\
#     doucment.getElementById('subject').value='{title}'".format(mail='didghddnr@naver.com',title='test')
# time.sleep(random.uniform(1,3))
# browser.execute_script(mail_js)


browser.find_element_by_id("toInput").send_keys("didghddnr@naver.com")
browser.find_element_by_id("subject").send_keys("test")

browser.find_element_by_class_name("se2_inputarea").send_keys("test")
browser.find_element_by_id("sendBtn").send_keys(Keys.ENTER)
# elem= browser.find_element_by_class_name("link_login")
# elem.click()
# elem= browser.find_element_by_id("id")
# elem.send_keys("didghddnr")
# elem= browser.find_element_by_id("pw")
# elem.send_keys("1Q2W3E11!!")
# elem.send_keys(Keys.ENTER)
# browser.find_element_by_class_name("btn_login").click()
