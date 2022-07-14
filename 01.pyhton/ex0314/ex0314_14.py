#4개의 값을 입력받아 합을 구하고 입력한 값을 출력하시오..


nums=[]
total=0
for i in range(4):
    num=int(input('{} 숫자를 입력하세요.>>>'.format(i+1)))
    nums.append(num)
for num in nums :
    total += num
print(total,nums)    
