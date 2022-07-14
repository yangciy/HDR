from random import *


#1~100까지의 랜덤 숫자 생성
temp = randint(1,100)
cnt=0
list=[]
while cnt<5:
    cnt+=1
    input1= int(input('1~100사이의 원하는 번호를 입력하세요.>>>>>>'))
    list.append(input1)
    if temp==input1:
        print('정답입니다. 정답숫자 : {} 도전횟수 : {}'.format(input1,cnt))
        break
    elif temp>input1:
        print('입력한 숫자({})가 더 작습니다. 더 큰 수를 입력하세요...'.format(input1))
        print('시도 횟수 {}'.format(cnt))
    elif temp<input1: 
        print('입력한 숫자({})가 더 큽니다. 더 작은 수를 입력하세요.'.format(input1))
        print('시도 횟수 {}'.format(cnt))
print('{}번의 도전기회가 모두 소진되었습니다. 정답은 {} 입니다. 입력값 {}'.format(cnt,temp,list))
list.sort(reverse=True)
print(list)

# sort(), sort(reverse=True)