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

