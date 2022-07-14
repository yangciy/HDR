from random import triangular
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit, softmax                      # 시그모이드함수
import matplotlib.pyplot as plt

df_fish = pd.read_csv('10.mlearn/m0704/fish.csv')

x= df_fish.drop(columns='Species').to_numpy()
y= df_fish['Species'].to_numpy()

train_x,test_x,train_y,test_y= train_test_split(x,y,random_state=42)

ss=StandardScaler()
ss.fit(train_x)
train_s=ss.transform(train_x)
test_s=ss.transform(test_x)


# c_lists=[0.001,0.01,0.1,1,10,100]
# train_score=[]
# test_score=[]
# for c_list in c_lists:
#     lr=LogisticRegression(C=c_list)
#     lr.fit(train_s,train_y)
#     train_score.append(lr.score(train_s,train_y))
#     test_score.append(lr.score(test_s,test_y))



# plt.plot(np.log10(c_lists),train_score)
# plt.plot(np.log10(c_lists),test_score)
# plt.show()
lr=LogisticRegression(C=10)
lr.fit(train_s,train_y)
proba=lr.predict_proba(test_s[:5])
print(proba)

s1=lr.score(train_s,train_y)
s2=lr.score(test_s,test_y)
print(s1)
print(s2)



decisions = lr.decision_function(test_s[:5])
print(decisions)

# 시그모이드함수 적용
print(np.round(softmax(decisions),decimals=3))