import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df)
print(df.iloc[0:5])
print(df.iloc[3:7,2])

print(df.iloc[4,:3])
print(df.iloc[0,4])

print(df.iloc[3:5,3:7])