import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=15



# 국어 영어 수학 누적 막대 그래프
df= pd.read_excel('score.xlsx')
x=df['이름']
y1=df['국어']
y2=df['영어']
y3=df['수학']
plt.figure(figsize=(8,5))
plt.barh(x,y1,label='국어')
plt.barh(x,y2,left=y1,label='영어')
plt.barh(x,y3,left=y1+y2,label='수학')
plt.grid(alpha=0.5,axis='y')
# 범례 가로로 3개 표시
# plt.yticks([0,50,100,150,200,250,300,350])
plt.legend(ncol=3)
plt.show()