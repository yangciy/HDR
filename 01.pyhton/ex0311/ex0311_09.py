#두개의 숫자를 입력해서 두개 사이의 숫자를 더해라
#eval() : 문자를 숫자로 str -> int

num1 = int(input('숫자를 입력하세요'))
num2 = int(input('숫자를 입력하세요'))
sum=0

if num1>num2:
    temp=num1
    num1=num2
    num2=temp
    #num1,num2 = num2, num1 temp할 필요 없다
    for i in range(num1,num2+1):
        sum +=i 
    # for i in range(num2,num1+1):
    #     sum +=i 
    print(sum)   
elif num1==num2:
    print('숫자가 같습니다.')
else:
    for i in range(num1,num2+1):
        sum +=i 
    print(sum)   
