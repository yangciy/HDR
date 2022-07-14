from operator import index
import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df.columns)
# print(df.index)

# df.columns=['name','school','height','kor']
df.rename(columns={'이름':'name'},inplace=True)
df.rename(columns={'이름':'name','학교':'school'},inplace=True)
print(df)