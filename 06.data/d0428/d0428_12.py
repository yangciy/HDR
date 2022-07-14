import pandas as pd

df=pd.read_excel('연령별인구현황.xlsx',skiprows=3)
print(df)

# moviexlsx 불러와서 최대관객수 출력
# df=pd.read_excel('시가총액1-200.xlsx')
# # print(df.columns[0])
# # df.set_index(df.columns[0],inplace=True)
# print(df)
# df.index.name='번호'
# print(df)
# print(df.index)
# print(df.loc[1])
# print(df[['N','종목명','현재가']])
# print(df['현재가'])
# df.set_index('N',inplace=True)
# print(df)
# print(df)
# print(df['관객 수'].nlargest(1))
# print(df['관객 수'].max())


# 영화, 개봉연도

# print(df[['영화','개봉 연도']][:3])




# data = {
# '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
# '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
# '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
# '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
# }
# df=pd.DataFrame(data)
# df.to_excel('movie.xlsx',index=False)

# print(df)