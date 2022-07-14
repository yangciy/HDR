import pandas as pd

df = pd.read_excel('user.xlsx',index_col='id')
print(df)

df['total']=0
print(df)

#500 505 910, 950  601~700
df.loc['total'][500,505,910,950]=100
df.loc['total'][601:700]=100
print(df.head(500))