import numpy as np


arr1=np.arange(10)
arr2=np.arange(10,20)
np.savez('np2.npz',a1=arr1,a2=arr2)
a=np.load('np2.npz')
print(a['a1'])
print(a['a2'])


# npy파일 저장
# np.save 저장
# np.load 읽어오기


# arr = np.arange(10)
# np.save('np1.npy',arr)
# a=np.load('np1.npy')

# print(a)