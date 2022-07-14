import numpy as np

# 1차원 행렬
# arr=np.arange(10)
# arr2=np.arange(10,20)
# arr3= np.concatenate([arr,arr2])

# # 2차원 행렬
# arr1= np.arange(4).reshape(1,4)
# # print(arr1)
# arr2= np.arange(8).reshape(2,4)
# # print(arr2)
# # axis=0 기준 (행) 행의 개수가 맞아야함
# arr3=np.concatenate([arr1,arr2],axis=0)
# print(arr3)

arr1=np.arange(4).reshape(2,2)
arr2=np.arange(4,8).reshape(2,2)
# axis=1 기준 (열) 열의 개수가 맞아야함
arr3=np.concatenate([arr1,arr2],axis=1)
print(arr3)