import numpy as np


arr= np.arange(8).reshape(2,4)
print(arr)

# (2,2),(2,2)
# split(행렬,기준)
left,right= np.split(arr,[1],axis=0)

print(left)
print(right)