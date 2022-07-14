from random import *

num= randint(1,45)
count=0
while True:

    input1 = int(input('숫자를 입력하세요.>>>'))
    count+=1
    if num==input1:
        print('숫자가 같습니다.\n 입력한 숫자: {}\n 난수: {} 반복 횟수: {}'.format(input1,num,count))
        break
    else:
        print('숫자가 일치하지 않습니다.\n입력한 숫자: {}\n반복한 횟수: {}'.format(input1,count))
        if count==5:
            print('난수는 {} 였습니다. 새로 시작해주세요.'.format(num))
            break
    



# input1 = int(input('숫자를 입력하세요.>>'))

# if input1>100:
#     print('100보다 큰 수를 입력하셨습니다.')
# else:
#     print('100보다 작은 수를 입력하셨습니다.')
