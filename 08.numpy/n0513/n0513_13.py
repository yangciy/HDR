import numpy as np


arr=np.arange(1,10).reshape(3,3)
print(arr)

axis0=np.sum(arr,axis=0)
axis1=np.sum(arr,axis=1)

print(f"행의 합{axis0} \n열의 합{axis1}")










# arr = np.array([[1,2],[3,4]])
# print(arr)
# arr_sum = np.sum(arr)
# arr_max = np.max(arr)
# arr_min = np.min(arr)
# arr_mean = np.mean(arr)
# print(arr_sum)
# print(arr_max)
# print(arr_mean)
# print(arr_min)

# axis0=np.sum(arr,axis=0)
# axis1=np.sum(arr,axis=1)

# print(axis0)
# print(axis1)
# arr = np.arange(16).reshape(4,4)

# print('최대값 :',np.max(arr))
# print('최소값 :',np.min(arr))
# print('합계 :',np.sum(arr))
# print('평균 :',np.mean(arr))