import requests
from bs4 import BeautifulSoup
import re
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
adate=input('시작날짜 입력(형식:2022-01-01)  ')
bdate=input('끝낼잘자 입력(형식:2022-01-01)  ')

url="https://www.goodchoice.kr/product/result?el_date="+adate+"&sel_date2="+bdate+"&keyword=오션뷰"
res= requests.get(url,headers=headers)
res.raise_for_status()
soup= BeautifulSoup(res.text,'lxml')

# 오션뷰
# 평점, 상품평 9.5 이상 상품평 500개 이상 출력

items= soup.find_all("li",{"class":"list_4"})
cnt=0
# print(items)
for i, item in enumerate(items):
    name= item.find("p",{"class":"pic"}).img
    if item.find("div",{"class":"name"}).find("div",{"class":"badge"}):
        name2 =item.find("div",{"class":"name"}).find("div",{"class":"badge"}).strong.div.next_sibling.strip()
    else :
        name2 =item.find("div",{"class":"name"}).find("strong").get_text()
    url=item.find("a")["href"]
    rate= float(item.find("p",{"class":"score"}).em.get_text())
    rate_cnt= item.find("p",{"class","score"}).span.next_sibling.strip()
    rate_cnt=int(rate_cnt[1:-1])
    if rate >=9.5 and rate_cnt >=100:
        cnt+=1
        print("{}. 숙소명: {}".format(cnt,name["alt"]))
        print("평점: ",rate)
        print("추천수: ",rate_cnt)
        print("바로가기 링크: ",url)
        print("--"*30)
# rate_cnt1= (rate_cnt,re.compile("^("))
# print(rate_cnt1)