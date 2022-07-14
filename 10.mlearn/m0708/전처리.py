from operator import contains
import pandas as pd
import numpy as np

df=pd.read_csv('samsung.csv')
model=["갤럭시", 'galaxy','플립','울트라','폴드','노트','알파','s','a','j','m','z','엣지',\
    'edge','아이폰','iphone','xr','xs','x','se','미니','프로','프로맥스','pro','max']

sw=[]
for i in model:
    # df.reset_index(drop=True, inplace=True)
    df_1=df[df['폰모델 제목'].str.contains(i)]
    # if df_1 is None:
    #     continue
    df=pd.concat([df_1,df],axis=0)
    print(df)
    
a=df['폰모델 제목'].unique()
print(df['폰모델 제목']==a)