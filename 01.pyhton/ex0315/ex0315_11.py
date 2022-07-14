from random import *

randNum=[]

for i in range(25):
    randNum.append(i+1)
print('섞기 전 리스트:',randNum)    

for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno]=randNum[rno],randNum[0]
print('섞은 후 리스트 :', randNum)


arrs=[]
for i in range(0,5): 
    arr2 = [randNum[5*i+j]for j in range(0,5)]
    arrs.append(arr2)
print(arrs)


while True:
    for arr in arrs:
        for i in arr:
            print('{:2s}'.format(str(i)),end=' ')
        print()
        
    choice= int(input('1~25 숫자를 입력하시오. >>>  '))
    
    for i, arr in enumerate(arrs):
        if choice in arr:
            arrs[i][arr.index(choice)]='X'