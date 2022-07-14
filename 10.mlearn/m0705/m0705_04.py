import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler         



df=pd.read_csv('iris(150).csv')
print(df.columns)
x=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y=df['Species']

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.fit_transform(test_x)

clf=KNeighborsClassifier()

clf.fit(train_x,train_y)
distances, indexes = clf.kneighbors([[5.1,3.8,1.8,0.5]])

pred=clf.predict([[5.1,3.8,1.8,0.5]])


score=clf.score(train_x,train_y)
score1=clf.score(test_x,test_y)
print('꽃: ',pred)
print('테스트: ',score1)
print('훈련: ',score)

# plt.scatter(train_x,train_x)
# plt.scatter(train_x[indexes,0],train_x[indexes,1],marker='D')
# plt.show()