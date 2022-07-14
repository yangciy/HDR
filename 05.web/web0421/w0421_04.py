from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re
import csv

url="https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

filename="시가총액1-200.csv"
f=open(filename,"w",encoding="utf-8 sig")
writer =csv.writer(f)
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE"
title=title.split("\t")
writer.writerow(title)
data_rows = soup.find("table",{"class":"type_2"}).tbody.find_all("tr")
for row in data_rows:
    columns= row.find_all("td")
    if len(columns)<=1:
        continue
    data=[]
 
    for column in columns:
        data.append(column.get_text().strip())
    writer.writerow(data)
f.close()