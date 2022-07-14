import pandas as pd
#학교컬럼 그룹 합계 역순정렬
df= pd.read_excel('stu1000.xlsx',index_col='학번')
# def school(x):
#     if x==1:
#         return '구로고'
#     elif x==2:
#         return '디지털고'
#     elif x==3:
#         return '단지고'
    
# def sw(x):
#     if x==1:
#         return 'Java'
#     elif x==2:
#         return 'c'
#     elif x==3:
#         return 'Python'    
#     elif x==4:
#         return 'Javascript'    
#     elif x==5:
#         return 'JAVA'   
#     # else :
#     #     return np.nan 
    
# df['학교']=df['학교'].apply(school)
# df['SW특기']=df['SW특기'].apply(sw)

df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균']=df['합계']/5
# print(df)
result= df.groupby(['학교','학년']).sum().sort_values('합계',ascending=False)
print(result)
print(df.groupby(['학교','학년']).mean().sort_values('합계',ascending=False))