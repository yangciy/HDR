students=[
    [1,'a',100,100,100,100,0,0],
    [2,'b',100,100,100,100,0,0],
    [3,'c',100,100,100,100,0,0],
    [4,'d',100,100,100,100,0,0],
    [5,'e',100,100,100,100,0,0]
]

while 1:
    print('1. 검색')
    print('2. 삭제')
    print('3. 전체 출력')
    print('0. 프로그램 종료')
    choice=input('실행할 번호를 입력해주세요..>>>>>')
    chk=0

    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        print()
        continue
    choice =int(choice)
    if choice==1:
        search= input('검색할 이름을 입력하세요>>>>>')
        chk=0
        for stu in students:
            if search in stu:
                for s in stu:
                    print(s,end=' ')
                    chk=1
                print()
                print()
                break
        if chk==0:
            print('찾는 학생이 없습니다. 다시 입력해주세요.')
    elif choice==2:  
        if students==[]:
            print('더이상 삭제할 정보가 없습니다.')
        else:
            search=input('삭제할 이름을 입력하세요>>>>')
            for idx,stu in enumerate(students):
                if search in stu:
                    del(students[idx])
                    chk=1
                    print('삭제되었습니다. ')
                    break
            if chk==0:
                print('학생이 없습니다. 다시 입력해주세요.')
            
            print()
    elif choice==3:
        print(students)      
        print()
    elif choice==0:
        print('프로그램 종료')
        break
    else :
        print('잘못 입력하셨습니다. 다시 입력해주세요.')