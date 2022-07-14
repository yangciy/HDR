from sklearn import svm
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

sns.set(style="ticks",color_codes=True)
iris = sns.load_dataset("iris")

data=iris[['sepal_length','sepal_width','petal_length','petal_width']]
label=iris['species']

train_x,test_x,train_y,test_y=train_test_split(data,label,test_size=0.2)


clf_svm=svm.SVC()
clf_svm.fit(train_x,train_y)
a=float(input('숫자를 입력해라.'))
b=float(input('숫자를 입력해라.'))
c=float(input('숫자를 입력해라.'))
d=float(input('숫자를 입력해라.'))
# b=[]
# for i in range(4):
#     a=int(input('숫자를 입력해라.: '))
#     b.append(a)
# c=pd.DataFrame(b)

# print(c)
result_svm=clf_svm.predict([[a,b,c,d]])
print('svm 예측',result_svm)
score_svm=clf_svm.score(test_x,test_y)
print('svm 정확도',score_svm)

# clf_rf=RandomForestClassifier()
# clf_rf.fit(train_x,train_y)
# result=clf_rf.predict(test_x)
# score=clf_rf.score(test_x,test_y)
# # print('rf 예측',result)
# print('rf 정확도',score)