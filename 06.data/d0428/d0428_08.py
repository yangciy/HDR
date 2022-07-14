import pandas as pd
df= pd.read_excel('출생아.xls',skiprows=[0,1,3,5],nrows=2,index_col=0)

print(df)
# print(df.index)
# print(df['2020'])
# print(df.loc['출생아 수'])

# nrow= 1번째줄은 컬럼으로 인식하여 제외하고 숫자만큼 가져옴
# df =pd.read_csv('score.txt',sep=",",index_col='지원번호')
# print(df)
# print(df.index)
# df=pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)