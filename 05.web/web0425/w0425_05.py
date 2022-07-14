import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser= webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
browser.get("https://www.melon.com/chart/index.htm")
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

# 셀레니움으로 html 소스 가져오기
charts= soup.find_all("tr",{"class":"lst50"})
print(charts[0].find("div",{"class":"ellipsis rank03"}).get_text())
print(charts[0].find("span",{"class":"cnt"}))

# url="https://www.melon.com/chart/index.htm"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")


# browser = webdriver.Chrome(r"/Users/uk/데이터분석가/chromedriver")
# browser.get("https://www.melon.com/chart/index.htm")

# elem= browser.find_element_by_link_text("증권")
# elem.click()
# # 현재 페이지 url가져오기
# page_url = browser.page_source
# soup = BeautifulSoup(page_url,"xml")

# with open("elem.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
