import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10
df=pd.read_excel('score.xlsx')

# x=df['국어']
# y=df['영어']
# sizes=np.random.rand(8)*1000
# plt.scatter(x,y,s=sizes)

# plt.show()

x=df['이름']
y=np.random.randint(60,101,8)
plt.title('집에가기 5분전')
plt.ylim(50,100)
plt.bar(x,y)
plt.show()