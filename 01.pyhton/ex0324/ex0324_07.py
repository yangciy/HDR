# exo324_07.py - main
# stu_class.py 클래스
# stu_func.py : 함수
# 학생성적프로그램
# 입력, 출력
# input
# print
import stu_func
from stu_class import Student
stuSave=[]
Student()
print('[ 학생성적 프로그램] ')
print('-'*30)
print('1. 학생성적입력')
print('2. 학생성적출력')
while True:
    choice= int(input('숫자를 입력'))
    if choice==1:
        stu_func.Stu_func.stuInput()
        stuSave.append(stu_func.Stu_func(stuNo,stuName,kor,eng))

    elif choice==2:
        stu_func.Stu_func.stuPrint()