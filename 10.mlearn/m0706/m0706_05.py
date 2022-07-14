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

dt=DecisionTreeClassifier(random_state=42)
params={'max_depth':range(5,20,1),
        'min_impurity_decrease':np.arange(0.0001,0.001,0.0001),
        'min_samples_split':range(2,100,10)}

gs=GridSearchCV(dt,params,cv=5,n_jobs=-1)
gs.fit(train_x,train_y)
dt_b=gs.best_estimator_
score1=dt_b.score(train_x,train_y)
score2=dt_b.score(test_x,test_y)
print('스코어: ', score1)
print('스코어: ', score2)
print(gs.best_params_)
print(gs.best_score_)
