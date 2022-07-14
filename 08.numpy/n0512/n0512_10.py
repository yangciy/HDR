import numpy as np

list_data= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
arr=np.array(list_data)
# arr = np.arange(1,13).reshape(3,4)
# print(arr)
# # 인덱싱
# print(arr[0,1])
# # numpy 인덱싱 (0,1),(2,3)
# idx= arr[[0,2],[1,3]]

idx=arr[[0,1,2],[1,2,3]]
print(idx)
