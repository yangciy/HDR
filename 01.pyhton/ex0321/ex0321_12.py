# # 로또 맞추기 게임
# # 로또 6자리 생성
# # 입력 6개 생성
# # 로또 번호와 입력 번호 확인
# # 똑같은 로또 번호 개수, 번호를 출력하시오.

from random import *
from test import *

randNum=[]
randNum.append(10)
lottoNum(randNum)
print(randNum)



# def lottoNum(randNum):
#     print(randNum)
#     randNum=10
#     return randNum
# def tempLotto(randNum):
#     print(randNum)
#     randNum=500
#     return randNum
# randNum=4
# randInput=[]

# randNum =lottoNum(randNum)
# print(randNum)
# randNum=tempLotto(randNum)

# print('로또숫자리스트 :',randNum)        


# # lotto=[i+1 for i in range(45)]
# # shuffle(lotto)
# # lottoD=sample(lotto,6)


# # choice=[]
# # for i in range(6):
# #     a= int(input('1~45 까지의 수를 입력하세요.'))
# #     choice.append(a)
    
# # print('로또 번호: ',lottoD)
# # print('입력 번호: ',choice)

# # listL=[]
# # for i in choice:
# #     if i in lotto:
# #             listL.append(i) 
               
# # print('맞은 개수: ',count)
# # print('맞은 번호: ',listL)