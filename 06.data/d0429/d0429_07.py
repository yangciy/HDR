import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)
#
# print(df.iloc[[0,3],[0,2]])


print(df.loc[(df['키']>188),'학교'])


# filt = df['키']>188
# print(df[~filt])
# print(df[~(df['키']>188)])
# print(df.loc[(df['키']>188),['이름','국어','영어']])

print(df.loc[(df['키']<170)|(df['키']>200),['이름','학교','키']])