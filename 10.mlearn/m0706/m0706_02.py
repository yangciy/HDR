from pytest import param
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

wine = pd.read_csv('10.mlearn/m0706/wine.csv')


x=wine.drop(columns='class')
y=wine['class']

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

ss=StandardScaler()
ss.fit(train_x,train_y)
train_s=ss.transform(train_x)
test_s=ss.transform(test_x)

# sc=SGDClassifier(loss='log')
# sc.fit(train_s,train_y)
# print(sc.score(train_s,train_y))
# print(sc.score(test_s,test_y))

# lr=LogisticRegression(C=10)
# lr.fit(train_s,train_y)
# print(lr.score(train_s,train_y))
# print(lr.score(test_s,test_y))

dt=DecisionTreeClassifier(random_state=42)
param_gird={
    'max_depth':[5,10,50,100]
}
dt_model=GridSearchCV(dt,scoring='accuracy',n_jobs=-1,cv=5,param_grid=param_gird)

dt.fit(train_x,train_y)
dt_model.fit(train_x,train_y)
print(dt_model.best_params_)
print(dt_model.best_score_)
print(dt.feature_importances_)
print(x.columns)
# print(dt_model.score(train_x,train_y))
# print(dt_model.score(test_x,test_y))

# plt.figure(figsize=(10,7))
# plot_tree(dt,filled=True,feature_names=['alcohol','sugar','pH'])
# plt.show()