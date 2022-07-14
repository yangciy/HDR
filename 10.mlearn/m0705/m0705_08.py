import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.special import softmax
df=pd.read_csv('iris(150).csv')
# print(df.columns)
x=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y=df['Species']

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.fit_transform(test_x)

sc=SGDClassifier(random_state=42,loss='log',max_iter=200,tol=None)
sc.fit(train_x,train_y)
# sc.partial_fit(train_x,train_y)
score1 = sc.score(train_x,train_y)
score2 = sc.score(test_x,test_y)
print('train: ',score1)
print('test: ',score2)