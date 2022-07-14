import pandas as pd


df= pd.read_excel('score.xlsx',index_col='지원번호')
print(df)
# 키를 기준으로 순차정렬
# print(df.sort_values('키'))
# print(df.sort_values('키',ascending=False))



# print(df.sort_values(['수학','영어']))
print(df.sort_values(['수학','영어'],ascending=False))
print(df.sort_values(['수학','영어'],ascending=[False,True]))