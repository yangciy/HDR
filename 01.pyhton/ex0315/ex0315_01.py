# total=0
# for i in range(1,101):
#     total+=i
    
# print('1부터 100까지의 합:',total)

#2개의 입력한 숫자의 사이의 합을 구하라
# total=0
# a=int(input('첫번째 숫자를 입력하세요..>'))
# b=int(input('두번째 숫자를 입력하세요..>'))


# if a>b:
#     for i in range(a,b+1):
#         total+=i
        
#     print('{}와 {}사이의 합은 {} 입니다.'.format(a,b,total))
# else:
#     a,b=b=a
#     for i in range(a,b+1):
#         total+=i
        
#     print('{}와 {}사이의 합은 {} 입니다.'.format(a,b,total))


# 1차원 리스트
# arr_list=[1,2,3,4,5,6,7]
# for i in arr_list:
#     print(i)



# 2차원 리스트는 for문 두번 돌리기
# arr_list=[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]  
# for i in arr_list:
#     for j in i:
#         print(j)


# 가변 리스트는 2차원 리스트와 동일
arr_list=[[1,2,3,4,5], [6,7], [8,9,10]]
for i in arr_list:
    for j in i:
        print(j)