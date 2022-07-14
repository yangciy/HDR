import requests
from bs4 import BeautifulSoup
url="https://comic.naver.com/index"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
res =requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print("li class rank01: ",soup.find("li",{"class":"rank01"}))
print("li class rank01 text: ",soup.find("li",{"class":"rank01"}).get_text())
print("li class rank01 text: ",soup.find("li",{"class":"rank01"}).a.get_text())

aurl= soup.find("li",{"class":"rank01"}).a
atxt= soup.find("li",{"class":"rank01"}).a.get_text()
print("1위 : {}".format(atxt))
print("바로가기 링크: ","https://comic.naver.com"+aurl["href"])