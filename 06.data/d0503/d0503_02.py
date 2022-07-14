import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv


# filename='daum_movie.csv'
# m_title='제목 평점 개봉 누적관객'
# m_title=m_title.split(" ")
# f=open(filename,"w",encoding='utf-8-sig')
# writer=csv.writer(f)
# writer.writerow(m_title)
# # 다음 영화 웹스크래핑 2016~2021- 5개
# # 제목 평점 개봉일 누적 
# # 추천 점수 컬럼(관객수*평점)/100
# for year in range(2016,2022): 
#     url="https://search.daum.net/search?w=tot&q={}년영화순위&DA=MOR&rtmaxcoll=MOR".format(year)
#     headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
#     res = requests.get(url,headers=headers)
#     soup = BeautifulSoup(res.text,"lxml")
    
#     info=soup.find("ol",{'class':"type_plural list_exact movie_list"})
#     info1=info.find_all('li')
    
#     for i in info1:
#         data=[]
        
    
#         title=i.find('div',{"class":"wrap_cont cont_type2"}).div.get_text().strip()
#         rate=i.find('em',{"class":"rate"}).get_text()
#         open=i.find_all('dd',{'class':'cont'})[0].get_text().strip()
#         many=i.find_all('dd',{'class':'cont'})[2].get_text()
#         rate=float(rate)
#         many=re.sub(r',','',many)
#         many=re.sub(r'명','',many)
#         many=int(many)
#         data.append(title)
#         data.append(rate)
#         data.append(open)
#         data.append(many)
#         writer.writerow(data)
#         print("제목: ",title)
#         print("평점: ",rate)
#         print("개봉: ",open)
#         print("누적관객: ",many)

# f.close()
# # 추천 점수 컬럼(관객수*평점)/100

df= pd.read_csv('daum_movie.csv',index_col='제목')
df['추천점수']=(df['누적관객']*df['평점'])/100
df.sort_values('추천점수',inplace=True,ascending=False)


print(df)