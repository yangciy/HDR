# set형태 - 중복을 제거
# myset={1,2,3,4,5,5}
# print(myset)
# list를 set으로 타입변경
# mylist=[9,12,4,4,5,5,1,2,6,7,8]
# print(mylist)
# myset=set(mylist)
# print(myset)
# mylist=list(myset)
# print(mylist)
# set 추가 제거
# myset={1,2,3}
# myset.add(4)
# print(myset)
# myset.remove(2)
# print(myset)
# myset.clear()
# print(myset)
adic={1,2,3,4,5}
bdic={3,4,5,6,7}

print(adic|bdic) #합집합
print(adic&bdic) #교집합
print(adic-bdic) #차집합
print(bdic-adic)
print(adic^bdic) #대칭집합(합-교)



# saleList=['삼각김밥','바나나','도시락','삼각김밥','도시락','오뎅','바나나']
# print(set(saleList))
# saledic=set(saleList)

# zipcode1 = {66012,66017,66076,66013,66019}
# zipcode2 = {66012,66017,66076,66015,66018}

# zipcode3= zipcode1-zipcode2
# print(zipcode3)
# zipcode3= (zipcode1|zipcode2)
# print(zipcode3)









# # tdic={'pig':'돼지','tiger':'호랑이',
# #       'lion':'사자','dog':'개'}
# # dtuple= list(tdic.items())
# # print(tdic)
# # dtuple.sort(reverse=True)
# # print(type(dtuple))
# # tdic=dict(dtuple)
# # print(tdic)
# # print(type(tdic))


# numdic= {1,2,33,3,3,5,1,9,2,3}
# numdic2= {2,3,4,5,2,3,9,10,11,13}
# print(numdic)
# print(numdic2)
# print(numdic|numdic2)                   #합집합
# print(numdic&numdic2)                   #교집합
# print(numdic-numdic2)                   #차집합
# print(numdic2-numdic)                                        
# numdic=list(numdic)
# numdic.sort

# # adic={1:'aaa',2:'bbb',3:'ccc',1:'ddd'}
# # adic=set(adic)
# # print(adic)
# tempdic1={1,2,33,3,3,5,1,9,2,3}

# nlist1=[1,2,3,4,5]
# nlist2=[3,4,5,8,2]