import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

fish= pd.read_csv('10.mlearn/m0704/fish.csv')

x=fish.drop(columns='Species').to_numpy()   #5 * 159
y=fish['Species'].to_numpy()                #7

# 105,15.2,19.5,5.09,3.42
train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)


poly=PolynomialFeatures(include_bias=False,degree=2)
poly.fit(train_x)
train_p=poly.transform(train_x)
test_p=poly.transform(test_x)
new=poly.transform([[105,15.2,19.5,5.09,3.42]])
ss=StandardScaler()
ss.fit(train_p)
train_s=ss.transform(train_p)
test_s=ss.transform(test_p)
new_s=ss.transform(new)
clf=KNeighborsClassifier()
clf.fit(train_s,train_y)


proba=clf.predict_proba(new_s)
print(np.round(proba,decimals=2))
# pred=clf.predict([[105,15.2,19.5,5.09,3.42]])
pred=clf.predict(new_s)
print(pred)
score1=clf.score(train_s,train_y)
score=clf.score(test_s,test_y)
print(score1)
print(score)




