aa=[1,2,3]
bb=[4,5,6]

cc= aa+bb

print(cc)

print(cc[::2])
print(cc[::-2])
print(cc[::-1])

cc[0]=10

print(cc)
cc[1:2]=[20,21]
print(cc)
cc[1:3]=[50,40,30,20]
print(cc)


cc[5]=[1,2,3]
print(cc)

del(cc[1:3])
print(cc)