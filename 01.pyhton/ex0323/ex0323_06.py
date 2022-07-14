# 입력한 값을 + 10 더해라 이거지
# lamda함수로 만들어서 출력하라는거지

list1=[1,2,3,4,5]
for i in range(len(list1)):
    list1[i]=(lambda num:num+10)(list1[i])
print(list1)




# # def hap(x):
#     result = x +10
#     return result
# hap2 = lambda x : x+10

# print(hap2(3))
# # def x():
# #     i=0
# #     for i in range(1,101):
# #         return i
# hap2 = lambda x,y : hap
# print(hap2(1,101))




# def hap(num1,num2):
#     result = num1+num2
#     return result

# hap(99,1)

# hap2 = lambda num1,num2:print(num1+num2)
# # hap2(100,lambda num1,num2:print(num1+num2))
# hap2(10,20)
# def fun1(v1,v2):
#     def fun2(num1,num2):
#         return num1+num2
#     return fun2(v1,v2)

# print(fun1(20,20))