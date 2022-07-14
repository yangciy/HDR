# aa list 100개, 0 2 4 8 ...

aa=[]
bb=[]

for i in range(200):
    aa.append(i*3)
for j in range(200):
    bb.append(200-j)


print(aa[2:5])
print(aa[190:210])
print(aa[190:-5])
# for i in range(100):
#     aa.append(i*2)
# print(aa)    
# for j in range(100):
#     bb.append(aa[99-j])
    
# print(bb)

