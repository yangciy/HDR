import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import matplotlib.pyplot as plt

df=pd.read_csv('10.mlearn/m0630/perch_full2.csv')


x=df.drop(columns=['weight'])
y=df['weight']
# print(y)

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

poly=PolynomialFeatures(degree=5,include_bias=False)
poly.fit(train_x)
train_p=poly.transform(train_x)
test_p=poly.transform(test_x)
new_p=poly.transform([[30.4,8.89,4.22]])
ss=StandardScaler()
ss.fit(train_p)
train_s=ss.transform(train_p)
test_s=ss.transform(test_p)
new_s=ss.transform(new_p)


lr=LinearRegression()
train_score=[]
test_score=[]
alpha_list=[0.01,0.1,1,10,100]
for alpha in alpha_list:
    ridge=Lasso(alpha=alpha)
    ridge.fit(train_s,train_y)
    train_score.append(ridge.score(train_s,train_y))
    test_score.append(ridge.score(test_s,test_y))

plt.plot(np.log10(alpha_list),train_score)
plt.plot(np.log10(alpha_list),test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()


ridge=Ridge(alpha=0.1)
ridge.fit(train_s,train_y)
pred=ridge.predict(test_s)
result=ridge.predict(new_s)
score1=ridge.score(train_s,train_y)
score2=ridge.score(test_s,test_y)
mae=mean_absolute_error(test_y,pred)

print('예측값: ',result)
print('정확도: ',score1)
print('정확도: ',score2)
print('오차범위: ',mae)