from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, cross_validate, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

wine = pd.read_csv('10.mlearn/m0706/wine.csv')


x=wine.drop(columns='class')
y=wine['class']

train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

rf= RandomForestClassifier(random_state=42,n_jobs=-1)
scores= cross_validate(rf,train_x,train_y,n_jobs=-1,return_train_score=True)
print(np.mean(scores['train_score']))
print(np.mean(scores['test_score']))
rf.fit(train_x,train_y)
print(rf.feature_importances_)
print(rf.score(train_x,train_y))
print(rf.score(test_x,test_y))