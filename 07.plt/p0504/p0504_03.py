import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

# x=[1,2,3]
# y=[2,4,8]
df=pd.read_excel('score.xlsx')
x=df['이름']
y=df['국어']

plt.plot(x,y)
# 상단 title 라벨 이름
plt.title('실적 그래프')
plt.xlabel('이름',color='#ff0000',loc='right')  #loc = left,center,right
plt.ylabel('국어 점수',color='#00ff00',loc='top')#loc = top, center, bottom
plt.show()

