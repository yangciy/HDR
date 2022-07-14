import requests
from bs4 import BeautifulSoup
url= "https://www.naver.com"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
res= requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

with open("bbb.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())    #prettify() : html을 정렬해서 출력
# 파일 저장
with open("aaa.html","w",encoding="UTF-8") as f:
    f.write(res.text)
