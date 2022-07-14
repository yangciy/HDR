# [ 문제 3 ] http://taas.koroad.or.kr/ > 한눈에 보는 통계 > 주요 교통사고 통계 >교통사고비교 >
# 교통여건년도별 통계를 화면에 출력하고, csv파일로 저장하시오.

import requests
from bs4 import BeautifulSoup
import re
import csv
title=[]
a,b,c,d,e=[],[],[],[],[]

url="http://taas.koroad.or.kr/sta/acs/gus/selectTrnsportCnd.do?menuId=WEB_KMP_OVT_MVT_TAC_TAT"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

roadlist=soup.find("table",{"class":"table01"})
list=roadlist.find_all("tr")

filename="교통여건.csv"
f=open(filename,"w",encoding="utf-8 sig")
writer = csv.writer(f)
for i in list:
    temp=i.get_text()
    temp=re.sub(r' ','',temp)
    temp=re.sub(r'\n',' ',temp)
    temp=temp.split(" ")
    for x,i in enumerate(temp):
        if i=="":
            continue
        elif x==1:
            title.append(i)
        elif x==2:
            a.append(i)
        elif x==3:
            b.append(i)
        elif x==4:
            c.append(i)
        elif x==5:
            d.append(i)
        elif x==6:
            e.append(i)
# writer.writerow(title)
writer.writerow(title)
writer.writerow(a)
writer.writerow(b)
writer.writerow(c)
writer.writerow(d)
writer.writerow(e)
f.close()
for i in range(5):
    print("{:12s}".format(title[i]),end=" ")
print("")
for i in range(5):
    print("{:18s}".format(a[i]),end=" ")
print("")
for i in range(5):
    print("{:18s}".format(b[i]),end=" ")
print("")
for i in range(5):
    print("{:18s}".format(c[i]),end=" ")
print("")
for i in range(5):
    print("{:18s}".format(d[i]),end=" ")
print("")
for i in range(5):
    print("{:18s}".format(e[i]),end=" ")
print("")
