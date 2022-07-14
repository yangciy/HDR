import pandas as pd

df=pd.read_excel('user.xlsx',index_col='id')
print(df.index)
# 500~600,605 first_name, email

print(df.iloc[(df.index>=500) & (df.index<=600) |(df.index==605),[0,2]])
print(df.iloc[(df.index>=500) & (df.index<=600) |(df.index==605)][['first_name','email']])
print(df.loc[(df.index>=500) & (df.index<=600) |(df.index==605),['first_name','email']])