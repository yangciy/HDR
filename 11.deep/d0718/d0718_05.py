from konlpy.tag import Okt
import pandas as pd
from gensim.models import word2vec
from bs4 import BeautifulSoup
import codecs

okt=Okt()
word_dic={}

fp= codecs.open('/Users/uk/Desktop/HDR/BEXX0003.txt',encoding='utf-16')
soup = BeautifulSoup(fp,'html.parser')
body=soup.select_one("body > text")
text=body.get_text()
lines=text.split("\n")

# print(type(lines))
for line in lines:
    malist = okt.nouns(line)
    for taeso in malist:
        if len(taeso)>=2:
            if not (taeso in word_dic):
                word_dic[taeso]=0
            word_dic[taeso] += 1
keys = sorted(word_dic.keys(),reverse=True) # 50개 데이터 정렧
# for word,count in keys[:50]:
#     print(f"{word}:{count}",end="") 
print(keys)
model= word2vec.Word2Vec(sentences=keys,vector_size=100,window=5,min_count=5,workers=4,sg=0)
print(model.wv.most_similar(positive=['김서방']))
