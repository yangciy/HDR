from random import *

numbers = [i for i in range(1,46)]

for i in range(2000):
    ran_num= randint(0,44)
    numbers[0], numbers[ran_num] = numbers[ran_num], numbers[0]

print(numbers)





# a=[]
# for i in range(1,46):
#     a.append(i)
 # print(a)