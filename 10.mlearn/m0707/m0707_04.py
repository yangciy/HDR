import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

df=pd.read_csv('mushroom.csv')
# print(df.columns)

x=df.drop(columns='poisonous')
y=df['poisonous']

x_a=[]
for i in range(len(x)):
    row_data=[]
    for v in range(len(x.iloc[i])):
        row_data.append(ord(x.iloc[i,v]))
    x_a.append(row_data)
    
# print(x_a)

train_x,test_x,train_y,test_y=train_test_split(x_a,y,random_state=42)
rf=RandomForestClassifier(random_state=42,n_jobs=-1)
params={'n_estimators':[10,20,30,50,100],
        'min_samples_leaf':[2,4,8],
        'max_depth':[2,4,8],
        'max_features':[2,4,8],
        }
rf_gs=GridSearchCV(rf,params,cv=3,n_jobs=-1)
rf_gs.fit(train_x,train_y)
print(rf_gs.best_estimator_)
rf.fit(train_x,train_y)
a=rf.score(train_x,train_y)
b=rf.score(test_x,test_y)
print(rf.feature_importances_)
print('train: ',a)
print('test: ',b)