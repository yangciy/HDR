import pandas as pd

df=pd.read_csv('전체연봉.csv')

# print(df)
# NoN 
# filt = df['WAR'].isnull()
# # 방법 1
# df.loc[filt,'WAR']=0
# # 방법 2
# df['WAR'].fillna(0,inplace=True)
# print(df)
# 검색
# filt2= (df['선수']=='애플러') & (df['연도']==2022)
# print(df[filt2])

# print(df.groupby('선수').mean())

# print(df.sort_values('선수'))
print(df.groupby('연도')['연봉(만원)'].mean())
print(df.groupby('연도').count())