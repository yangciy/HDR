import numpy as np



arr = np.random.randint(1,100,(5,10))
# print(arr)

idx= np.where(arr%2==0,arr*10,arr*2)
print(idx)
# idx= np.where(arr<50,arr,100)
# print(arr[idx])

i_arr= arr<50
arr[i_arr]=100
print(arr)














# list1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# arr = np.array(list1)

# idx_arr = [
#     [False,True,False],
#     [True,True,False],
#     [False,False,True]
# ]
# idx=np.array(idx_arr)
# # idx2=idx_arr.np
# print(arr[idx])







# arr = np.arange(9).reshape(3,3)

# bol_arr = arr>5
# print(arr[bol_arr])

# idx_arr = np.where(arr>5,arr,0)
# print(idx_arr)