from random import *

# randNum=[i+1 for i in range(25)]

randNum=[]
for i in range(25):
    randNum.append(i+1)
    
for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno] = randNum[rno],randNum[0]
print('섞은 후 리스트 :',randNum)    
    

arrs=[]
for i in range(0,5):
    
    arr2 = [randNum [5*i+j] for j in range(0,5)]
    arrs.append(arr2)
print(arrs)




# for i in range(0,5):
#     arr2=[5*i+j for j in range(1,6)]
#     arrs.append(arr2)
while True:
    # 1~25 출력
    for arr in arrs:
        for i in arr:
            print('{:2s}'.format(str(i)),end=' ')
        print()
        
    choice=int(input('1~25의 숫자를 입력하세요.>>>>>>'))

    for i, arr in enumerate(arrs):
        if choice in arr:
            x= arr.index(choice)
            arrs[i][x]='X'
    




# 0으로 채워진 5*5 2차원 배열을 생성하ㄱ소
# zero=[]
# for i in range(5):
#     zero2=[0*j for j in range(5)]
#     zero.append(zero2)
    
# print(zero)
# for i in range (0,4):
#     for j in range (0,3):
#         pass