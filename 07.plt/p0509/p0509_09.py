import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

df=pd.read_excel('stu1000.xlsx')
df['합계']=df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
filt= df['학년']==1
df2=df[filt]

df2.sort_values('합계',inplace=True,ascending=False)
data=df2.head(5)

print(data)
x=np.arange(5)
y1=data['국어']
y2=data['영어']
y3=data['수학']
y4=data['과학']
y5=data['사회']
plt.figure(figsize=(20,5))

plt.bar(x-0.2,y1,label='국어',width=0.1)
plt.bar(x-0.1,y2,label='영어',width=0.1)
plt.bar(x,y3,label='수학',width=0.1)
plt.bar(x+0.1,y4,label='과학',width=0.1)
plt.bar(x+0.2,y5,label='사회',width=0.1)
plt.xticks(x,data['이름'],size=10)
plt.ylim(0,120)
plt.legend(ncol=5,loc='upper center')

for i,txt in enumerate(y1):
    plt.text(x[i]-0.2,y1.iloc[i]+1,txt,ha='center')
for i,txt in enumerate(y2):
    plt.text(x[i]-0.1,y2.iloc[i]+1,txt,ha='center')    
for i,txt in enumerate(y3):
    plt.text(x[i],y3.iloc[i]+1,txt,ha='center')    
for i,txt in enumerate(y4):
    plt.text(x[i]+0.1,y4.iloc[i]+1,txt,ha='center')    
for i,txt in enumerate(y5):
    plt.text(x[i]+0.2,y5.iloc[i]+1,txt,ha='center')    
plt.show()