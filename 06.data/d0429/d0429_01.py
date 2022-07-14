import pandas as pd

df_m=pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,E:Y',index_col='행정기관')
df_w=pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,AB:AV',index_col='행정기관')


df_w.columns=df_m.columns
print(df_w.columns)
df_m.rename(columns={'0~4세':'4세'},inplace=True)
print(df_m.columns[0])
for i in range(18):
    df_m.rename(index={df_m.index[i]:df_m.index[i].strip()},inplace=True)
print(df_m.index.values)
# print(df['0~4세'])
# df['0~4세']=df['0~4세'].str.replace(',','').astype(int)
# print(type(df['0~4세']))
# print(df['0~4세'][1:].sum)