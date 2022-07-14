from random import *

# randNum=[i+1 for i in range(25)]

randNum=[]
for i in range(25):
    randNum.append(i+1)
print('섞기 전 리스트 :',randNum) 
for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno] = randNum[rno],randNum[0]
print('섞은 후 리스트 :',randNum)



# aa=[1,2,3,4,5]
# input1= int(input('1~5까지 입력'))
# for i,a in enumerate(aa):
#     if a == input1:
#         x=aa.index()
#         aa[x]= 'x'
                
# print(aa)