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

train['IsHoliday']=train['IsHoliday'].apply(Holi)
train['Month']=train['Date'].apply(Month)
train['Year']=train['Date'].apply(Year)
test['IsHoliday']=test['IsHoliday'].apply(Holi)
test['Month']=test['Date'].apply(Month)
test['Year']=test['Date'].apply(Year)
train=train.drop(columns=['Date','id','Temperature', 'Fuel_Price'])
test=test.drop(columns=['Date','id','Temperature', 'Fuel_Price'])

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
# print(prediction)

temp = pd.read_csv('sample_submission.csv')
temp['Weekly_Sales'] = prediction['Label']

submission = pd.DataFrame({
        "id" : temp['id'],
        "Weekly_Sales" : temp['Weekly_Sales']
})
temp.to_csv('submit13.csv', index = False)


# LGBMRegressor(bagging_fraction=0.8, bagging_freq=3, boosting_type='gbdt',
#               class_weight=None, colsample_bytree=1.0, feature_fraction=0.8,
#               importance_type='split', learning_rate=0.2, max_depth=-1,
#               min_child_samples=6, min_child_weight=0.001, min_split_gain=0.6,
#               n_estimators=100, n_jobs=-1, num_leaves=30, objective=None,
#               random_state=42, reg_alpha=0.001, reg_lambda=5, silent=True,
#               subsample=1.0, subsample_for_bin=200000, subsample_freq=0)
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
