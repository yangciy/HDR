# 연령별 인구 현황 여자부분 출력
import pandas as pd

df_m=pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols='B,E:Y')






df_w=pd.read_excel('연령별인구현황.xlsx',skiprows=3,usecols="B,AB:AV")
df_w.columns=df_m.columns
# print(df)
# print(df.columns)
# print(df['100세 이상.1'])
df_w['100세 이상']=df_w['100세 이상'].str.replace(',','').astype(int)
# print("여성 100세이상 합계: ",df_w['100세 이상.1'][1:].sum())
a=df_w['100세 이상'][1:].sum()
# print(a)
df_w.set_index('행정기관',inplace=True)
print(df_w,"여성 100세이상 합계: {:,d}".format(a))


#컬럼명 변경
# df.rename(columns={'100세 이상.1':'100세 이상'},inplace=True)
# df.columns.values  특수문자 보기