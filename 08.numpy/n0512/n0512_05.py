import numpy as np

arr=np.arange(3,10)
print(arr[0])

arr2=np.full((5,5),1)
print(arr2)

list=[4,2,1,5,2,6,1,1,1]
arr3=np.array(list)
arr3=arr3.reshape(3,3)
print(arr3)

arr4=np.arange(0,31,2)
print(arr4)

arr5= np.linspace(0,4,9,retstep=True)
print(arr5)

