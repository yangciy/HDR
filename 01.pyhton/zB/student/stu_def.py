from student.stu import Student

stuSave=[]

def screePrint():
    print('[ 학생성적 프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 학생등수처리')
    print('0. 프로그램종료')
    print()
    
    choice =int(input('원하는 번호를 입력하세요.>>'))
    return choice

def setInput():
    while True:
        print('[ 학생성적 입력 ]')
        stuName = input('학생이름을 입력하세요.(0.종료)>>')
        if stuName=='0':
            break
        kor=int(input('국어성적을 입력하세요.>>'))
        eng=int(input('영어성적을 입력하세요.>>'))
        math=int(input('수학성적을 입력하세요.>>'))
        
        temp=Student(stuName,kor,eng,math)
        stuSave.append(temp)
        
        print('{}번. {} 학생이 저장되었습니다.'.format(temp.stuNo,temp.stuName))
        print()
        
def topTitle():
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
    print('-'*60)
    
def stuOutput():
    topTitle()
    for stu in stuSave:
        print(stu)
        
def stuSearch():
    print()
    print('[ 학생검색출력 ]')
    sname=input('학생이름을 입력하세요.>>')
    count=0
    for stu in stuSave:
        if stu in stuSave:
            topTitle()
            print(stu)
            count=1
            break
    if count ==0:
        print('검색된 이름이 없습니다. 다시 한번 입력하세요.!!')
        
def stuModify():
    print()
    print('[ 학생성적수정 ]')
    sname=input('학생이름을 입력하세요.>>')
    count=0
    for stu in stuSave:
        if stu == sname:
            print('{} 학생이 검색되었습니다.'.format(sname))
            print('[ 성적수정 ]')
            print('1. 국어점수')
            print('2. 영어점수')
            print('3. 수학점수')
            tempNum= int(input('수정할 과목의 번호를 입력하세요.>>'))
            if tempNum==1:
                print('현재 국어점수  {}'.format(stu.kor))
                score= int(input('수정할 점수를 입력하세요.>>'))
                stu.setKor(score)
                print('국어점수가 {}으로 변경되었습니다.'.format(score))
            elif tempNum==2:
                print('현재 영어점수  {}'.format(stu.eng))
                score= int(input('수정할 점수를 입력하세요.>>'))
                stu.setEng(score)
                print('영어점수가 {}으로 변경되었습니다.'.format(score))
            elif tempNum==3:
                print('현재 수학점수  {}'.format(stu.math))
                score= int(input('수정할 점수를 입력하세요.>>'))
                stu.setMath(score)
                print('수학점수가 {}으로 변경되었습니다.'.format(score))
            count=1
            break
        
        if count==0:
            print('검색된 이름이 없습니다. 다시 한번 입력하세요!!')
            
def stuDelete():
    print()
    print('[ 학생성적삭제 ]')
    sname = input('학생이름을 입력하세요.>>')
    count=0
    for i, stu in enumerate(stuSave):
        if stu == sname:
            print('{} 학생이 검색되었습니다.'.format(sname))
            flag =input('정말 삭제하시겠습니까?')
            if flag =='y' or flag =='Y':
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(sname))
            else :
                print('삭제가 취소되었습니다.')
            count=1
            break
    if count==0:
        print('검색된 이름이 없습니다. 다시 입력하세요')

def stuRank():
    for stu1 in stuSave:
        rankCount=1
        for stu2 in stuSave:
            if stu1 < stu2:
                rankCount +=1
        stu1.rank =rankCount
    print('등수처리가 완료되었습니다.')
    print()