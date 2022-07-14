import numpy as np

arr=np.random.randn(16).reshape(4,4)
arr2=np.where(arr>0,2,-2)
# print(arr)
print(arr2)


arr3= np.arange(1,12,2).reshape(3,2)
arr4= np.arange(2,13,2).reshape(3,2)
arr5= np.concatenate([arr3,arr4],axis=0)
print(arr5)

arr6= np.arange(100).reshape(10,10)

a,b=np.split(arr6,[3],axis=1)
print(a)
print(b)