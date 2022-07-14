a= [1]
b= [2]
c= a   # 리스트일 경우 주소가 복사됩니다.
print(a)
print(b)
print(c)

a[0]= 10
print(c)