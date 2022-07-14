import os

with open('1.txt','w',encoding='utf-8') as file:
    file.write ('1\t홍길동\t100\t100\t200\t100.0\t0\n')
    file.write ('2\t김김김\t100\t100\t200\t100.0\t0\n')
    file.write ('3\t이이이\t100\t100\t200\t100.0\t0\n')
    file.write ('4\t박박박\t100\t100\t200\t100.0\t0\n')
    file.write ('5\t최최최\t100\t100\t200\t100.0\t0\n') 


    





# open받는 file 에서는 꼭 close()를 해야함
# file = open('1.txt','w',encoding='utf-8')
# file.write('글을 다른형태로 작성중입니다.\n')
# file.write('글을 다른형태로 작성중입니다2.')
# file.close()
# with open('1.txt','w',encoding='utf-8') as file:        # w는 덮어쓰기, a는 추가
#     file.write('파이썬 수업이 가.\n ㅎㅎ')
#     file.write('파이썬 수업이 마.\n')
#     file.write('파이썬 수업이 라.\n')
#     file.write('파이썬 수업이 다.\n')
#     file.write('파이썬 수업이 마.\n')
#     file.write('파이썬 수업이 라.\n ㅎㅎ')
#     file.write('파이썬 수업이 다.\n ㅎㅎ')
#     file.write('파이썬 수업이 나.\n ㅎㅎ')
#     file.write('파이썬 수업이 가.\n ㅎㅎ')

# with open('1.txt','a',encoding='utf-8') as file:
#     file.write('다시 글을 입력합니다.\n')
#     file.write('다시 글을 입력합니다.\n')
#     file.write('다시 글을 입력합니다.\n')


# print(os.name)
# print(os.getcwd())  # 현재 위치
# print(os.listdir()) # 현재 위치에 무슨 폴더가 있는지 출력

# os.mkdir('py')    # 폴더 생성
# os.rmdir('py')    # 폴더 삭제