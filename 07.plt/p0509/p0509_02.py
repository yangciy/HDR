import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')

x=df['지원번호']
y=df['국어']

# 그래프 크기 조정
plt.figure(figsize=(15,5),facecolor='y',dpi=100)
plt.plot(x,y,label='국어')
plt.plot(x,df['영어'],label='영어')
plt.plot(x,df['수학'],label='수학')
plt.title('학생성적 그래프')
plt.xlabel('학생번호')
plt.ylabel('점수')
plt.yticks([0,20,40,60,80,100])
plt.legend(loc='upper right')
plt.savefig('핵생성적.png',dpi=200)
plt.show()