from student import Student
stuSave=[]
def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적출력')
    print('3. 학생검색출력')
    print('4. 학생성적수정')
    print('5. 학생성적삭제')
    print('6. 학생등수처리')
    print('0. 프로그램종료')
    print()
    choice = int(input('원하는 번호를 입력하세요.>>'))

def stuInput():
    while True:
        print('학생성적입력')
        stuname=input("학생이름을 입력하세요.")
        if stuname=='0':
            break
        kor = int(input('국어성적 입력'))
        eng = int(input('영어성적 입력'))
        temp= Student(stuname,kor,eng)
        stuSave.append(temp)
        print("{}번 학생 {}이 저장되었습니다.".format(temp.stuno,stuname))
        
def topTitle():
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)
    
def stuOutput():
    topTitle()
    for stu in stuSave:
        print(stu) 
        
def stuSearch():
    print('학생검색출력')
    sname=input("검색할 학생의 이름을 입력")
    count=0
    for stu in stuSave:
        if sname==stu:
            topTitle()
            print(stu)
            count=1
            break
    if count==0:
        print("입력한 학생이 없습니다. 다시입력하세요.")
        
def stuModify():
    print("학생수정")
    sname=input("수정할 학생의 이름을 입력")
    count=0
    for stu in stuSave:
        if sname==stu:
            tN=int(input("수정할 과목을 선택하세요. 1.국어 2.영어"))
            if tN==1:
                print('국어 성적을 수정합니다.')
                print("현재 국어성적 : {}".format(stu.kor))
                score=int(input('수정할 점수를 입력하세요.'))
                stu.setKor(score)
                print("{}로 변경되었습니다.".format(score))
            elif tN==2:
                print('영어 성적을 수정합니다.')
                print("현재 영어성적 : {}".format(stu.eng))
                score=int(input('수정할 점수를 입력하세요.'))
                stu.setEng(score)
                print("{}로 변경되었습니다.".format(score))
            count=1
            break
    if count==0:
        print("입력한 학생이 없습니다. 다시입력하세요.")
        
def stuDel():
    print('학생성적 삭제')
    sname=input("수정할 학생의 이름을 입력")
    count=0
    for i,stu in enumerate(stuSave):
        if sname==stu:
            print("{}학생이 검색되었습니다.".format(sname))
            flag=input("정말 삭제하시겠습니까? ")
            if flag =='y' or "Y":
                del(stuSave[i])
                print("{}학생이 삭제되었습니다.".format(sname))
            else:
                print("취소되었습니다.")
        if count==0:
          print("입력한 학생이 없습니다. 다시입력하세요.")
                
def rank():
    print('등수처리')
    for stu1 in stuSave:
        rankCount=1
    for stu2 in stuSave:
        if stu1<stu2:
            rankCount +=1
    stu1.rank = rankCount
        
    print("등수처리가 완료되었습니다.")                

            
