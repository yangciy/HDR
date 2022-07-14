total,i=0,0

for i in range(1,100):
    total +=i
    print(i,end=' ')
    if total>100:
        break

print('합: {} '.format(total))
print('100을 넘길 때의 숫자: {} '.format(i))








# a=input('문자를 입력하세요....')
# if a=='$':
#     print('$입니다.')
# else:
#     print('$가 아닙니다.')
