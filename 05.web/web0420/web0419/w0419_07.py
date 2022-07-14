import requests
from bs4 import BeautifulSoup
# url="https://comic.naver.com/index"
# url2='https://shoppinghow.kakao.com/siso/p/bestRank/'
url="https://news.daum.net"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
res =requests.get(url,headers=headers)
res.raise_for_status()

soup= BeautifulSoup(res.text,"lxml")
a=soup.find("strong",{"class":"tit_g"})
print("최신뉴스 1 :",a.get_text().strip())
print("바로가기 링크 : ",a.a["href"])
# atag=soup.find("a",{"id":"recommand_titleName_0"})
# ahref=atag["href"]
# print("1위 : ",atag.get_text())
# print("바로가기 링크: ","https://comic.naver.com"+ahref)

# res1 = requests.get(url2,headers=headers)
# res1.raise_for_status()

# soup1= BeautifulSoup(res1.text,"lxml")

# btext=soup1.find("ul",{"class":"list_product"})
# bhref=btext["href"]
# print(btext.a.get_text())
