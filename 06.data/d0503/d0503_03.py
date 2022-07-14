import requests
from bs4 import BeautifulSoup
import csv
import re
for year in range(2020,2023):
    url="http://www.statiz.co.kr/salary.php?opt=0&sopt={}&te=".format(year)
# url="http://www.statiz.co.kr/salary.php?opt=0&sopt=2022&te="
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")
    list=soup.find('table',{"class":"table table-striped"})
    aa=list.find_all('tr')
    filename="{} 연봉.csv".format(year)
    f=open(filename,"w",encoding="utf-8 sig")
    writer =csv.writer(f)
    title="선수 연도 팀 연봉(만원) WAR"
    print(title)
    title=title.split(' ')
    writer.writerow(title)


    for i ,j in enumerate(aa):
        data=[]
        if i==0:
            continue
        name=j.find_all('td')[0].get_text()
        year=j.find_all('td')[1].get_text()
        team=j.find_all('td')[2].get_text()
        salary=j.find_all('td')[3].get_text()
        salary=re.sub(r',','',salary)
        war=j.find_all('td')[4].get_text()
        
        # aa_list=i.find_all('td')[0]
        data.append(name)
        data.append(year)
        data.append(team)
        data.append(salary)
        data.append(war)
        print(name, year, team, salary, war)
        writer.writerow(data)
    f.close()
