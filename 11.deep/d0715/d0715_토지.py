from konlpy.tag import Okt
import pandas as pd
from bs4 import BeautifulSoup
import codecs
from konlpy.tag import Okt
okt=Okt()
word_dic={}

fp= codecs.open('/Users/uk/Desktop/HDR/BEXX0003.txt',encoding='utf-16')
# soup = BeautifulSoup(fp,'lxml')
soup = BeautifulSoup(fp,'html.parser')
# body = soup.find("body").get_text()
body=soup.select_one("body > text")
text=body.get_text()
lines=text.split("\r\n")
for line in lines:
    malist = okt.pos(line,norm=True,stem=True)
    for taeso,pumsa in malist:
        if len(taeso)>=2:
            if pumsa == 'Noun':
                if not (taeso in word_dic):
                    word_dic[taeso]=0
                word_dic[taeso] += 1
            
keys = sorted(word_dic.items(),key=lambda x:x[1],reverse=True) # 50개 데이터 정렧
for word,count in keys[:50]:
    print(f"{word}:{count}",end="") 
print()
# for i in word_dic:
#     if len(i)>1:
#         print(i)