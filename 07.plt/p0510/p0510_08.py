import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

df=pd.read_excel('score.xlsx')
x=df['이름']
y=df['키']
# y=[1100,1200,1500,1600,1000,1300,1100,1400]
z=df['국어']
fig,ax1 =plt.subplots()
ax1.set_ylim(160,210)
ax1.set_ylabel('키')
ax1.plot(x,y,'o-')
for i , val in enumerate(y):
    if i==0 or i==2:
        ax1.text(i,val-3,val,ha='center')
    # elif i==2:
        # ax1.text(i,val-3,val,ha='center')
    else:
        ax1.text(i,val+2,val,ha='center')
ax2=ax1.twinx()
ax2.set_ylim(10,110)
ax2.set_ylabel('국어',color='r')
ax2.plot(x,z,'rx-')
for i , val in enumerate(z):
    ax2.text(i,val+2,val,ha='center')
# plt.plot(x,y)
# plt.plot(x,z)
plt.show()
