import pandas as pd

df= pd.read_excel('stu1000.xlsx',index_col='학번')
# print(df)
def school(x):
    if x==1:
        return '구로고'
    elif x==2:
        return '디지털고'
    elif x==3:
        return '단지고'
    
def pro(x):
    if x==1:
        return 'Java'
    elif x==2:
        return 'c'
    elif x==3:
        return 'Python'
    elif x==4:
        return 'Javascript'
    elif x==5:
        return 'JAVA'

def score(x):
    if x>=90:
        return 'A'
    elif x>=80:
        return 'B'
    elif x>=70:
        return 'C'
    elif x>=60:
        return 'D'
    else:
        return 'f'
    
df['합계']=df['국어']+df['영어']+df['수학']+df['사회']+df['과학']
df['평균']=df['합계']/5
    
df['학교']=df['학교'].apply(school)
df['SW특기']=df['SW특기'].apply(pro)
df['평가']=df['평균'].apply(score)

print(df)

# 2
filt=df['합계']>=400
print('합계 400이상 수학 평균 :',df[filt]['수학'].mean())