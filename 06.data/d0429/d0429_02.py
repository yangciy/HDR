import pandas as pd
import re
df=pd.read_excel('출생아.xls',skiprows=2,nrows=2,index_col=0)
df.index.name='목록'
# print(df)
print(df.index.values)
# print(df.inㄴdex[0])
print(df.loc['출생아\xa0수'])
df.rename(index={df.index[0]:'출생아 수'},inplace=True)
df.rename(index={df.index[1]:re.sub(r'[^ㄱ-힣]', ' ',df.index[1])},inplace=True)

print(df.index.values)