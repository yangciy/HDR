import requests
from bs4 import BeautifulSoup
import re
# 제목, 금액, 링크, 무료배송, 사진을 저장 및 출력하시오. 
url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb#pageNum%%5"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
best= soup.find("div",{"class":"best_prd_box"})
list = best.find("div",{"class":"viewtype catal_ty"})
product= list.find("ul",{"class":"cfix"})
pd= product.find_all("li")

for x,i in enumerate(pd):
    title=i.find("div",{"class":"pname"}).p.get_text()
    price=i.find("strong",{"class":"sale_price"}).get_text()
    send=i.find("div",{"class":"s_flag"}).get_text().strip()
    image=i.find("div",{"class":"img_plot"}).img["src"]
    link=i.div.a["href"]
    print("상품명: ",title)
    print("가격: ",price)
    if send=="":
        print("배송:  유료배송")
    else:
        print("배송: ",send)
    print("이미지: ",image)
    print("바로가기: ",link)
    image_res=requests.get(image)
    image_res.raise_for_status()
    with open("상품{}.jpg".format(x+1),"wb")as f:
        f.write(image_res.content)

    