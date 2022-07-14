import pandas as pd

df=pd.read_excel('user.xlsx')
# print(df)
# print(df.info())
# print(df.head(10))
# print(df.tail(20))
# print(df.values)
print(df.values[2:4])
# print(df.iloc[0])
# print(df[['first_name','gender']])
# print(df.index)
# print(df.columns)
# print(df.shape)
# describe 숫자컬럼 통계  ( 최대값 평균 숫자 분포도 )
# print(df.describe())
# info 컬럼의 타입
# print(df.info())

# df=pd.read_excel('user.xlsx',skiprows=[i for i in range(0,500)],nrows=10)
# print(df)