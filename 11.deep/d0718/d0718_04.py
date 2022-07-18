from konlpy.tag import Okt
import pandas as pd
from gensim.models import word2vec

f=open('/Users/uk/Desktop/HDR/book.txt',encoding='utf-8')
book=f.read()

results=[]
# 199992개를 가져와서 형태소 분석
lines= book.split('\n')
# 한글만 남기고 제외

# print(train_data.head(10))

# 형태소 분석
okt=Okt()
token_data=[]
# word2vec 형태소 분석 -> 글자간의 벡터화를 해서 글자간의 관계를 형성
# [[]] 리스트 안에 

# 불용어 정의
stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

for sent in lines:
    temp_x=okt.morphs(sent,stem=True)
    temp_x=[word for word in temp_x if not word in stopwords]
    token_data.append(temp_x)
print(type(token_data))


# model= word2vec.Word2Vec(sentences=token_data,vector_size=100,window=5,min_count=5,workers=4,sg=0)
# print(model.wv.most_similar(positive=['여자','결혼'],negative=['남자']))
