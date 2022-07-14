#list 0~100 
a=[]
for num in range(0,101):
    if num%2==0 and num>0:
        a.append(num)
    
print(a)
