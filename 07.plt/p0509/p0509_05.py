import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')
x=df['이름']
y=df['키']
plt.figure(figsize=(8,5))
plt.bar(x,y,width=0.5)
# plt.yticks([170,180,190,200,210])
for i, txt in enumerate(y):
    plt.text(x[i],y[i],txt,ha='center')
plt.xticks(x,rotation=45)
plt.ylim(160,210)
plt.show()