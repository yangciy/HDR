#0부터 100까지 7의 배수의 합을 구하여라 !

# sum=0
# sum_1=0


# for i in range(0,101):
#     if i%7==0 and i!=0:
#         sum+=i
#         print(i,end=' ')
# print('\n7의 배수의 합',sum)

# #0부터 100까지 홀수의 합
# for j in range(0,101):
#     if j%2==1 and j!=0:
#         sum_1+=j
#         print(j,end=' ')
# print('\n홀수의 합',sum_1)

#두수를 입력 받아 홀수의 값의 합을 출력 하시오.

num1=int(input('숫자를 입력하세요.>>'))
num2=int(input('숫자를 입력하세요.>>'))
sum_a=0
if num1>num2:
    num1,num2 = num2,num1
    for i in range(num1, num2+1):
        if i%2 ==1:
            sum_a+=i
            print(i,end=' ')
    print('\n두 수사이의 홀수 합',sum_a)            
else :
    for i in range(num1, num2+1):
        if i%2 ==1:
            sum_a+=i
            print(i,end=' ')
    print('\n두 수사이의 홀수 합',sum_a)            