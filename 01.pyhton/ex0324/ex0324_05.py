import student

stuSave=[]
while True:
    cnt = int(input('학생번호를 입력하세요.(0. 종료)'))
    if cnt==0:
        break
    name = input('이름을 입력하세요.')
    kor = int(input('국어점수를 입력하세요.'))
    eng = int(input('영어점수를 입력하세요.'))
    math = int(input('수학점수를 입력하세요.'))
# temp=student.Student(cnt,name,kor,eng,math)
    stuSave.append(student.Student(cnt,name,kor,eng,math))
    
# 홍길동, 이순신    
temp=int(input('홍길동의 국어점수를 변경하세요.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'))

tempName=input('홍길동의 이름을 변경하세요>>>')
stuSave[0].setName(tempName)

stuSave[0].setKor(temp)

print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
for stu in stuSave:
    print(stu)