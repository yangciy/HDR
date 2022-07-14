import errno


while True:
    try:
        a=int(input('숫자를 입력하세요.>>>'))
        print(a)
    except Exception as err:
        print(err)
        print('숫자가 아닙니다.')
    



# a=int(input('정수를 입력하세요.>>'))
# print

# # try:
# #     a=int(input('정수를 입력하세요.>>'))
# #     print(a)
# # except:    
# #     print('print명령은 완벽합니다.')
    
# print('프로그램을 종료합니다.')