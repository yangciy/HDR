import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')
# 다중 막대 그래프
x=np.arange(8)
y1=df['국어']
y2=df['영어']
y3=df['수학']

plt.bar(x-0.25,y1,label='국어',width=0.25)
plt.bar(x,y2,label='영어',width=0.25)
plt.bar(x+0.25,y3,label='수학',width=0.25)
plt.legend()
plt.ylim(0,110)
plt.xticks(x,df['이름'],size=8)
plt.show()

