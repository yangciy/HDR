#두 수를 입력 받아 사칙연산이 되도록 프로그램 하시오
#무한 반복 할수 있도록 한다
ch=0
# 얕은 복수 (주소 값)

#list1=[[0]*2]*2 

#list 깊은 복사 deep copy (새로운 공간을 만듦)
list1= [[0]*2 for _ in range(5)]
# print(list1)
# list1=[[0,0],[0,0]]
# print(list)
while True:
    if ch<len(list1) :    
        no1= int(input('숫자를 입력하세요..>>>'))
        no2= int(input('두번째 숫자를 입력하세요..>>>'))
     
        list1[ch][0] = no1
        list1[ch][1] = no2
        print('{} + {} = {}'.format(no1,no2,no1+no2))
        print('{} - {} = {}'.format(no1,no2,no1-no2))
        print('{} * {} = {}'.format(no1,no2,no1*no2))
        print('{} / {} = {:.2f}'.format(no1,no2,no1/no2))
    
    else :
        print(list1)
        break
    ch+=1
