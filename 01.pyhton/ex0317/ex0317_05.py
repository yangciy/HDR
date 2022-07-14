foods=['떡볶이','짜장면','라면','피자','맥주']
sides =['오뎅','단무지','김치','피클','땅콩']
# 1개의 주소값으로 두개가 동시에 사용
# copy() == [:]
foods2=foods[:]
print(foods)
foods2[0]='안판다'
foods2=foods.copy()
# foods2[0]='판다'
print(foods2)

# 튜플형태의 리스트로 변경
# 2개의 리스트를 딕셔너리로 변경
# tuple=list(zip(foods,sides))
# td=dict(tuple)
# print(type(dict(tuple)))
# print(tuple)
# print(td)


# for i in range(min(len(sides),len(foods))):
#         print('{}:{}'.format(foods[i],sides[i]))
# # min은 최소값 반납 max는 최대값 반납

# if len(foods)>len(sides):
#     for i in range(len(sides)):
#         print('{}:{}'.format(foods[i],sides[i]))
# else:
#     for i in range(len(foods)):
#         print('{}:{}'.format(foods[i],sides[i]))
# # for food,side in zip(foods,sides):
# #     print('{}:{}'.format(food,side))


# #complist=[0,1,2,3,4,5,6,7,8,9]

# alist=[i for i in range(10)]
# print(alist)

# blist=[]
# for i in range(1,21):
#     if i%3==0:
#         blist.append(i)
# # 한 줄 for 문
# clist=[i for i in range(1,21)   if i%3==0 if i<10 if i>5]
# print(blist)
# print(clist)