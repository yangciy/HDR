import pandas as pd
import random
df= pd.read_excel('score.xlsx',index_col='지원번호')

# 1. 요일 컬럼 추가
# 2. 0-6까지 숫자를 랜덤 입력
# 3. 함수 생성
def week(a):
    if a==0:
        return '월'
    elif a==1:
        return '화'
    elif a==2:
        return '수'
    elif a==3:
        return '목'
    elif a==4:
        return '금'
    elif a==5:
        return '토'
    elif a==6:
        return '일'
df['요일']=[0,0,0,0,0,0,0,0]
# df['요일']=[random.randint(0,6) for i in range(8)]

for i in range(df['요일'].count()):
    df['요일'][i]=random.randint(0,6)
df['요일']=df['요일'].apply(week)    
cols=list(df.columns)
df=df[cols[:3]+[cols[-1]]+cols[3:-1]]
print(df)


