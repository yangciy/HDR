import pandas as pd

df=pd.read_excel('score.xlsx',index_col='지원번호')

# filt = df['이름'].str.startswith('김')
filt = df['이름'].str.contains('근')
print(df[~filt])