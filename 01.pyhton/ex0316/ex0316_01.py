from random import *
''' 
1. 리스트 생성
2. 리스트 1 ~ 25까지 숫자 입력
3. 랜덤섞기
4. 2차원배열 리스트 생성
5. 1차원리스트를 2차원 리스트에 추가
6. 2차원리스트 출력
7. 무한루프 -> 원하는 숫자를 입력받음
8. 입력받은 숫자를 X표시로 변경
'''
# 리스트 생성후 숫자입력
randN=[i+1 for i in range(25)]
# print(randN)

# 랜덤섞기
for i in range(250):
    rN=randint(0,24)
    randN[0],randN[rN]=randN[rN],randN[0]
# print(randN)

# 2차원 배열 리스트 생성 후 리스트에 추가
arrs=[]
for i in range(0,5):
    arr2=[randN[5*i+j] for j in range(0,5)]
    arrs.append(arr2)       
# print(arrs)
# 7,8
while True:
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end=' ')
        print()

    choice= int(input('숫자를 입력하세요.> (0을 입력시 프로그램 종료)  '))
    
    if choice==0:
        print('프로그램 종료')
        break
    
    for a, arr in enumerate(arrs):
        if choice in arr:
            arrs[a][arr.index(choice)]='X'
            
     