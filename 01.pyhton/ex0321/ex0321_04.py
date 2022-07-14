def coffee(choice):
    print('[ 커피주문완료 ]')
    print('1. 종이컵 준비')
    print('2. 물 채우기')
    print('3. 커피를 내립니다.')
    if choice== 1:
        print('4. 커피를 컵에 추가합니다.')
    elif choice==2 :
        print('4. 얼음을 넣습니다.')
        print('5. 커피를 컵에 추가합니다.')
    elif choice==3:
        print('4. 커피를 컵에 추가합니다.')
        print('5. 헤이즐넛 시럽을 두 펌프 넣습니다.')

choice =0
while True:
    print('1. 아메리카노 2. 아이스아메리카노 3. 헤이즐넛아메리카노')
    choice = int(input('커피를 선택하세요.( 0. 프로그램 종료)>>'))
    if choice==0:
        print('프로그램을 종료합니다')
        break
    coffee(choice)

x=int(input('주문할 음료의 수를 입력하세요...>>>'))
for i in range(x):
    print('1. 아메리카노 2. 아이스아메리카노 3. 헤이즐넛아메리카노')
    choice= int(input('커피를 선택하세요>>> '))
    coffee(choice)
    print()

print('제조완료 후 진동벨을 누릅니다.')   








# def ea(x,y):

#     print('{} + {} = {}'.format(x,y,x+y)),
#     print('{} - {} = {}'.format(x,y,x-y)),
#     print('{} * {} = {}'.format(x,y,x*y)),
#     print('{} / {} = {}'.format(x,y,x/y))


# for i in range(3):

#     num1 = int(input('숫자를 입력하세요.>>'))
#     num2 = int(input('숫자를 입력하세요.>>'))
    
#     ea(num1,num2)

# # print(num1+num2)
# # print(num1-num2)
# # print(num1*num2)
# # print(num1/num2)

    