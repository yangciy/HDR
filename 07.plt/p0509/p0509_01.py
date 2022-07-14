import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')

x=df['지원번호']
y=df['키']
# x=[1,2,3]
# y=[-2,4,8]
# plt.plot(x,y,marker='o',linestyle=':',label='키')
plt.plot(x,y,'ro--',label='키')
plt.legend()
plt.title('학생 그래프')
plt.xlabel('번호',color='r')
plt.xticks([0,1,2,3,4,5,6,7,8])
plt.ylabel('키',color='g')
plt.yticks([170,180,190,200])
plt.grid(axis='x',color='y')
plt.grid(axis='y',color='b')
plt.show()