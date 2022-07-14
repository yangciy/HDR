import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit                      # 시그모이드함수
import matplotlib.pyplot as plt

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
length=bream_length+smelt_length
weight=bream_weight+smelt_weight

data= np.column_stack((length,weight))
label=['도미']*35+['빙어']*14
was=[[25,150]]
was1=[[30,600]]
train_x,test_x,train_y,test_y=train_test_split(data,label)

ss=StandardScaler()
ss.fit(train_x)
train_s=ss.transform(train_x)
test_s=ss.transform(test_x)
was=ss.transform(was)
was1=ss.transform(was1)
lr=LogisticRegression()
lr.fit(train_s,train_y)

pred=lr.predict(was)
pred1=lr.predict(was1)
print('25,150 정답은: ',pred)
print('30,600 정답은: ',pred1)
# score1=lr.predict_proba(was)
score2=lr.score(train_s,train_y)
score3=lr.score(test_s,test_y)
# print(score1)
print(score2)
print(score3)

train_s=train_s.reshape(-1,1)
print(train_s)

plt.scatter(length,weight)
# plt.scatter(length,weight)
plt.scatter(25,150,marker='*')
plt.scatter(30,600,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()



decisions = lr.decision_function(test_s[:5])
print(decisions)

# 시그모이드함수 적용
print(expit(decisions))