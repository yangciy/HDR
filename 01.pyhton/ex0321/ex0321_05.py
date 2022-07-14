def calc(num1,num2,choice):
    result=0
    if choice==1:
        result=num1+num2
        return result
    elif choice ==2:
        result=num1-num2
        return result
    elif choice ==3:
        result=num1*num2
        return result
    elif choice ==4:
        result=num1/num2
        return result
print('[ 사칙연산 프로그램 ]')
print('1.+ 2.- 3.* 4./')    
choice= int(input('원하는 번호를 입력하세요.>>>'))
num1 = int(input('숫자를 입력하세요.>>>'))
num2 = int(input('숫자를 입력하세요.>>>'))


result=calc(num1,num2,choice)
print(result)
    



# def cal(a,b):
#     result=0
#     result=a+b
#     return result

# hap=cal(1,2)
# print(hap)


