from konlpy.tag import Okt
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
import urllib.request
from gensim.models import *

urllib.request.urlretrieve('https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt',filename='ratings.txt')
train_data=pd.read_table('ratings.txt')

# 정보 확인
# print(train_data.describe())
# print(train_data.info())

# None값 제거
train_data= train_data.dropna(how='any')

# 한글만 남기고 제외
train_data['document']= train_data['document'].str.replace('[^ㄱ-하-ㅣ가-힣]',"",regex=True)

# print(train_data.head(10))

# 형태소 분석
okt=Okt()
# word2vec 형태소 분석 -> 글자간의 벡터화를 해서 글자간의 관계를 형성
# [[]] 리스트 안에 

# 불용어 정의
stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
token_data=[]
# 199992개를 가져와서 형태소 분석
for sent in train_data['document']:
    temp_x=okt.morphs(sent,stem=True)
    temp_x=[word for word in temp_x if not word in stopwords]
    token_data.append(temp_x)

    
# word2vec
model= word2vec(sentences=token_data,vector_size=100,window=5,min_count=5,workers=4,sg=0)
# model.save('model_w2v.h5')
# model=word2vec.Word2Vec.load('model_w2v.h5')

print(model.wv.most_similar('때'))