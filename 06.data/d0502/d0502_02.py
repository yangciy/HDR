import pandas as pd

df= pd.read_excel('score.xlsx',index_col='지원번호')


df['총합']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['결과']='불합격'

filt = df['총합']>400
df.loc[filt,'결과']='합격'
print(df)
