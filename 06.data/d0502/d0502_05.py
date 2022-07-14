import pandas as pd
df=pd.read_excel('score.xlsx',index_col='지원번호')
# 컬럼 삭제
# df.drop(columns=['국어','영어','수학'],inplace=True)

#인덱스 삭제 row삭제 
# df.drop(index='3번',inplace=True)
# df.drop(index=['1번','3번','5번'],inplace=True)

# print(df)
filt= df['수학']>=80
print(df[filt].index)
df.drop(index=['1번','2번'],inplace=True)
df.drop(index=df[filt].index,inplace=True)

print(df)
