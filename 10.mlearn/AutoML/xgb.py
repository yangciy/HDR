import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import f1_score, r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error
from sklearn.metrics import classification_report
import sklearn.gaussian_process as gsp
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings(action='ignore')

def Holi(isHoliday):
    if isHoliday == True:
      return 1
    else:
      return 0
  
def Month(date):
  month = date[3:5]
  month = int(month)
  return month

def Year(date):
  year = date[7:]
  year = int(year)
  return year

train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')

train=train.fillna(0)
test=test.fillna(0)
  
train['IsHoliday']=train['IsHoliday'].apply(Holi)
train['Month']=train['Date'].apply(Month)
train['Year']=train['Date'].apply(Year)
test['IsHoliday']=test['IsHoliday'].apply(Holi)
test['Month']=test['Date'].apply(Month)
test['Year']=test['Date'].apply(Year)
train=train.drop(columns=['Date','id','Temperature', 'Fuel_Price','Promotion1'])
test=test.drop(columns=['Date','id','Temperature', 'Fuel_Price','Promotion1'])
train_x = train.drop(columns=['Weekly_Sales'])
train_y = train[['Weekly_Sales']]
# ss=StandardScaler()
# train_x=ss.fit_transform(train_x)
# test=ss.fit_transform(test)
xgb=XGBRegressor( n_jobs=-1,
             objective='reg:squarederror',
             random_state=42,n_estimators=170,learning_rate=0.3,
             scale_pos_weight=33.0, verbosity=0)
print('돌아가는중')
params = {
      "max_features": [10],
    'min_samples_split':  [5], "max_depth":[5],
    'num_parallel_tree':[6],
    "min_child_weight":[4],
    'colsample_bytree':[0.6]}
X_train,X_val,y_train,y_val=train_test_split(train_x,train_y,random_state=42)

gs_xgb=GridSearchCV(xgb,params,cv=15,n_jobs=-1,scoring='neg_mean_squared_error',verbose=2)

gs_xgb.fit(X_train,y_train)
print('베스트 파라미터: ',gs_xgb.best_params_)
print("train rmse: ",np.sqrt(-gs_xgb.best_score_))
xgb_model=gs_xgb.best_estimator_
xgb_pred1=xgb_model.predict(test)
xgb_pred2=xgb_model.predict(X_train)
print('val rmse',mean_squared_error(y_train,xgb_pred2,squared=False))
print(xgb_model.feature_importances_)

submission = pd.read_csv('sample_submission.csv')
submission['Weekly_Sales'] =xgb_pred1
submission.to_csv('submit11111.csv', index = False)
# rmse:  116732.32898109956
# rmse:  106959.78558376589
# 온도, 연료

# train rmse:  112864.26781795392
# k-20
# train rmse:  112506.8403805893
# val rmse 116042.11721024137
# k-15
# train rmse:  109447.5383956876
# val rmse 113641.77441611075
# k-10
# train rmse:  113190.6021139052
# val rmse 116042.11721024137
# k-5
# train rmse:  114574.93501566633
# val rmse 116042.11721024137

# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#              colsample_bynode=1, colsample_bytree=0.7, enable_categorical=False,
#              gamma=0, gpu_id=-1, importance_type=None,
#              interaction_constraints='', learning_rate=0.4, max_delta_step=0,
#              max_depth=6, min_child_weight=1, missing=nan,
#              monotone_constraints='()', n_estimators=60, n_jobs=-1,
#              num_parallel_tree=1, objective='reg:squarederror',
#              predictor='auto', random_state=42, reg_alpha=0.001, reg_lambda=0.7,
#              scale_pos_weight=38.0, subsample=0.7, tree_method='auto',
#              validate_parameters=1, verbosity=0)