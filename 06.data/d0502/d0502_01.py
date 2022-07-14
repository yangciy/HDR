import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df)
# print(df.index)
# index 추가
# df.loc['9번']=['이순신','디지털고',200,100,100,100,100,100,'C']
# print(df)
# column 추가
# df['총합']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
# print(df)
# 데이터 수정 전체 컬럼 변경
# df['학교'].replace({'구로고':'단지고','디지털고':'비비고'},inplace=True)
# print(df)
# # 소문자 변경   
# df['SW특기']= df['SW특기'].str.lower()
# df['SW특기']= df['SW특기'].str.upper()
# df['SW특기']= df['SW특기'].str.capitalize()
# df['SW특기'].replace({'java':'javaC'},inplace=True)
# df['학교']=df['학교']+'등학교'
# df['키']=df['키'].astype(str)+'cm'


# filt= df['키']>=190
# df.loc[filt,'국어']=100
# row index 수정
# df.loc['4번',['학교','SW특기']]=['즐기고','HTML']
# df.loc['2번','국어']=50
# filt=df['국어']==40
# df.loc[filt,'국어']=50

# filt=df.loc['2번']['국어']==40
# if filt:
#     df.loc['2번',['영어','수학','사회','과학']]=[40,40,40,40]
    
# df.loc['2번',['영어','수학','사회','과학']]=[40,40,40,40]
# df.loc['2번'][filt,'영어']=40
# filt=(df['이름']=='강태원') &(df['국어']==40)

# df.loc[filt,'수학']=40
# df.loc[filt,'과학']=40
# df.loc[filt,'사회']=40
# df.loc[filt,['영어','수학','과학','사회']]=[40,40,40,40]
# print(filt)
print(df)