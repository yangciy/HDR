from sklearn import svm
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# def nameChange(species):
#     if species == 'setosa':
#         return 0
#     elif species == 'versicolor':
#         return 1
#     else:
#         return 2


sns.set(style="ticks",color_codes=True)
iris = sns.load_dataset("iris")
# iris.info()

# df=pd.read_csv('iris(150).csv')
# print(iris)


data=iris[['sepal_length','sepal_width','petal_length','petal_width']]
# iris['species']=iris['species'].apply(nameChange)
label=iris['species']

train_x,test_x,train_y,test_y=train_test_split(data,label,test_size=0.2)
# print(train_x)
# print(train_y)

clf_svm=svm.SVC()
clf_svm.fit(train_x,train_y)
result_svm=clf_svm.predict([[5.7,2.7,3.6,1]])
print('svm 예측',result_svm)
score_svm=clf_svm.score(test_x,test_y)
print('svm 정확도',score_svm)

clf_rf=RandomForestClassifier()
clf_rf.fit(train_x,train_y)
result=clf_rf.predict(test_x)
score=clf_rf.score(test_x,test_y)
# print('rf 예측',result)
print('rf 정확도',score)