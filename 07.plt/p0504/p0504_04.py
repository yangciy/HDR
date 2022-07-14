import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10


x=[1,2,3]
y=[192,194,198]
# legend를 사용해야 범례 호출 가능
plt.plot(x,y, label='키높이')
plt.legend(loc='upper right')
plt.title('키높이 그래프')
plt.xlabel('번호',color='blue',loc='center')
plt.ylabel('키',color='red',loc='top')
# 그래프 눈금 간격 표시
plt.xticks([1,2,3])
plt.yticks([192,193,194,198])
  
plt.show()