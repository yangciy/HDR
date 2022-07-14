# 1~25까지 list를 만들어보세요.

nums=[i for i in range(1,26)]
# 2차원 리스트를 생성
nums_2 =[[],[],[],[],[]]

for i,num in enumerate(nums):
    print(i, num)
    # nums_2[0].append(1,2,3,4,5)
    # nums_2[1].append(6,7,8,9,10)
    # nums_2[2].append(11,12,13,14,15)    
    nums_2[i//5].append(num)


print(nums_2)

print("[0][0] 데이터",nums_2[0][0])
print("[1][0] 데이터",nums_2[1][0])
print("[2][2] 데이터",nums_2[2][2])

    # print('{:2d}'.format(num),end=' ')
    # if num%5==0:
    #     print()
    
    
