# 1~100 홀수만 출력
# ch=0

# while ch<=100:
#     if ch%2==1:
#         print(ch,end=' ')
#     ch+=1


ch=1 

while ch<=9:
    if ch %3==0:
        ch+=1
        continue
    print('2 * {} = {}'.format(ch,ch*2))
    ch+=1
    
     