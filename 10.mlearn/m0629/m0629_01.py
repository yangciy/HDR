import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

sns.set(style="ticks",color_codes=True)
iris = sns.load_dataset("iris")

print(iris)

data=iris[['sepal_length','sepal_width','petal_length','petal_width']]
label=iris[['species']]

train_x,test_x,train_y,test_y=train_test_split(data,label)
clf=KNeighborsClassifier()
clf.n_neighbors=3
clf.fit(train_x,train_y)
result=clf.predict(test_x)
score=clf.score(test_x,test_y)

print('결과',result)
print('정확도',score)

# a=float(input('숫자를 입력하샘'))
# b=float(input('숫자를 입력하샘'))
# c=float(input('숫자를 입력하샘'))
# d=float(input('숫자를 입력하샘'))
# result1=clf.predict([[a,b,c,d]])
# print('예측결과는 ',result1)