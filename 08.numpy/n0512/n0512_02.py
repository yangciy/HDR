import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10

list_data=[
    [1,2,3],
    [4,5,6]
]
print(list_data)
arr = np.array(list_data)
print(arr.shape)
print(arr[0,1])
# arange : 순차적인 넘파이 행렬 생성
arr1= np.arange(4)
print(arr1)
# 2부터 9까지
arr2= np.arange(2,10)
print(arr2)
# 1부터 9까지 2씩 중가
arr3= np.arange(1,10,2)
print(arr3)

# x=[1,2,3,4,5,6,7,8,9,10]
# x1=np.arange(1,11)
# y=[2,4,8,16,32,64,128,64,32,16]


# plt.plot(x1,y)
# plt.show()