import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10


df= pd.read_excel('score.xlsx')
df['학년']=[3,3,2,1,1,3,2,2]
x=df['영어']
y=df['수학']
# sizes=[1000,1000,3000,3000,1000,1000,2000,2000]
# sizes=np.random.rand(8)*1000
sizes= df['학년']*1000
plt.scatter(x,y,s=sizes,c=df['학년'],cmap='BuGn')
plt.colorbar(ticks=[1,2,3],label='학년',shrink=0.3,orientation='horizontal')
plt.show()
