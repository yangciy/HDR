import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

df= pd.read_excel('score.xlsx')

fig,axs = plt.subplots(2,2,figsize=(10,6))
x= df['이름']
y= df['국어']
z= df['영어']
z2= df['수학']
fig.suptitle('4개의 전체제목 그래프')
axs[0,0].bar(x,y,label='국어')
axs[0,0].set_title('국어점수')
axs[0,0].set(xlabel='이름',ylabel='국어')
axs[0,0].set_facecolor('#fff2cf')
axs[0,0].grid(linestyle='--',linewidth=0.5)
axs[0,0].legend()
axs[0,1].plot(x,z,label='영어')
axs[0,1].plot(x,z2,label='수학')
axs[0,1].set_title('영어, 수학')
axs[0,1].legend(loc='lower right')
axs[1,0].barh(x,df['키'])
axs[1,1].plot(x,df['사회'],color='g',alpha=0.5)
plt.show()  
