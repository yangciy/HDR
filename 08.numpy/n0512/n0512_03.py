import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 

plt.rc('font', family='AppleGothic') 			
matplotlib.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['font.size']=10


arr1 =np.arange(1,11,4)
print(arr1)

arr2=np.linspace(1,11,4)
print(arr2)
# linspace = 균등으로 나누고 retstep으로 간격 확인 가능
arr3= np.linspace(0,10,3,retstep=True)
print(arr3)

# list_data= [1,2,3,4,5]
# arr= np.array(list_data,dtype=float)
# print(arr.dtype)

# arr2= np.arange(5)+1
# print(arr2)

# arr3= np.arange(1,6)
# print(arr3)

# arr4= np.arange(0,21,5)
# print(arr4)