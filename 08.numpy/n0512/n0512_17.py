import numpy as np

arr=np.ones((3,5))
print(arr)

arr2=np.random.randint(1,11,6).reshape(3,2)
print(arr2)

arr3=np.concatenate([arr,arr2],axis=1)
print(arr3)

arr4_l,arr4_r=np.split(arr3,[4],axis=1)
print(arr4_r)
print(arr4_l)

arr5_r,arr5_l=np.split(arr3,[2],axis=0)
print(arr5_r)
print(arr5_l)