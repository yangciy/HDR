import numpy as np

# lst=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# arr=np.array(lst)

# 슬라이싱 0:2 - 행 0부터 2앞까지 0~1

# arr2= arr[0,0:2]

# arr2 = arr[0:,:2]
# print(arr2)

arr=np.arange(1,51).reshape(5,10)
print(arr)

arr2=arr[2:4,4:9]
print(arr2)