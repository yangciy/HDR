import pandas as pd

def sV(s):
    if s>=90:
        return 'A'
    elif s>=80:
        return 'B'
    elif s>=70:
        return 'C'
    elif s>=60:
        return 'D'
    else:
        return 'F'
df= pd.read_excel('score.xlsx',index_col='지원번호')

df['사회평가']=df['사회'].apply(sV)
df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']

df['평균']=df['합계']/5
df['평균평가']=df['평균'].apply(sV)
cols=['이름','학교','키','국어','영어','수학','과학','사회','사회평가','합계','평균','평균평가','SW특기']

print(df[cols])