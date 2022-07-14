import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

df=pd.read_excel('stu1000.xlsx')
# print(df)

df_2=df.groupby('학년').size()
df_3=list(df_2)

for i, (rank,cnt) in enumerate(df_2.iteritems()):
    print(i,rank,cnt)
    
    
a=df['학년']==1
b=df['학년']==2
c=df['학년']==3
x=(df[a]['학년'].count())
y=(df[b]['학년'].count())
z=(df[c]['학년'].count())
plt.figure(figsize=(8,5))
values=[x,y,z]
labels=['1학년','2학년','3학년']

wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}
plt.pie(values,labels=labels,autopct='%.1f%%',wedgeprops=wedgeprops,pctdistance=0.7,startangle=90,counterclock=False)
plt.title('학년별 비율')
plt.legend(loc=(1.1,0.3),title='학년별 인원')
plt.show()
