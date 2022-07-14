import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

df=pd.read_csv('iris(150).csv')
# print(df.columns)

x=df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
y=df['Species']


train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)

rf=RandomForestClassifier(random_state=42,n_jobs=-1,)
params={
    'n_estimators':[10,100],
    'max_depth':[5,3,1],
    'min_samples_leaf':[3,4,5]
}
gs=GridSearchCV(rf,params,n_jobs=-1,cv=5)
gs.fit(train_x,train_y)
gs=gs.best_estimator_
print(gs.score(train_x,train_y))
print(gs.score(test_x,test_y))
print(gs)
rf.fit(train_x,train_y)
print(rf.predict([[6.7,3.0,5.1,1.8]]))
print(rf.score(train_x,train_y))
print(rf.score(test_x,test_y))