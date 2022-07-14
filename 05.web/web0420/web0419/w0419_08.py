import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
url="https://comic.naver.com/webtoon/weekday"
res= requests.get(url,headers=headers)
soup= BeautifulSoup(res.text,'lxml')

allday= soup.find("div",{"class":"list_area daily_all"})
ad=allday.find_all("li")
for i , j in enumerate(ad):
    print("{:2d}: {}".format(i+1,j.get_text().strip()))
    print("링크주소","https://comic.naver.com"+j.a["href"])

# monday=soup.find("div",{"class":"col_inner"})
# mW= monday.find_all("li")
# # a=monday
# # print(a)
# print(mW)
# for i , j in enumerate(mW):
#     print("{:2d}: {}".format(i+1,j.get_text().strip()))
#     print("링크주소","https://comic.naver.com"+j.a["href"])
    



# rankall=soup.find("ol",{"id":"realTimeRankFavorite"})   # 10개의 인기웹툰 ol태그 가져옴 (li태그 10개 담겨져있음)
# cartoons=rankall.find_all("li")                         # 10개의 li태그를 리스트 형태로 반환
# # print(cartoons)
# for i,cartoon in enumerate(cartoons):
#     print("{:2d}위 : {}".format(i+1,cartoon.a.get_text()))
#     print("링크주소 :","https://comic.naver.com"+cartoon.a["href"])

# rank1=soup.find("li",{"class":"rank01"})
# print(rank1.find_next_sibling("li").find_next_sibling("li"))
# next_sibling 현재기준 바로 다음 검색
# find_next_sibling 현재태그부터 li를 찾을 때까지 검색
# print(rank2.previous_sibling.previous_sibling)
# previous_sibling 현재기준 바로 전 검색
# find_previous_sibling 현재기준 이전에서 li 찾을 때 까지 검색
