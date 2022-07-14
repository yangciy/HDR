import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
train_csv=pd.read_csv("./mnist/train.csv",header=None)
test_csv=pd.read_csv("./mnist/test.csv",header=None)


def func(x):
    output=[]
    for i in x:
        output.append(float(i)/256)
    return output

train_x=list(map(func,train_csv.iloc[:,1:].values))
# print(train_x)
test_x=list(map(func,test_csv.iloc[:,1:].values))
# print(test_x)
train_y=train_csv[0].values
test_y=test_csv[0].values
# print(len(train_y))
# clf=RandomForestClassifier()
# clf=KNeighborsClassifier()
clf=svm.SVC()
clf.fit(train_x,train_y)
pred=clf.predict(test_x)
print('결과값: ',pred)

score1=clf.score(train_x,train_y)
score2=clf.score(test_x,test_y)
print('svm score1 :',score1)
print('svm score2 :',score2)


clf=RandomForestClassifier()
clf.fit(train_x,train_y)
pred=clf.predict(test_x)
print('결과값: ',pred)

score1=clf.score(train_x,train_y)
score2=clf.score(test_x,test_y)
print('rf score1 :',score1)
print('rf score2 :',score2)


clf=KNeighborsClassifier()

clf.fit(train_x,train_y)
pred=clf.predict(test_x)
print('결과값: ',pred)

score1=clf.score(train_x,train_y)
score2=clf.score(test_x,test_y)
print('knn score1 :',score1)
print('knn score2 :',score2)
