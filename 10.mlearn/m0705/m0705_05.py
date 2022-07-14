import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.special import softmax
df=pd.read_csv('iris(150).csv')
print(df.columns)
x=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y=df['Species']

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.fit_transform(test_x)


train_score=[]
test_score=[]
c_list=[1,2,3,4,5,6,7,8,9,10]

# for c in c_list:
#     lr=LogisticRegression(C=c)
#     lr.fit(train_x,train_y)
#     train_score.append(lr.score(train_x,train_y))
#     test_score.append(lr.score(test_x,test_y))


# plt.plot(np.log10(c_list),train_score)
# plt.plot(np.log10(c_list),test_score)
# plt.show()

lr=LogisticRegression(C=6)
lr.fit(train_x,train_y)

pred=lr.predict([[5.1,3.8,1.8,0.5]])
# print(pred)
score=lr.score(train_x,train_y)
score1=lr.score(test_x,test_y)
print('꽃: ',pred)
print('테스트: ',score1)
print('훈련: ',score)

decisions = lr.decision_function(test_x[:5])
# print(decisions)

# 시그모이드함수 적용
# print(np.round(softmax(decisions),decimals=3))
