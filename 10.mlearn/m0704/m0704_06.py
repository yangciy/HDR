import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

fish= pd.read_csv('10.mlearn/m0704/fish.csv')

x=fish.drop(columns='Species').to_numpy()   #5 * 159
y=fish['Species'].to_numpy()                #7

# 105,15.2,19.5,5.09,3.42
train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)


# poly=PolynomialFeatures(include_bias=False,degree=2)
# poly.fit(train_x)
# train_p=poly.transform(train_x)
# test_p=poly.transform(test_x)
# new=poly.transform([[105,15.2,19.5,5.09,3.42]])
ss=StandardScaler()
ss.fit(train_x)
train_s=ss.transform(train_x)
test_s=ss.transform(test_x)
# new_s=ss.transform(new)

bream_smelt_index= (train_y=='Bream') | (train_y=='Smelt')
train_bs=train_s[bream_smelt_index]
train_y=train_y[bream_smelt_index]
bream_smelt_index= (test_y=='Bream') | (test_y=='Smelt')
test_bs=test_s[bream_smelt_index]
test_y=test_y[bream_smelt_index]
# print(train_bs)
# print(test_bs)
# print(train_y.shape)
# print(test_y.shape)
# print(bream_smelt_index)

clf=LogisticRegression()
clf.fit(train_bs,train_y)


# proba=clf.predict_proba(new_s)
# print(np.round(proba,decimals=2))
pred=clf.predict([[105,15.2,19.5,5.09,3.42]])
# pred=clf.predict(new_s)
print(pred)
score1=clf.score(train_bs,train_y)
score=clf.score(test_bs,test_y)
print(score1)
print(score)




