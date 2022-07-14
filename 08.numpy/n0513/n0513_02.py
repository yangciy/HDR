import numpy as np

# 1~8 2,2 배열
# arr=np.arange(1,9).reshape(2,4)
# print(arr)


arr= np.arange(8)
idx= np.where(arr>5)
print(arr[idx])

idx2= np.where(arr>5,100,0)
print(idx2)