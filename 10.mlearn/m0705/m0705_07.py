import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.special import softmax


fish = pd.read_csv('10.mlearn/m0704/fish.csv')

x=fish.drop(columns='Species').to_numpy()
y=fish['Species'].to_numpy()

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

ss=StandardScaler()
train_s=ss.fit_transform(train_x)
test_s=ss.fit_transform(test_x)

sc=SGDClassifier(loss='log',max_iter=130,tol=None,random_state=42)


sc.fit(train_s,train_y)
sc.partial_fit(train_s,train_y)
score1 = sc.score(train_s,train_y)
score2 = sc.score(test_s,test_y)
print('train: ',score1)
print('test: ',score2)