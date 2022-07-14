import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
import re
import csv
options = webdriver.ChromeOptions()
# options.headless =True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15")

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver",options=options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })

url="https://www.coupang.com"
browser.maximize_window()
browser.get(url)
# prev_height=browser.execute_script("return document.body.scrollHeight")
# time.sleep(5)
# while True:
#     # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     # 스크롤 내리기는 - 올리기는 +
#     pyautogui.moveTo(400,400)
#     pyautogui.scroll(-prev_height)
#     time.sleep(2)
#     curr_height=browser.execute_script("return document.body.scrollHeight")

#     if prev_height == curr_height:
#         break

#     prev_height = curr_height
# page_html =browser.page_source
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import pyautogui
# import requests
# from bs4 import BeautifulSoup
# import time
# import re
# import random

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import os

# url = 'https://www.coupang.com/'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach',True)
# userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
# options.add_argument(userAgent)

# browser = webdriver.Chrome(chrome_options=options)
# browser.maximize_window()
# browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
# browser.get(url)
# time.sleep(random.uniform(1,3))
# # #스크롤내림
# prev_height = browser.execute_script("return document.body.scrollHeight")
# while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(random.uniform(1,3))
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == curr_height:
#         break
#     prev_height = curr_height
    
    
# time.sleep(random.uniform(1,3))



# page_url = browser.page_source
# soup = BeautifulSoup(page_url,"lxml")