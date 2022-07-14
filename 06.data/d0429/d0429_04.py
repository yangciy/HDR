# 구글 무비 4,5번 제목 가격 출력
import pandas as pd

df=pd.read_csv('google_movie.csv')
df.to_excel('google_movie.xls')
df=pd.read_excel('google_movie.xls',index_col=0)
df.index.name='번호'
print(df)
print(df.loc[[3,4],['제목','가격']])
# print(df.loc[[2,3]])
# print(df.index)