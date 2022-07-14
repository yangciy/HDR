import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
url="https://comic.naver.com/webtoon/list?titleId=703846&weekday=tue"
res= requests.get(url,headers=headers)
res.raise_for_status()
soup= BeautifulSoup(res.text,'lxml')
cartoons=soup.find_all("tr")
print(cartoons)
for cartoon in cartoons:
    toon_title=(cartoon.find("td",{"class":"title"}))
    if not toon_title:
        continue
    toon_href=(toon_title.a["href"])
    print(toon_title.a.get_text())
    print("http://comic.naver.com/"+toon_href)