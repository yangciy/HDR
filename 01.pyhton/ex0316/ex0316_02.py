stu1 = {'stu_no':1,'name':'홍길동','major':'컴퓨터공학과'}

print(stu1['name'])

# 키값이 없으면 None
print(stu1.get('tel'))

# 키값이 없으면 에러
# print(stu1['tel'])
# 키 값 전체 출력
print(stu1.keys())
print(list(stu1.keys()))

# value 값 전체 출력
print(stu1.values())
print(list(stu1.values()))
# print(type(stu1.values()))
print(stu1)
print(stu1.items())

print('tel' in stu1)
if 'name' in stu1:
    print(stu1[' name'])
    print('있다.')
else:
    print('없다.')
    

aa=[1,2,3,4,5,6,7,8,9,0]
if 10 in aa:
    print('있다.')
else:
    print('없다.')


# print(stu1['major'])
# print(stu1['stu_no'])
# #stu_no    변수
# #stuNo()   함수
# #StuNo     클래스
# print(stu1)
# #딕셔너리 추가


# stu1['kor']=100
# print(stu1)

# #딕셔너리 삭제
# del(stu1['kor'])
# print(stu1)


# stu= [1,'홍길동',100,100,200,100,0]


# aa={'no':1,'name':'홍길동','kor':100,'eng':100,'total':200}


# print(aa)
# print(stu)

# print(aa['name'],'\"')

# aa=[
#     [1,2,3,4],
#     [5,6],
#     [7,8]
# ]    

# for a2 in aa:
#     print(a2)
#     for i in a2:
#         print(i)