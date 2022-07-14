import requests
from bs4 import BeautifulSoup
import re
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
for i in range(1,6):
    url="https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(i)+"&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
    res= requests.get(url,headers=headers)
    res.raise_for_status()
    soup= BeautifulSoup(res.text,'lxml')
    items= soup.find_all("li",{"class",re.compile("^search-product")})
    cnt=0
    allcnt=0
    for i, item in enumerate(items):
    # "li",{"class",re.compile("__ad-badge$")}
        ad=item.find("span",{"class":"ad-badge-text"})
        if  ad:
            continue
        rate_t=item.find("em",{"class":"rating"})
        if not rate_t :
            continue
        rate=float(item.find("em",{"class":"rating"}).get_text())
        rate_cnt=item.find("span",{"class":"rating-total-count"}).get_text()
        rate_cnt1=int(rate_cnt[1:-1])
        if rate>=4.5 and rate_cnt1>=50:
            product_name=item.find("div",{"class":"name"}).get_text()
            if "Apple" not in product_name:
                print("상품명 : ",product_name)
                print("가격 : ",item.find("strong",{"class":"price-value"}).get_text())
                print("구매링크 : ","https://www.coupang.com"+item.a["href"])
                cnt+=1
        allcnt+=cnt   
print("검색된 개수 : ",allcnt )
    # url ="https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# print(len(items))
# print(rate) #평점
# print(rate_cnt1) #상품평
# items= soup.find_all("li",{"class","search-product"})
# product_name=items[0].find("div",{"class":"name"}).get_text()
# if "기가바이트" in product_name:
#     print(product_name)
# for i, item in enumerate(items):
#     if rate>4.5 and rate_cnt1>50:
#         print(item.find("div",{"class":"name"}).get_text())
#         print(item.find("strong",{"class":"price-value"}).get_text())
#         print("https://www.coupang.com"+item.a["href"])