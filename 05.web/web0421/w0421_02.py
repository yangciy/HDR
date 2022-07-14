from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re
for year in range(2017,2022):
    url="https://search.daum.net/search?w=tot&q={}년영화순위&DA=MOR&rtmaxcoll=MOR".format(year)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    info=soup.find("ol",{"class":"type_plural list_exact movie_list"})
    info1=info.find_all("li")

    for i, j in enumerate(info1):
        title = j.find("div",{"class":"wrap_cont cont_type2"}).div.get_text().strip()
        rate = float(j.find("em",{"class":"rate"}).get_text())
        image= j.find("img",{"class":"thumb_img"})["src"]
        ppp=j.find_all("dd",{"class":"cont"})
        ppp=ppp[-1].get_text()
        link=j.find("a",{"class":"tit_main"})["href"]
        if image.startswith("//"):
            print("https:"+image)
        print(image)
        img_res=requests.get(image)
        img_res.raise_for_status()
        # with open("movie{}_{}.jpg".format(year,i+1),"wb") as f:
        #     f.write(img_res.content)    
        print("제목: ", title)
        print("평점: ",rate)
        print("이미지: ",image)
        print("누적: ",ppp)
        print("바로가기: ","https://search.daum.net/search"+link)
        if i >=1:
            break
# images= info1.find("img",{"class":"thumb_img"})
# title=info1.find("div",{"class":"wrap_cont cont_type2"}).div.get_text().strip()
# rate=info1.find("div",{"class":"wrap_cont cont_type2"}).dl.dd.em.get_text()
# # print(images[0]["src"])
# print(title)
# print(rate)
# print(len(info1))
# for i, image in enumerate(images):
#     img_url = image["src"]
#     if img_url.startswith("//"):
#         print("https:"+img_url)
#     print(img_url)
#     img_res=requests.get(img_url)
#     img_res.raise_for_status()

#     with open("movir2021_{}.jpg".format(i+1),"wb") as f:
#         f.write(img_res.content)