import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


df_fish = pd.read_csv('10.mlearn/m0704/fish.csv')

x= df_fish.drop(columns='Species').to_numpy()
y= df_fish['Species'].to_numpy()

train_x,test_x,train_y,test_y= train_test_split(x,y,random_state=42)

ss=StandardScaler()
ss.fit(train_x)
train_s=ss.transform(train_x)
test_s=ss.transform(test_x)

bream_smelt_index= (train_y=='Bream') | (train_y=='Smelt')
train_bs=train_s[bream_smelt_index]
train_y=train_y[bream_smelt_index]
bream_smelt_index= (test_y=='Bream') | (test_y=='Smelt')
test_bs=test_s[bream_smelt_index]
test_y=test_y[bream_smelt_index]


lr= LogisticRegression()
lr.fit(train_bs,train_y)
print(lr.coef_,lr.intercept_)
pred=lr.predict(test_bs[:5])
pred1=lr.predict_proba(test_bs[:5])
print(pred)
print(pred1)
score1= lr.score(train_bs,train_y)
score2= lr.score(test_bs,test_y)
print(score1)
print(score2)

desisions= lr.decision_function(test_bs[:5])
