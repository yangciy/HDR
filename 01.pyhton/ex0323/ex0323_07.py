# list1=[9,2,7,4,5,6,8,3,1,10]
# add10=lambda num:num+10
# print(list(map(add10,list1)))
# print(list1)
# print(list(map(add10,list1)))

# print(list(filter(lambda num: num>5,list1)))
# print(list(filter(lambda num: num%2==0,list1)))
# print(list(map(lambda num: num>5,list1)))

# map(함수,리스트)

list2=[0,1,0,1,1]
list3=['','aaa','a','','aa']
for i in list2:
    if i==True:
        print(i,'True')
    else:
        print(i, 'False')