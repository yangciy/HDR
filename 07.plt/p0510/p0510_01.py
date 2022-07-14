import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 


plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15

values= [30,25,20,13,10,2]
labels= ['python','java','javascript','c#','c++','etc']
# 원 그래프
colors=['#17fc03','#5d84c7','#f788f0','#e9f5cb','#e4f5f3','#e01f26']
plt.figure(figsize=(8,5))
explode=[0.05,0.01,0,0,0,0]
plt.pie(values,labels=labels,explode=explode,colors=colors,autopct='%.1f%%',startangle=90,counterclock=False)
plt.title('원그래프')
plt.legend(loc=(1.1,0.3))
plt.show()

#