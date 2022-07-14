import pandas as pd

df= pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)
# print(df['국어'][0])
# print(df.loc[['1번','2번']])
# print(df.loc['1번','국어'])
# print(df.loc[['1번','2번'],'국어'])
# print(df.loc[['1번','3번'],['국어','영어']])
print(df.loc['1번':'5번','국어':'사회'])