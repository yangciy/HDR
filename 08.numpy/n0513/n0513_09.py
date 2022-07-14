import numpy as np

# arr= np.arange(5)
# print(arr)
# print(arr.shape)

arr1=np.array([[1,1],[0,1]])
arr2=np.array([[2,0],[3,4]])
arr3=np.multiply(arr1,arr2)
result=np.dot(arr1,arr2)
print('곱\n',arr3)
print('단위행렬\n',result)


arr4=np.arange(1,7).reshape(2,3)
arr5=np.arange(7,13).reshape(3,2)
arr6=np.dot(arr4,arr5)
print('곱 ',arr6)

arr7=np.arange(1,10).reshape(3,3)
arr7[0,:]=arr7[0,:]*2
arr7[1,:]=arr7[1,:]*2

print('1행 *2 2행 *3',arr7)
