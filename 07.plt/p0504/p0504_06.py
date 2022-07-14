import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=12

df=pd.read_excel('score.xlsx')
x=df['이름']
y=df['국어']
z=df['영어']
# plt.plot(x,y,label='성적',linewidth=2,color='r',marker='x',linestyle='-')     # marker( o, x, v)  linestyle(none,:,-,--)
# plt.plot(x,y,'bo--')
# plt.plot(x,y,marker='o',markersize=10,markeredgecolor='red',markerfacecolor='yellow')
plt.plot(x,y,'bo-',ms=8,mec='y',mfc='y',label='국어',linewidth=2,alpha=0.2)
plt.plot(x,z,'ko-',ms=8,mec='red',mfc='r',label='영어',linewidth=2)
plt.legend(loc='upper right')
plt.title('성적 그래프')

plt.xlabel('이름',loc='center')
plt.ylabel('점수',loc='center')

plt.show()