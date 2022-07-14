from temp import *
import os
content=[]
str1=''

str1= strInput(str1,content)

strFileSave(str1,content)
# print(os.listdir())
# 파일이 있으면 파일이름을 1_1.txt로 변경을 해서 저장하시오.

# str1=input('저장 할 파일의 이름을 입력하세요.')
# count=1
# while True:
#     temp = input('{}줄'.format(count))
#     if temp=='0':
#         break
#     content.append(temp+'\n')
#     count+=1
# if str1 in (os.listdir()):
#     print('{} 파일이 있습니다.'.format(str1))
#     str1 =str1[:str1.find('.')]+'_1'+str1[str1.find('.'):]
#     with open(str1,'w',encoding='utf-8') as file:
#         for i in range(len(content)):
#             file.write(content[i])

#         file.write('파일이름저장완료')
# else:
#     print('중복되는 이름이 없습니다.')    
#     with open(str1,'w',encoding='utf-8') as file:
#         for i in range(len(content)):
#             file.write(content[i])


# # if '1.txt' in os.listdir():
# #     print('있습니다. ')
# #     with open('1.txt','a',encoding='utf-8') as file:
# #         file.write('파일을 추가해서 저장시킵니다.\n')
# # else:
# #     print('없습니다. ')
# #     with open('1.txt','w',encoding='utf-8') as file:
# #         file.write('파일을 새로 만들어서 저장합니다.')