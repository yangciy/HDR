from student import Student
# import cx_Oracle

# def myConn():
#     conn = cx_Oracle.connect(user='admin', password='Epdlxjqpdltm1!',dsn='db_high')
#     return conn

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
    return choice
def stuInput():
    # conn = myConn()
    # cs = conn.cursor() 
    while True:
        print('학생성적입력')
        stuname=input("학생이름을 입력하세요.")
        if stuname=='0':
            break
        kor = int(input('국어성적 입력'))
        eng = int(input('영어성적 입력'))
        temp= Student(stuname,kor,eng)
        stuSave.append(temp)
        # sql="insert into studata values (stu_seq.nextval,:1,:2,:3,:4,:5.1)"
        # cs.execute(sql,(stuname,kor,eng,kor+eng,(kor+eng)/2))
        # cs.close()
        # conn.commit()
        # conn.close()
        print("{}번 학생 {}이 저장되었습니다.".format(temp.stuno,stuname))
        
def topTitle():
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)
    
def stuOutput():
    topTitle()
    # conn = myConn()
    # cs = conn.cursor() 
    # sql = "select * from studata order by stuno"
    # rows = cs.execute("select * from studata")
    # for row in rows:
    #     print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],sep='\t')

    for stu in stuSave:
        print(stu) 

    # cs.close()
    # conn.close() 

        
def stuSearch():
    # conn = myConn()
    # cs = conn.cursor() 
    print('학생검색출력')
    sname=input("검색할 학생의 이름을 입력")
    # sql = "select * from studata where stuname like '%"+sname+"%'"
    # cs.execute(sql)
    # rows = cs.fetchall()
    # if(len(rows) != 0):
    #     for row in rows:
    #         print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],sep='\t')
    #     print()
    #     print("{}의 데이터가 검색되었습니다.".format(cs.rowcount)) 
    count=0
    for stu in stuSave:
        if sname==stu:
            topTitle()
            print(stu)
            count=1
            break
    if count==0:
        print("입력한 학생이 없습니다. 다시입력하세요.")
    # cs.close()
    # conn.close() 
def stuModify():
    # count=0
    # conn = myConn()
    # rows = cs.fetchall()
    print("학생수정")
    sname=input("수정할 학생의 이름을 입력")
    # sql = "select * from studata where stuname like '%"+sname+"%'"
    # cs = conn.cursor() 
    # cs.execute(sql)
    # rows = cs.fetchall()

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
    # conn = myConn()
    # cs = conn.cursor()
    print('학생성적 삭제')
    sname=input("수정할 학생의 이름을 입력")
    # sql="delete studata where stuname='"+sname+"'"
    # cs.execute(sql)
    # cs.close()
    # conn.commit()
    # conn.close() 
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
#     conn = myConn()
#     cs = conn.cursor()
#     sql = "update studata a set rank=(select ranks from \
# (select rank() over(order by total desc) as ranks,stuno from studata) b where b.stuno = a.stuno)"
#     cs.execute(sql)            
#     cs.close()
#     conn.commit()
#     conn.close()