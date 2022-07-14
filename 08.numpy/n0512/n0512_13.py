import numpy as np

arr=np.random.randint(1,101,100).reshape(10,10)
print(arr)
idx=np.where(arr>50)
print(arr[idx])

arr2=np.random.randint(0,21,20)

idx2=np.where(arr2>10,arr2,0)
print(idx2)