import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
url="https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
res= requests.get(url,headers=headers)
soup= BeautifulSoup(res.text,'lxml')
web_table= soup.find("table",{"class","viewList"})
cartoons=web_table.find_all("tr")
allRate=0
for i, cartoon in enumerate(cartoons):
    toons_title=(cartoon.find("td",{"class":"title"}))
    if not toons_title:
        continue
    toons_rate=(cartoon.find("strong"))
    toons_date=(cartoon.find("td",{"class":"num"}))
    rate=float(toons_rate.get_text())
    print(toons_title.a.get_text(),end=" ")
    print(toons_rate.get_text(),end=" ")
    print(toons_date.get_text())
    allRate+=rate
print("전체평군 {:.2f}".format(allRate/(len(cartoons)-1)))

# print(toons_rate)
# print(cartoons)


# cartoons= all.find_all("tr")
# cartoons=soup.find_all("td",{"class":"title"})
# print(cartoons[0].get_text())


# for i,cartoon in enumerate(cartoons):
#     dt= cartoon.find("td",{"class","title"})
#     dr= cartoon.find("strong")
#     print(dt)
#     print(dr)
    


# print(all)
# a1=all.find_all("strong")
# print(a1)

# print(dr)
    
    