import requests
from bs4 import BeautifulSoup
import re
for page in range(1,5):
    url="https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220421&hh=15&rtm=Y&pg={}".format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")


    list=soup.find("table",{"class":"list-wrap"}).tbody
    # print(list)
    sings=list.find_all("tr",{"class":"list"})
    # info=sings[0].find("td",{"class":"info"})
    # title=info.find("a",{"class":"title ellipsis"}).get_text()
    # image=info.find("a",{"class":"cover"}).img["src"]
    print(len(sings))
    for i, sing in enumerate(sings):
        if page==1:
            info=sing.find("td",{"class":"info"})
            # num=sing.find("td",{"class":"number"}).get_text()
            title=info.find("a",{"class":"title ellipsis"}).get_text().strip()
            artist=info.find("a",{"class":"artist ellipsis"}).get_text()
            image=sing.find("a",{"class":"cover"}).img["src"]
            image="https:"+image
            print("순위 :" ,(i+1))
            print("제목 :" ,title)
            print("가수 :" ,artist)
            print("이미지 :" ,image)
            # image=image.replace("//","")
            img_res=requests.get(image)
            img_res.raise_for_status()
            with open("sing{}.jpg".format(i+1),"wb") as f:
                f.write(img_res.content)  
        else:
            info=sing.find("td",{"class":"info"})
            # num=sing.find("td",{"class":"number"}).get_text()
            title=info.find("a",{"class":"title ellipsis"}).get_text().strip()
            artist=info.find("a",{"class":"artist ellipsis"}).get_text()
            image=sing.find("a",{"class":"cover"}).img["src"]
            image="https:"+image
            print("순위 :" ,((page-1)*50+(i+1)))
            print("제목 :" ,title)
            print("가수 :" ,artist)
            print("이미지 :" ,image)
            # image=image.replace("//","")
            img_res=requests.get(image)
            img_res.raise_for_status()
            with open("sing{}.jpg".format((page-1)*50+(i+1)),"wb") as f:
                f.write(img_res.content)  