import pandas as pd


data1= pd.read_csv('2020 연봉.csv')
data2= pd.read_csv('2021 연봉.csv')
data3= pd.read_csv('2022 연봉.csv')

# 컬럼 하다ㄴ부분으로 병합
df=pd.concat([data1,data2,data3])
# print(df.head(101))
df.to_csv('전체연봉.csv',encoding='utf-8-sig',index=False)
df=pd.read_csv('전체연봉.csv')
print(df)
print(df.sort_values('WAR',ascending=False))
# print(data2)
# print(data3)