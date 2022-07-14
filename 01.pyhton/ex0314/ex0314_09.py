#3의 배수를 제외하고
# 

total,i=0,0
for i in range(1,101):
   
    if i%3==0:
        continue
    total+=i
    print(i,end=' ')
    if total>1000:
        break

print('넘었을 때의 합: {} , 숫자 {}'.format(total,i))