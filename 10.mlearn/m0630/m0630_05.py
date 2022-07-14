import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

# 농어의 무게를 예측하라

perch_length = np.array( [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5, 44.0] )
perch_weight = np.array( [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0] )

# a=perch_length.tolist()
# print(a)

train_x,test_x,train_y,test_y=train_test_split(perch_length,perch_weight,random_state=42)

train_x=train_x.reshape(-1,1)
test_x=test_x.reshape(-1,1)

knr= KNeighborsRegressor()
knr.fit(train_x,train_y)

pred=knr.predict([[50]])
print(pred)

x,y=knr.kneighbors([[50]])

plt.scatter(train_x,train_y)
plt.scatter(100,1010,marker='^')
plt.scatter(train_x[y],train_y[y],marker='d')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
# pred=knr.predict(test_x)
# print(pred)
# mae=mean_absolute_error(test_y,pred)
# print(mae)
# score=knr.score(test_x,test_y)
# print("test: ",score)
# score1=knr.score(train_x,train_y)
# print("train: ",score1)
