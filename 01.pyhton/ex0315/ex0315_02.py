list1= ['주바다','공유진','김샛별','송선유','양홍욱','윤상운','이한구']


while 1:
    search= input('찾을 이름을 입력하세요...>>>>>>')
    if search in list1:
        print('출석 했습니다.')
    else:
        print('출석 전입니다.')
# list1 = [i for i in range(0,10)]
# print(list1)
# print(type(list1))
# for i in range(0,10):
#     print(i)


# # list1= ['주바다','공유진','김샛별','송선유','양홍욱']

# # # for idx,i in enumerate(list1):
# # #     print('{}.{}'.format(idx+1,i))
    
# # # idx =1

# # # for i in list1:
# # #     print('{}. {}'.format(idx,i)) 
# # #     idx+=1
    
    
# # for i in range(len(list1)):
# #     print('{}. {}'.format(i+1,list1[i]))       





# # # print('[2단]\t\t[3단]\t\t[4단]\t\t[5단]\t\t[6단]\t\t[7단]\t\t[8단]\t\t[9단]')
# # # for p in range(2,10):
# # #     print('[ {:3d}단  ]\t'.format(p),end='')
# # # print()    
# # # for i in range(1,10):
# # #     for j in range(2,10):
# # #         print('{} * {} = {} '.format(j,i,j*i),end='\t')
# # #     print()   