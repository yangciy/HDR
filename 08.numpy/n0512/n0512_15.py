import numpy as np

arr=np.arange(8)
arr2=arr.reshape(2,4)
arr3=arr2.reshape(2,2,2)
print(arr3[1,0,0])
print(arr3[1,1,0])


# arr4= np.arange(1,5).reshape(2,2)
# print(arr4[0,1])
# arr5=arr4.reshape(4)
# # flatten(): 1차원으로 변경
# print(arr5)

# arr6=[
#     [15,8,12],
#     [11,7,3]]
# arr6=np.array(arr6)
# idx=np.where(arr6>10)
# print(arr6[idx].size)