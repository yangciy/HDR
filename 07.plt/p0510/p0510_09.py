from unittest import skip
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
import re
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10
def dol(x):
    dx=float(re.sub(r'[^0-9.]','',x))
    return dx
    

df1_m=pd.read_excel('201201_인구현황.xlsx',skiprows=3,usecols='E:Y')
df1_w=pd.read_excel('201201_인구현황.xlsx',skiprows=3,usecols='AB:AV')

x=df1_m.columns
y=df1_m.iloc[0].apply(dol).values
z=df1_w.iloc[0].apply(dol).values
for i in range(len(y)):
    y[i]=y[i]/1000
for i in range(len(z)):
    z[i]=z[i]/1000
print(y)
print(z)

plt.barh(x,-y,color='r',label='남자')
plt.barh(x,z,color='b',label='여자')
plt.xlabel('단위: 천명',loc='right')
plt.legend()
plt.show()




df2_m=pd.read_excel('201201_인구현황.xlsx',skiprows=3,usecols='B,C')
df2_w=pd.read_excel('201201_인구현황.xlsx',skiprows=3,usecols='B,Z')


# print(df2_m)
def custom_autopct(pct):
    if pct >5:
        return '{:.1f}%'.format(pct)
    else :
        return ''
df2_m['전체']=df2_m['남 인구수'].apply(dol)+df2_w['여 인구수'].apply(dol)
x=df2_m['행정기관']
y=df2_m['전체']
for i in range(len(y)):
    y[i]=y[i]/1000
x=x[1:]
y=y[1:]
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}

plt.pie(y,labels=x,startangle=90,counterclock=True,pctdistance=0.7,autopct=custom_autopct,wedgeprops=wedgeprops)
plt.show()
