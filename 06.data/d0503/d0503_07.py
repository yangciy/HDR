import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')

# print(df.columns)
# print(df.index)

df['학년'] =[3,3,2,1,1,3,2,2]
print(df.groupby(['학교','학년']).count())
# 학년 그룹화 - 평균의 역순정렬 s
print(df.groupby('학년').mean().sort_values('키',ascending=False))