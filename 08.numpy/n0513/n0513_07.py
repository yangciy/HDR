import numpy as np

arr1=np.arange(4).reshape(2,2)
arr2=np.arange(4).reshape(2,2)


# 두 수의 더하기
idx=np.add(10,100)
print(type(idx))
print(idx)
# 두 수의 빼기
idx= np.subtract(10,100)
print(idx)
# 두 수의 곱
idx= np.multiply(10,100)
print(idx)
# 두 수의 나누기
idx= np.divide(10,100)
print(idx)
# 제곱
idx= np.power(2,5)
print(idx)
# 제곱근
idx= np.sqrt(2)
print(idx)
# arr1= np.arange(4).reshape(2,2)

# arr2 =np.arange(2)
# arr3= arr1+arr2
# print(arr3)