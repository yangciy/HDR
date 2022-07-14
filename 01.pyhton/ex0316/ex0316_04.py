student={
    'id':'aaa','pw':'1111','name':'길동', 'tel':'010-xxxx-xxxx','address':'seoul', 'gender':'male','hobby':'game'
}

# 1. 키값 검색 
# 2. value값 검색 
# 3. 딕셔너리 전체 출력 
# 원하는 번호를 입력하세요
# 프로그램을 구성하세요

while True:
    print('1. key 값 검색')
    print('2. value 값 검색')
    print('3. 딕셔너리 전체 출력')
    print('4. 프로그램 종료')

    choice = input('원하는 번호를 입력하세요.>> ')
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
   
        continue  
    choice=int(choice)
   
    if choice==1:
        while True:
            wK = input('검색할 key값을 입력하세요.> (0번 입력시 메인화면으로 돌아갑니다.)')
            if  wK.isdigit():
                if int(wK)==0:
                    print('메인메뉴로 돌아갑니다.')
                    break
            if wK in student:
                print('{}의 값은 : {}'.format(wK,student[wK]))
            # elif wK=='0':
            #     break
            else:
                print('key 값이 없습니다.')
    elif choice==2:
        while True:
            wV = input('검색할 value값을 입력하세요.> (0번 입력시 메인화면으로 돌아갑니다.)')
            if wV.isdigit():
                if int(wV)==0:
                    print('메인메뉴로 돌아갑니다.')
                    break        
            # if wV in student.values():
            #     print('value 값이 있습니다.')
            #     print('{}의 값은 : {}'.format(wV,student))
                # else :
                #     print('value 값이 없습니다.')
        
       
            kchk=0    
            for k in student:
                if student[k]==wV:
                    print('{} : {} 값이 있습니다.'.format(k,student[k]))
                    kchk=1
                    break
            if kchk==0:
                print('{}의 value 값은 없습니다.'.format(wV))
        
    elif choice==3:
        print(student)
        for stu in student:
            print('{} : {}'.format(stu,student[stu]))
    
    elif choice==4:
        print('프로그램 종료')
        break
    
    
