import numpy as np

# list1= [9,2,7,5,6,8,1,4,3,0]
# arr =np.array(list1)
# print(arr)
# # arr.sort()
# print(arr)
# # 역순 ::-1
# print(arr[::-1])


arr= np.array([[5,9,10,3,1],[8,3,4,2,5]])
print(arr)

# arr.sort(axis=0)
arr.sort(axis=1)
print(arr)