import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
url="http://corners.gmarket.co.kr/Bestsellers"
res= requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')
# item= soup.find("li",{"class":'first'})
# item_name= item.find("a",{"class":"itemname"})
# price= item.find("div",{"class":"s-price"})
# print(item_name.get_text())
# print(price.span.get_text())


t_div= soup.find("div",{"id":"topPlusItems"})
t2_div= t_div.find_next_sibling("div")
items=t2_div.find_all("li")
# print(items)
# print(len(items))
# print(items[1].find("a",{"class":"itemname"}).get_text())
# send= items[1].find("div",{"class":"icon"})
# s_t= send.img["alt"]
# print(s_t)
for i, item in enumerate(items):
    name= items[i].find("a",{"class":"itemname"})
    price= items[i].find("div",{"class":"s-price"})
    send= items[i].find("div",{"class":"icon"}).img
    print(name.get_text())
    print(price.span.get_text())
    if send :
        if send["alt"] =="스마일배송":
            print("무료배송")
        else:
            print(send["alt"])
            
            
        

