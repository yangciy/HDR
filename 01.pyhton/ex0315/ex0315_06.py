aa=[1,2,333,4,555,6,77,8,9]
# 얕은 복사
# bb = aa
# aa[0] =500
# print('aa list:',aa)
# print('bb list:',bb)

# 깊은 복사
bb = aa.copy()
aa[0] =500
print('aa list:',aa)
print('bb list:',bb)








# aa=aa.sort()
# print(aa)
# print('--'*20)
# bb=aa.sort()
# print(bb)
# print('--'*20)
# cc= sorted(aa)
# print(cc)

# aa.extend([1,2,333])
# print(aa)
# print(aa.count(333))


# idx = aa.index(333)
# print(idx)

# aa.sort()
# print(aa)
# aa.sort(reverse=1)
# print(aa)

#지정한 값 삭제
# aa.remove(333)
# print(aa)
# aa.pop()
# print(aa)
# aa.clear()
# print(aa)

# #del
# aa[1:4]=[]
# print(aa)

# aa=[]
# print(aa)


# aa=None
# print(aa)
# print(type(aa))


# del(aa)      
# print(aa)
# print(type(aa))
