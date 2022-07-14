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
params={
    'max_depth':[1,5,10,50,100],
    'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005],
    'min_samples_split':[1,10,50,100],
}
dt_model=GridSearchCV(dt,params,scoring='accuracy',n_jobs=-1,cv=5)
dt_model.fit(train_x,train_y)
dt_a=dt_model.best_estimator_
print(dt_a.score(train_x,train_y))
print(dt_model.best_params_)
print(dt_model.best_score_)
# print(dt_model.score(train_x,train_y))
# print(dt_model.score(test_x,test_y))

# plt.figure(figsize=(10,7))
# plot_tree(dt,filled=True,feature_names=['alcohol','sugar','pH'])
# plt.show()