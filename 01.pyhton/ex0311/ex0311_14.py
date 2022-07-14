#입력한 단 부터 9단까지 출력

a= int(input('시작할 단을 입력하세요.>>>'))
b= int(input('마지막 단을 입력하세요.>>>'))

if a>b:
    a,b=b,a
    for i in range(a,b+1):
        for j in range(1,10):
            print('{} * {} = {}\t'.format(i,j,i*j),end=' ')
        print()
else:
    for i in range(a,b+1):
        for j in range(1,10):
            print('{} * {} = {}\t'.format(i,j,i*j),end=' ')
        print()





# for i in range(1,10):
#     for j in range(2,10):
#         print('{} * {} = {} \t'.format(j,i,i*j),end=' ')
#     print()    