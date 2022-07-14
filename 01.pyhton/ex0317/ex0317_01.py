# stulist=[
#     {'sno':1,'stuname':'길동','kor':100,'eng':100,'math':100,'total':100+100+100,'avg':(100+100+100)/3,'rank':0},
#     {'sno':2,'stuname':'홍이','kor':10,'eng':80,'math':40,'total':100+100+100,'avg':(100+100+100)/3,'rank':0},
#     {'sno':3,'stuname':'삼식','kor':100,'eng':40,'math':60,'total':100+100+100,'avg':(100+100+100)/3,'rank':0}
    
# ]



# cnt=0
# while True:
#     search_name= input('삭제할 학생의 이름을 입력하세요.> ')
#     for idx, stu in enumerate(stulist):
#         if search_name in stu.values():
#             print('{} 있습니다.'.format(search_name),end=' ')
#             cnt=1
#             print('{}이 삭제되었습니다.'.format(search_name))
#             del(stulist[idx])
#             break
        
#     if cnt==0:
#         print('{} 없습니다.'.format(search_name),end=' ')
#         print()
#         continue

# print(stulist)

# stu1={'sno':1,'stuname':'길동','kor':100,'eng':100,'math':100,'total':100+100+100,'avg':(100+100+100)/3,'rank':0}
# if '길동' in stu1.values():
            

    
# stu1={'sno':1,'stuname':'길동','kor':100,'eng':100,'math':100,'total':100+100+100,'avg':(100+100+100)/3,'rank':0}
# print(stu1['{}'.format(search_name)])
            
            


# studic= {'sno':1,'stuname':'길동','kor':100,'eng':100,'math':100,'total':100+100+100,'avg':(100+100+100)/3,'rank':0}

# print(studic.items())
# for k,v in studic.items():
#     print('{}:{}'.format(k,v),end=' ')
# for k in studic.keys():
#     print(k,studic[k])
# for v in studic.values():
#     print(v)    


# a=1

# print(a)
# a=3
# print(a)
      
# list1 = [1,2,3,4,5]
# list1[3]=5
# print(list1)
# del(list1[3])
# print(list1)

# dlist=[1,2,3,4,5]
# dtuple=(1,2,3,4,5)
# alist=[dlist,dtuple,ddict]

# print(dtuple[0])

# print(alist)

# #dicts
ddict={1:'1',2:'2a',3:'3d',4:'4f',5:'5s'}
print(ddict.keys())
print(ddict.values())
ddict[1]=111
del(ddict[4])
print(ddict)


