from lightgbm import LGBMRegressor
import pandas as pd
import numpy as np
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
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# 학습용 데이터를 이용해 scaler를 학습시킵니다.
scaler.fit(train[['Promotion1','Promotion2','Promotion3','Promotion4','Promotion5']])

# 학습된 scaler를 사용해 데이터를 변환합니다.
scaled = scaler.transform(train[['Promotion1','Promotion2','Promotion3','Promotion4','Promotion5']])

# 변환된 값을 새로운 column에 할당합니다.
train[['Scaled_Promotion1','Scaled_Promotion2',
       'Scaled_Promotion3','Scaled_Promotion4',
       'Scaled_Promotion5']] = scaled
train = train.drop(columns=['Promotion1','Promotion2','Promotion3','Promotion4','Promotion5'])


scaled = scaler.transform(test[['Promotion1','Promotion2','Promotion3','Promotion4','Promotion5']])

test[['Scaled_Promotion1','Scaled_Promotion2',
       'Scaled_Promotion3','Scaled_Promotion4',
       'Scaled_Promotion5']] = scaled

test = test.drop(columns=['Promotion1','Promotion2','Promotion3','Promotion4','Promotion5'])
train['IsHoliday']=train['IsHoliday'].apply(Holi)
train['Month']=train['Date'].apply(Month)
train['Year']=train['Date'].apply(Year)
test['IsHoliday']=test['IsHoliday'].apply(Holi)
test['Month']=test['Date'].apply(Month)
test['Year']=test['Date'].apply(Year)
train=train.drop(columns=['Date','id','Temperature', 'Fuel_Price'])
test=test.drop(columns=['Date','id','Temperature', 'Fuel_Price'])
train_x = train.drop(columns=['Weekly_Sales'])
train_y = train[['Weekly_Sales']]
  
from pycaret.regression import *

test_1  = setup(train, target = 'Weekly_Sales',
              fold_shuffle=True,
              fold=15, 
              session_id=42,
              remove_multicollinearity = True,
              normalize= True,
              n_jobs = -1)



model = compare_models(sort='RMSE')
best_m=tune_model(model)
prediction = predict_model(best_m, data=test)
print(best_m)
# 여기서 추출된 모델 세부 파라미터 조정
# XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
#              colsample_bynode=1, colsample_bytree=0.7, enable_categorical=False,
#              gamma=0, gpu_id=-1, importance_type=None,
#              interaction_constraints='', learning_rate=0.3, max_delta_step=0,
#              max_depth=8, min_child_weight=2, missing=nan,
#              monotone_constraints='()', n_estimators=170, n_jobs=-1,
#              num_parallel_tree=1, objective='reg:squarederror',
#              predictor='auto', random_state=42, reg_alpha=10, reg_lambda=0.15,
#              scale_pos_weight=33.0, subsample=0.9, tree_method='auto',
#              validate_parameters=1, verbosity=0)
xgb=XGBRegressor( n_jobs=-1,
             objective='reg:squarederror',
             random_state=42,n_estimators=170,learning_rate=0.3,
             scale_pos_weight=33.0, verbosity=0)
X_train,X_val,y_train,y_val=train_test_split(train_x,train_y,random_state=42)

print('돌아가는중')
params = {
      "max_features": [10],
    'min_samples_split':  [5], "max_depth":[5],
    'num_parallel_tree':[6],
    "min_child_weight":[4],
    'colsample_bytree':[0.6]}
gs_xgb=GridSearchCV(xgb,params,cv=15,n_jobs=-1,scoring='neg_mean_squared_error',verbose=2)

gs_xgb.fit(X_train,y_train)
print('베스트 파라미터: ',gs_xgb.best_params_)
print("train rmse: ",np.sqrt(-gs_xgb.best_score_))
xgb_model=gs_xgb.best_estimator_
xgb_pred1=xgb_model.predict(test)
xgb_pred2=xgb_model.predict(X_train)
print('val rmse',mean_squared_error(y_train,xgb_pred2,squared=False))
print(xgb_model.feature_importances_)
