import pandas as pd
import numpy as np

df= pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)

# 결측치 : Nan데이터처리
# print(df.fillna('',inplace=True))
# filt=df['SW특기'].str.contains('python',case=False)
# print(df[filt])
df.dropna(inplace=True)    # 해당되는 행 삭제
# df['학교'] =np.nan
# df['수학'] =np.nan
# # df['학교'].fillna("없음",inplace=True)
# df['수학'].fillna(0,inplace=True)
print(df)