import random
from random import *
temp = randrange(1,46)
lotto=[]
for i in range (0,6):
    while temp in lotto:   
        temp = randrange(1,46)
    lotto.append(temp)    


print(lotto)


temp_a = randrange(1,46)
lotto=[]
while len(lotto) !=6:
    temp_a = randrange(1,46)
    if temp_a not in lotto:
        lotto.append(temp_a)        
    
print(len(lotto))
print(lotto)
    
count=0
while True:
    if count<=5:
        temp = randrange(1,46)
        if temp not in lotto:
            lotto.append(temp)
            count+=1
        else :
            print('추첨완료')
            break
        
print(lotto)