import pandas as pd

df=pd.read_excel('교통사고.xlsx',skiprows=2,index_col='월')
print(df)
# df['피해수']=df['사망자수(명)']+df['부상자수(명)']
# print(df)


df.loc['합계']=[df['사고건수(건)'][:12].sum(),df['사망자수(명)'][:12].sum(),df['부상자수(명)'][:12].sum(),df['교통사고 피해수(명)'][:12].sum()]
df.loc['평균']=[df['사고건수(건)'][:12].mean(),df['사망자수(명)'][:12].mean(),df['부상자수(명)'][:12].mean(),df['교통사고 피해수(명)'][:12].mean()]
print(df)
filt=df['사고건수(건)']<df['사고건수(건)']['평균']
f=df["사망자수(명)"]<230
df.drop(index=df[f].index,inplace=True)
print('사망자수 230 이상')
print(df)
print('-'*80)
df.drop(index=df[filt].index,inplace=True)
print('사고건수 평균이상')
print(df)

