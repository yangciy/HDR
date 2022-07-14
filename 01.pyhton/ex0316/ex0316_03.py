aa= [1,'홍길동',100,100,200,100.0,0]
for i in range(len(aa)):
    print('{} :{} '.format(i,aa[i]))

stu1 = {'no':1, 'name':'홍길동', 'kor':100, 'eng':100, 'total':200, 'avg':100.0,'rank':0}


for key in stu1:
    print('{} : {} '.format(key,stu1[key]))




# while True:
#     search = input('키 값을 입력하세요.>>>>  (0을 입력하면 프로그램이 종료됩니다.)')
    
#     if search in stu1:
#         print(stu1[search])
#     elif int(search)==0:
#         print('프로그램 종료 ')
#         print()
#         break
#     else:
#         print('입력한 키 값이 없습니다. 다시 입력하세요. ')
#         print()
        