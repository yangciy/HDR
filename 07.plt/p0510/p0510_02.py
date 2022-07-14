import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 


plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('score.xlsx')
print(df)
colors=['#b8ffd2','#5d84c7','#f788f0','#e9f5cb','#e4f5f3','#e01f26']
df2=df[:5].sort_values('국어')
values=df2['국어']
label=df2['이름']
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}
def custom_autopct(pct):
    if pct >10:
        return '{:.1f}%'.format(pct)
    else :
        return '생략'
plt.figure(figsize=(8,5))
plt.pie(values,labels=label,colors=colors,autopct=custom_autopct,startangle=90,counterclock=True,wedgeprops=wedgeprops,pctdistance=0.7)
plt.legend(loc=(1.1,0.3))
plt.show()