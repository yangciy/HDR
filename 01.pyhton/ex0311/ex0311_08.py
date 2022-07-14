# 6개의 로또
import random
from random import *
lotto= []
count= 0
temp= randrange(1,46)
user=[]
#입력
for i in range(0,6):
    user.append(int(input('{}. 숫자를 입력하시오.>>'.format(i+1))))
print('숫자 입력 완료')


#로또
while count!=6:
    temp= randrange(1,46)
    if temp not in lotto:
        lotto.append(temp)
        count +=1
    else:
        print('추첨완료')
        break
print('로또번호',lotto)
print('입력번호',user)
#비교
aa=[]

for i in range(0,6):
        if user[i] in lotto:
            aa.append(user[i])
print('맞은 갯수',len(aa))      
print('맞은 번호',aa)        
# l_count=0

# if my_num[0] in lotto:
#     l_count += 1
#     ok_nun.append(my_num[i])