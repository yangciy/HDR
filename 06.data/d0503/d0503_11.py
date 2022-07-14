import pandas as pd
# concat 하단 데이터 넣어주기

data ={
    '이름':['주바다','공유진','송선유','양홍욱'],
    '키':[180,182,188,179],
    '몸무게':[47,49,50,45]
}
data2 ={
    '이름':['주바다','공유진','송선유','윤상운'],
    '전공':['컴퓨터공학','기계공학','독문학','컴퓨터공학'],
    '실력':['고급','중고급','특급','중고급']
}
# data join - 주데이터(data)를 중심으로 join
# merge : 열기준 컬럼명으로 합침
# inner : 중복되는 데이터만 출력 (교집합)
# left : data에 있는 이름 기준
# right : data2에 있는 이름 기준
# outer : 합집합
df=pd.DataFrame(data)
df2=pd.DataFrame(data2)

# mdf=pd.merge(left=df,right=df2,how='inner',on='이름')
# print(mdf)
mdf2=pd.merge(left=df,right=df2,how='left',on='이름')
mdf2['전공'][3]='자율전공'
mdf2['실력'][3]='초급'
print(mdf2)
# mdf3=pd.merge(left=df,right=df2,how='right',on='이름')
# mdf3['키'][3]=189
# mdf3['몸무게'][3]=89
# print(mdf3)

# mdf4=pd.merge(left=df,right=df2,how='outer',on='이름')
# mdf4['전공'][3]='자율전공'
# mdf4['실력'][3]='초급'
# mdf4['키'][4]=189
# mdf4['몸무게'][4]=89
# print(mdf4)
# print(df)
# print(df2)
# temp= pd.Series([-20,-10,10,20])
# print(temp)