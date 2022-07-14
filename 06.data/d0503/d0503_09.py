import pandas as pd

import pandas as pd
import numpy as np

df= pd.read_excel('stu1000.xlsx',index_col='학번')


def school(x):
    if x==1:
        return '구로고'
    elif x==2:
        return '디지털고'
    elif x==3:
        return '단지고'
    
def sw(x):
    if x==1:
        return 'Java'
    elif x==2:
        return 'c'
    elif x==3:
        return 'Python'    
    elif x==4:
        return 'Javascript'    
    # elif x==5:
    #     return 'JAVA'   
    else :
        return np.nan 
    
df['학교']=df['학교'].apply(school)
df['SW특기']=df['SW특기'].apply(sw)
# print(df)

result=df.groupby('학교')['학년'].value_counts()
# print(result)
# normalize=True 비율로 출력
print(df.groupby('학교')['학년'].value_counts().loc['구로고'])
temp=(df.groupby('학교')['학년'].value_counts(normalize=True).loc['구로고'])
print(temp)