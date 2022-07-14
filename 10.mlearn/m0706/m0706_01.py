from sklearn.linear_model import SGDClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

fish = pd.read_csv('10.mlearn/m0704/fish.csv')

x=fish.drop(columns='Species').to_numpy()
y=fish['Species'].to_numpy()

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)
ss=StandardScaler()
train_s=ss.fit_transform(train_x)
test_s=ss.fit_transform(test_x)

sc= SGDClassifier(loss='log', max_iter=300, random_state=42)

train_score=[]
test_score=[]
classes= np.unique(train_x)
for _ in range(300):
    sc.partial_fit(train_s,train_y,classes=classes)
    train_score.append(sc.score(train_s,train_y))
    test_score.append(sc.score(test_s,test_y))
    
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('Accuracy')
plt.show()