import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
print(df.describe())
print("키 최소값 : ",df['키'].min())
print("키 최대값 : ",df['키'].max())
print("키 평균값 : ",df['키'].mean())
print("키 개수 : ",df['키'].count())
print("키 합개 : ",df['키'].sum())
print(df['키'].nlargest(3))
print(df['키'].nsmallest(3))

print(df)
print('학교 : ',df['학교'])
print('학교 : ',df['학교'].nunique())
print('학교 : ',df['학교'].unique())

# df= pd.read_excel('출생아.xls',skiprows=2,nrows=2)

# print(df[df.columns[-1]])


# print(df.columns)

# print('end= '+df.columns[-1])
# print(df.columns[5])
# print(df.columns[0])
# print(df[['과학','사회','SW특기']])


# df=pd.read_excel('score.xlsx')
# df.set_index('이름',inplace=True)
# print(df)
# print(df.iloc[1])
# print(df.loc['강나래'])
# print(df.loc[df.index[0]])