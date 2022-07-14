import requests
from bs4 import BeautifulSoup
url="https://comic.naver.com/index"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
res =requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #text를 lxml파싱해서 soup 가져옴
# print(soup)
# print('title: ',soup.title)
print('title제목: ',soup.title.get_text())
# print("a : ",soup.a)
# print("a attr : ",soup.a.attrs)
# print("a attr href : ",soup.a["href"])
# print("a text : ",soup.a.get_text())
# print("div : ",soup.div)
# print("div : ",soup.div.attrs)
# print("div id : ",soup.div["id"])
print("div id=menu : ",soup.find("div",attrs={"id":"menu"}))
