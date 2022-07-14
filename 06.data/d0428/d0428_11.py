import pandas as pd

df=pd.read_excel('score.xlsx',index_col="지원번호")

print(df[['학교','국어']])
print(df[df.columns[[1,3,-2]]][0:5])
print(df[:1])
print(df[1:])
# print(df['이름'])
# print(df[df.columns[1]])
