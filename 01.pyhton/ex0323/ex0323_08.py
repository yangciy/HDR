try:
    input1 = int(input('숫자를 입력하세요.>> '))
    input2 = int(input('숫자를 입력하세요.>> '))
    print(input1/input2)
# except ValueError:
#     print('숫자가 아닙니다.')
# except ZeroDivisionError:
#     print('0으로 나누기는 가능하지 않다.')
except Exception as err:
    print(err)
print('프로그램 종료')