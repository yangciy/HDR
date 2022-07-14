from random import *

numlist=[i for i in range(1,46)]

print(numlist)
shuffle(numlist)  # 리스트 섞기가 가능한 함수
print(numlist)
print(sample(numlist,k=6)) # 리스트 중 해당되는 수만큼 선택가능함수

# a= random.random()
# print(a)
# round(a,3)
# print((round(a*100)/100))
# print('{:.2f}'.format(a))