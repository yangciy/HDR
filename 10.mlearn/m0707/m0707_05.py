
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from matplotlib import rc 
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor

rc('font', family='AppleGothic') 			## 이 두 줄을 
plt.rcParams['axes.unicode_minus']=False

# def tN(x):
#     if x=='SK':
#         return 1
#     elif x=='LG':
#         return 2
#     elif x=='KIA':
#         return 3
#     elif x=='롯데':
#         return 4
#     elif x=='KT':
#         return 5
#     elif x=='두산':
#         return 6
#     elif x=='삼성':
#         return 7
#     elif x=='한화':
#         return 8
#     else:
#         return 9
        


df=pd.read_csv('picher_stats_2017.csv')
# df['팀명']=df['팀명'].apply(tN)
one=pd.get_dummies(df['팀명'])
# print(df['팀명'])
print(df.columns)
df_1=df.join(one)
# print(df.columns)
# print(df.info())
# print(df)
x=df_1[['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
    '연봉(2017)', 'KIA', 'KT', 'LG', 'NC', 'SK', '두산', '롯데', '삼성',
       '한화']]
y=df['연봉(2018)']
# temaName=df['팀명'].unique()
# 'SK' 'LG' 'KIA' '롯데' 'KT' '두산' '삼성' '한화' 'NC'
# print(temaName)
# def plot_hist(df):
#     plt.rcParams['figure.figsize']=[20,16]
#     fig = plt.figure(1)
#     for i in range(len(df.columns)):
#         ax= fig.add_subplot(5,5,i+1)
#         plt.hist(df[df.columns[i]],bins=50)
#         ax.set_title(df.columns[i])
#     plt.show()
# df_c=df[['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
#        '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
#        '연봉(2018)', '연봉(2017)']]
# plot_hist(df_c)


def standard_scaling(df,scale_columns):
    for col in scale_columns:
        series_mean=df[col].mean()
        series_std = df[col].std()
        df[col]=df[col].apply(lambda x:(x-series_mean)/series_std)
    return df
scale_columns=['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
       '연봉(2018)', '연봉(2017)']

standard_scaling(df,scale_columns)

# 두개 이상 제거
# df.columns.difference(['',''])


# # # # print(x)
train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=42)
# # params={   
# #     'n_estimators':[500,600],
# #     'max_depth':[11,10,9],
# #     'max_samples':[54,56,52],




# # }
# # rf=RandomForestRegressor(random_state=42,n_jobs=-1)
# # gs=GridSearchCV(rf,params,n_jobs=-1,cv=5)
# # gs.fit(train_x,train_y)
# # print(gs.score(train_x,train_y))
# # print(gs.best_estimator_)
rf=RandomForestRegressor(max_depth=10, max_samples=54, n_estimators=500, n_jobs=-1,
                      random_state=42)
rf.fit(train_x,train_y)
print(rf.score(train_x,train_y))
print(rf.score(test_x,test_y))

# score=rf.predict(test_x)
# print(score[:5])
# print(test_y[:5])
# print(rf.feature_importances_)
ss=StandardScaler()
ss.fit(train_x,train_y)
train_s=ss.transform(train_x)
test_s=ss.transform(test_x)
# svm=SVC()
# svm.fit(train_s,train_y)
# print(svm.score(train_s,train_y))
# print(svm.score(test_s,test_y))

lr=LinearRegression()
lr.fit(train_s,train_y)

print(lr.score(train_s,train_y))
print(lr.score(test_s,test_y))
# score=lr.predict(test_x)
# print(score[:5])
# print(test_y[:5])

