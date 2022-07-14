import requests
from bs4 import BeautifulSoup

headers={"User=Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
url="https://comic.naver.com/webtoon/weekday"
res = requests.get(url,headers=headers)
soup= BeautifulSoup(res.text,'lxml')
cul = soup.find("div",{"class":"col_inner"}).ul
cartoons = cul.find_all("li")
for i,cartoon in enumerate(cartoons):
    clink= cartoon.a["href"]
    ctxt= cartoon.find("a",{"class","title"}).get_text()
    print("{:2d}: {}".format(i+1,ctxt))
    print("링크주소","https://comic.naver.com"+clink)