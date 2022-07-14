import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10


# df= pd.read_csv('daum_movie.csv')

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2016, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}

df = pd.DataFrame(data).sort_values('개봉 연도')
# df.index.name='영화'
df=df.reset_index(drop=True)

x=list(df['개봉 연도'])
y=list(df['평점'])
# print(df2)
plt.plot(x,y,'ro-',label='평점')
for i ,txt in enumerate(y):
    if i%2==1:
        plt.text(x[i],y[i]+0.1,txt,ha='center')
    else:
        plt.text(x[i],y[i]-0.1,txt,ha='center')
# plt.text(x[0],y[0]+0.1,df2['평점'][0],ha='center')
# plt.text(x[1],y[1]-0.1,df2['평점'][1],ha='center')
# plt.text(x[2],y[2]+0.1,df2['평점'][2],ha='center')
# plt.text(x[3],y[3]-0.1,df2['평점'][3],ha='center')
# plt.text(x[4],y[4]+0.1,df2['평점'][4],ha='center')
# plt.text(x[5],y[5]-0.1,df2['평점'][5],ha='center')
# plt.text(x[6],y[6]+0.1,df2['평점'][6],ha='center')
# plt.text(x[7],y[7]-0.1,df2['평점'][7],ha='center')

plt.title('연도별 영화 평점')
plt.legend()
plt.xticks([2005,2010,2015,2020])
plt.ylim([7,10])
plt.show()