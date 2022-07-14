import numpy as np 
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10



# arr = np.random.randint(1,99,5)
# arr = np.random.rand(8)*100
# normal 평균이 0이고, 표준편차가 1인 표준 정규분포
arr = np.random.normal(0,1,(3,3))
print (arr)
# y=[1,2,3,4,5]
# plt.plot(y,arr)
# plt.show()
