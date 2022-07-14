import pandas as pd
import numpy as np
df= pd.read_excel('score.xlsx',index_col='지원번호')

# df.dropna(axis='index',inplace=True)
# df.dropna(axis='columns',inplace=True)

df['학교']=np.nan
# how='any' nana 이 한개라도 있으면 삭제 'all' 모두 nan일 경우
# df.dropna(axis='columns',how='any',inplace=True)

df.dropna(axis='columns',how='all',inplace=True)
print(df)