# 1) 남자(male)이면서 pclass가 1인 승객을 출력하시오.
# 2) Survivied 1이면서 age 20이하인 승객을 출력하시오.
# 3) 그룹 survivied,pclass 컬럼으로 수를 출력하시오.

import pandas as pd

df=pd.read_csv('train.csv',index_col='PassengerId')
# print(df)

# 1
filt =(df['Sex']=='male')&(df['Pclass']==1)
print(df[filt])

# 2
filt = (df['Survived']==1)&(df['Age']<=20)
print(df[filt])

#3
result=df.groupby(['Survived','Pclass']).count()
print(result)

member={
    '이름':['주바다','공유진','송선유','양홍욱'],
    '성별':['여','여','여','남'],
    '전화번호':['010-1111-1111','010-1111-2222','010-1111-3333','010-1111-4444']
}
score={
    '이름':['주바다','공유진','윤상운','송선유'],
    '국어':[100,99,95,100],
    '영어':[95,99,99,100]
}
df=pd.DataFrame(member)
df2=pd.DataFrame(score)
mdf=pd.merge(left=df,right=df2,how='inner',on='이름')
mdf2=pd.merge(left=df,right=df2,how='outer',on='이름')
print(mdf)
print(mdf2)