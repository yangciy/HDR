import numpy as np


arr=np.arange(6).reshape(3,2)
arr2=np.arange(10,16).reshape(2,3)
print(arr)
print(arr2)

result=np.dot(arr,arr2)
print(result)



# arr=np.random.randint(1,11,15).reshape(5,3)
# print(arr)
# arr2=np.array([4,2,1])
# print(arr2)

# result=np.dot(arr,arr2)
# print(result)


# list1 = np.array([[1,3],[2,4]])
# list2 = np.array([2,5])

# a= np.dot(list2,list1)

# print(a)
# list1=[[1,2],[3,4]]
# list2=[[5,6],[7,8]]

# arr1=np.array(list1)
# arr2=np.array(list2)

# arr3= np.dot(arr1,arr2)
# print(arr3)


# arr1 =np.array([1,2,3])
# arr2 =np.array([4,5,6])

# arr3 = arr1+arr2
# print(arr3)

# arr4= arr1-arr2
# print(arr4)

# arr5=arr1*arr2
# print(arr5)

# arr6=arr1%arr2
# print(arr6)