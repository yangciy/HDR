#화면 출력 구성
#프로그램 무한 반복
#학생성적입력 부분을 구성
stuSave=[]
# stuSave= [[0]*8 for _ in range(0)]
cnt=0
while 1:
        
    print(' [ 학생 성적 프로그램 ]')
    print(' 1. 학생 성적 입력')
    print(' 2. 학생 성적 수정')
    print(' 3. 학생 성적 삭제')
    print(' 4. 학생 성적 전체 출력')
    print(' 5. 학생 검색 출력')
    print(' 6. 등수 처리')
    print(' 0. 프로그램 종료')
    print('='*20)
    choice= int(input('번호를 입력해주세요. '))
    if choice==1:
        print('학생 성적 입력을 선택하셨습니다.')
        print('{}번째 학생의 성적을 입력해주세요.'.format(cnt+1))
        name= input('이름을 입력해주세요.  ')
        kor= int(input('국어 성적을 입력해주세요.  '))
        eng= int(input('영어 성적을 입력해주세요.  '))
        math= int(input('수학 성적을 입력해주세요.  '))
        #리스트에 저장
        # stuSave[cnt][0]= cnt+1
        # stuSave[cnt][1]= name
        # stuSave[cnt][2]= kor               
        # stuSave[cnt][3]= eng                            
        # stuSave[cnt][4]= math                           
        # stuSave[cnt][5]= kor+eng+math
        # stuSave[cnt][6]= kor+eng+math/3     
        # stuSave[cnt][7]= 0
        temp={'sno':cnt+1,'stuname':name,'kor':kor,'eng':eng,'math':math,'total':kor+eng+math,'avg':(kor+eng+math)/3,'rank':0}
        stuSave.append(temp)
        cnt+=1
    
    elif choice==2:    #수정
        print('[ 학생 성적 수정페이지 ]')
        print('='*50)
        name_r=input('수정할 학생의 이름을 입력해주세요.  ')
        count=0
        for i,stu in enumerate(stuSave):
            if name_r in stu.values():
                print('{} 학생이 존재합니다.'.format(name_r))
                count=1
                choice = input('수정할 과목을 입력하세요.>> (0입력시 메인메뉴로 돌아갑니다.)\n')
                if choice=='0':
                    int(choice)
                    break
                if choice == '국어':
                    print('현재 국어점수 : ',stu['kor'])
                    kor= int(input(' 변경할 국어 성적을 입력해주세요.  '))
                    stu['kor']=kor
                    stu['total']=kor+eng+math
                    stu['avg']=stu['total']/3
                elif choice == '영어':
                    print('현재 영어 점수 : ',stu['eng'])
                    eng= int(input('영어 성적을 입력해주세요.  '))
                    stu['eng']=eng
                    stu['total']=kor+eng+math
                    stu['avg']=stu['total']/3
                elif choice == '수학':
                    print('현재 수학 점수 : ',stu['math'])
                    math= int(input('수학 성적을 입력해주세요.  '))
                    stu['math']=math
                    stu['total']=kor+eng+math
                    stu['avg']=stu['total']/3
                else :
                    print('잘못 입력하셨습니다. 다시 입력해주세요.')
                    continue                
                break
        if count==0:   
            print('{} 학생이 없습니다.'.format(name_r))
    
    elif choice==3:    #삭제
        print('학생 성적 삭제를 선택하셨습니다.')
        name_d=input('삭제할 학생의 이름 입력해주세요.  ')
        count=0
        for i,stu in enumerate(stuSave):
            if name_d in stu.values():
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(name_d))
                count=1
                break
        if count==0:   
            print('{} 학생이 없습니다.'.format(name_d))
        
    elif choice==4:    #출력
        print('학생 성적 전체 출력을 선택하셨습니다.')
        print('='*65)
        # print('{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}{:.5s}{:.5s}'.format('번호','이름','국어','영어','수학','합계','평균','등수'))
        print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
        print('='*65)
        for i in stuSave:
            for k,v in i.items():
                # print(j,end='\t')
                print('{}\t'.format(v),end='')
            print()  
            print('='*65)  
    elif choice==5:
        print('학생 검색 출력을 선택하셨습니다.')
        print('='*65)
        name_s=input('검색할 학생의 이름을 입력하세요.')
        count=0
        for i,stu in enumerate(stuSave):
            if name_s in stu.values:
                print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')
                print(stu['sno'],stu['stuname'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank'],sep='\t')
                count=1
                break
            if count==0:
                print('입력한 학생이 없습니다. 다시 검색해주세요')
    elif choice==6:
        print('등수 처리를 선택하셨습니다.')
        
        for stu in stuSave:
            rcount=1
            for stu2 in stuSave:
                if stu['total']<stu2['total']:            
                    rcount +=1
            stu['rank']=rcount
        print('등수 처리가 완료되었습니다.')
                
        # rank=[]
        # avgg=[]
        # avgg1=[]
        # for i , stu in enumerate(stuSave):
        #     print('번호: {}, 평균: {}'.format(i+1,stu['avg']))
        #     avgg.append(stu['avg'])
        #     avgg1.append(stu['avg'])
        #     avgg.sort(reverse=True)
        #     print(avgg)
        # print(avgg)
        # for i in avgg1:
        #     rank.append(avgg.index(i)+1)
        # print(rank)
        # for i , stu in enumerate(stuSave):
        #     stu['rank']=rank[i]
       
    elif choice==0:
        print('프로그램을 종료합니다.')
        break