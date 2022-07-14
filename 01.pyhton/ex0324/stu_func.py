from stu_class import Student
s1= Student(1,'가',100,100)

cnt=0

stuSave=[]
class Stu_func(Student):
    
    def stuInput():
        
        stuNo=cnt
        print('학생 성적 입력을 선택하셨습니다.')
        print('{}번째 학생의 성적을 입력해주세요.'.format(cnt))
        stuName= input('이름을 입력해주세요.  ')
        kor= int(input('국어 성적을 입력해주세요.  '))
        eng= int(input('영어 성적을 입력해주세요.  '))
        stuSave.append(Stu_func(stuNo,stuName,kor,eng))
        print('저장되었습니다.')
        cnt
    def stuPrint():
        print('학생 성적 전체 출력을 선택하셨습니다.')
        print('='*65)
        # print('{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}{:.5s}{:.5s}'.format('번호','이름','국어','영어','수학','합계','평균','등수'))
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
        print('='*65)
        for stu in range(len(stuSave)):
            print(stu)  
