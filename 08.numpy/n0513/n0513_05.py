import numpy as np

arr= np.random.randint(1,10,4).reshape(2,2)
print(arr)
arr = arr*10
print(arr)

arr2= np.random.randint(1,10,25).reshape(5,5)
print(arr2)
arr3 =np.where(arr2>5,arr2*10,arr2)
print(arr3)

# arr=np.array([20,30,40,50])
# arr2= np.arange(4)
# arr3=arr-arr2
# print(arr)
# print(arr2)
# print(arr3)


# arr = np.arange(1,12,2)
# print(arr)
# print(arr.shape)

# list_data=[1,3,5,7,9,11]

# arr=np.array(list_data)
# print(arr)
# arr2= arr+3
# print(arr2)


# list_data2=[]
# for i in list_data:
#     list_data2.append(i+3)
    
# print(list_data2)