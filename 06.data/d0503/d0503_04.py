import pandas as pd

df= pd.read_excel('score.xlsx',index_col='지원번호')

# print(df)
# 학교로 그룹
print(df.groupby('학교').get_group('구로고'))
# 학교로 묶어서 평균
print(df.groupby('학교').mean())

# 학교별 인원
print(df.groupby('학교').size()['구로고'])

# 학교 키 평균
print(df.groupby('학교')['키'].mean())

print(df.groupby('학교')[['키','국어','영어']].mean())