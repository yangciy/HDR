import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')

x=df['지원번호']
y=df['키']
plt.plot(x,y,'o--',label='키')
plt.legend()
plt.title('키높이')
for i,txt in enumerate(y):
    plt.text(x[i],y[i]+1.5,txt,ha='center')

plt.show()
